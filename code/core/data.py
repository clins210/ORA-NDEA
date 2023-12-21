import random


def input_generator(idx):
    # INPUT
    age = random.randint(1, 179)
    risk = random.randint(1, 50)
    size = random.randint(5000, 9999)  # 5000–9999
    returns = [age, risk, size]

    # return INPUT
    return float(returns[idx])
    # return [float(age), float(risk), float(size)]


def output_generator():
    # OUTPUT
    # 0.5 bn to 1 bn
    sale = random.randint(5, 10)

    # return OUTPUT
    return float(sale)


def generate_dataset(N: int,
                     type,
                     input_idx):
    # Data generator

    K = 3
    X, Y = {}, {}
    DMU = []

    for j in range(N):
        DMU.append(j)
        X[j] = {}
        Y[j] = {}
        if type == "SD":
            same_input = input_generator(input_idx)
            for k in range(K):
                X[j][k] = same_input
                Y[j][k] = output_generator()

        elif type == "DS":
            same_output = output_generator()
            for k in range(K):
                X[j][k] = input_generator(input_idx)
                Y[j][k] = same_output

        elif type == "DD":
            for k in range(K):
                X[j][k] = input_generator(input_idx)
                Y[j][k] = output_generator()

    return DMU, X, Y


def dataset_to_txt(dataset,
                   file_path=""):
    DMU, X, Y = dataset


def text_to_dataset(file_path):

    DMU, X, Y = dataset
