import matplotlib.pyplot as plt


def plot_fig(input_output_type: str,
             res_NDEA_CRS: list,
             res_NDEA_VRS: list,
             res_DEA_CRS: list,
             res_DEA_VRS: list):

    plt.plot(res_NDEA_CRS, label="NDEA_CRS")
    plt.plot(res_NDEA_VRS, label="NDEA_VRS")
    plt.plot(res_DEA_CRS, label="DEA_CRS")
    plt.plot(res_DEA_VRS, label="DEA_VRS")
    plt.xlabel('DMU')

    plt.ylabel('efficiency')
    plt.xticks(list(range(len(res_NDEA_CRS))))
    plt.legend()
    plt.title(f"Type of {input_output_type}")
    plt.show()
    plt.close()
