from gurobipy import *

epsilon = 0.001


def DEA(single_data: list,
        model_type="CRS"
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
                theta[h] = m.addVar(vtype=GRB.CONTINUOUS,
                                    lb=-1000, name="theta_%s" % h)
                Si[h] = m.addVars(
                    I, lb=0, vtype=GRB.CONTINUOUS, name="Si_%s" % h)
                Sr[h] = m.addVars(
                    O, lb=0, vtype=GRB.CONTINUOUS, name="Sr_%s" % h)

            m.update()
            # Add objective function
            m.setObjective(
                theta[h] - epsilon * (sum(Si[h][i] + Si[h][i] for i in range(I))), GRB.MINIMIZE)

            # Add constraints
            # for each input
            for i in range(I):
                m.addConstr(quicksum(λ[j]*X[j][i]
                            for j in DMU) + Si[h][i] == theta[h]*X[h][i])
            # for each output
            for r in range(O):
                m.addConstr(quicksum(λ[j]*Y[j][r]
                            for j in DMU) - Sr[h][r] >= Y[h][r])

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

    # return E
    return list(E.values()), feasible
