import matplotlib.pyplot as plt


def plot_fig(model_result: list,
             crs_result: list):
    plt.figure()
    plt.plot(model_result, crs_result, 'b-o')
    plt.xlabel('model_result')
    plt.ylabel('crs_result')

    plt.xlim([0, 1.1])
    plt.ylim([0, 1.1])
    plt.show()
