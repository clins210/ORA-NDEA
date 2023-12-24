from gurobipy import *


# Global
epsilon = 0.001


def NDEA(single_data,
         model_type
         ):
    '''
    args:
        single_data: DMU, X, Y
    returns:
        list of efficiency
        list of feasiable checker
    '''

    assert len(single_data) != 0, "No Data"

    DMU, X, Y = single_data

    # feasiable checker
    feasible = [False for i in range(len(DMU))]

    # record the efficiency
    E = {}

    # For each DMU

    for r in DMU:
        try:
            # number of stage
            K = 3
            H = K

            # number of DMU
            N = len(DMU)

            m_k = [1, 1, 1]
            r_k = [1, 1, 1]

            w = [1/3, 1/3, 1/3]

            m = Model("model")
            m.setParam('OutputFlag', False)  # Muting the optimize function

            # add variables
            λ = m.addVars(N, K, lb=0, vtype=GRB.CONTINUOUS, name="λ_")  # λ_jk
            w_j = m.addVars(N, K, lb=0, vtype=GRB.CONTINUOUS, name="w_j_")

            s_neg = m.addVars(N, 5, lb=0, vtype=GRB.CONTINUOUS, name="s_neg_")
            s_pos = m.addVars(N, K, lb=0, vtype=GRB.CONTINUOUS, name="s_pos_")

            #  set Objective
            m.setObjective(
                quicksum(w[k] * (1 - (s_neg[r, k] / X[r][k])) for k in range(K)), GRB.MINIMIZE)

            # add Constrs
            for k in range(K):
                # turn on is VRS
                if model_type == "VRS":
                    m.addConstr(sum(λ[j, k] for j in range(N)) == 1, "C9")
                m.addConstr(sum(w_j[j, k] for j in range(N)) == 1, "C10")

            # k=0
            m.addConstr((X[r][0] == sum(X[j][0] * λ[j, 0] + s_neg[r, 0] for j in range(N))), "C1")  # input: X1
            m.addConstr((Y[r][0] == sum(Y[j][0] * λ[j, 0] - s_pos[r, 0] for j in range(N))), "C2")  # output: Y1(z2)

            # k=1
            m.addConstr((X[r][1] == sum(X[j][1] * λ[j, 1] + s_neg[r, 1] for j in range(N))), "C3")  # input: X2
            m.addConstr((Y[r][1] == sum(Y[j][0] * λ[j, 1] + s_neg[r, 3] for j in range(N))), "C4")  # input: Y1(z1)
            m.addConstr((Y[r][1] == sum(Y[j][1] * λ[j, 1] - s_pos[r, 1] for j in range(N))), "C5")  # output: Y2(z2)

            # k=2
            m.addConstr((X[r][2] == sum(X[j][2] * λ[j, 2] + s_neg[r, 2] for j in range(N))), "C6")  # input: X3
            m.addConstr((Y[r][2] == sum(Y[j][2] * λ[j, 2] + s_neg[r, 4] for j in range(N))), "C7")  # input: Y2(z2)
            m.addConstr((Y[r][2] == sum(Y[j][2] * λ[j, 2] - s_pos[r, 2] for j in range(N))), "C8")  # output: Y3

            # (k, h) pairs
            # z[j ,0, 1] = Y[j, 0]
            m.addConstr(((sum(Y[j][0] * λ[j, 0] for j in range(N)) - sum(Y[j][0] * λ[j, 1] for j in range(N))) <= 0.1), "C5-1")
            # z[j ,1, 2] = Y[j, 1]
            m.addConstr((sum(Y[j][1] * λ[j, 1] for j in range(N)) - sum(Y[j][1] * λ[j, 2] for j in range(N)) <= 0.1), "C5-2")

            m.optimize()

            if m.Status == 2:
                # Store the result
                E[r] = m.objVal
                feasible[r] = True
            else:
                E[r] = m.Status

        except GurobiError:
            E[r] = 'GurobiError reported'

    # return E, feasible
    return list(E.values()), feasible


def DEA(single_data: list,
        model_type
        ):
    '''
    args:
        single_data: DMU, X, Y
    returns:
        list of efficiency
        list of feasiable checker
    '''

    assert len(single_data) != 0, "No Data"

    DMU, X, Y = single_data

    # Calculate the length of input and output
    I = len(X[0])
    O = len(Y[0])

    # feasiable checker
    feasible = [False for i in range(len(DMU))]

    # record the efficiency
    E = {}

    # For each DMU
    for h in DMU:
        try:
            # The decision variables
            theta, λ, Sr, Si = {}, {}, {}, {}
            # Initialize LP model
            m = Model("Dual_of_DEA_model")
            m.setParam('OutputFlag', False)  # Muting the optimize function

            # Add decision variables
            for r in DMU:
                λ[r] = m.addVar(vtype=GRB.CONTINUOUS, name="λ_%s" % r)
                theta[h] = m.addVar(vtype=GRB.CONTINUOUS, lb=-1000, name="theta_%s" % h)
                Si[h] = m.addVars(I, lb=0, vtype=GRB.CONTINUOUS, name="Si_%s" % h)
                Sr[h] = m.addVars(O, lb=0, vtype=GRB.CONTINUOUS, name="Sr_%s" % h)

            m.update()
            # Add objective function
            m.setObjective(theta[h] - epsilon * (sum(Si[h][i] + Si[h][i] for i in range(I))), GRB.MINIMIZE)

            # Add constraints
            # for each input
            for i in range(I):
                m.addConstr(quicksum(λ[j]*X[j][i] for j in DMU) + Si[h][i] == theta[h]*X[h][i])
            # for each output
            for r in range(O):
                m.addConstr(quicksum(λ[j]*Y[j][r] for j in DMU) - Sr[h][r] >= Y[h][r])

            # turn on is VRS
            if model_type == "VRS":
                m.addConstr(sum(λ[j] for j in DMU) == 1)

            # Start optimize the formulation
            m.optimize()

            if m.Status == 2:
                # Store the result
                E[h] = m.objVal
                feasible[r] = True
            else:
                E[h] = m.Status
            # E[h] = "The efficiency of DMU %s:%0.3f" % (h, m.objVal)

        except GurobiError:
            continue
            # print('GurobiError reported')
    print(list(E.values()))
    # return E
    return list(E.values()), feasible
