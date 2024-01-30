from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def dataToDataNum(data):
    """convert data to numeric"""
    for col in data.columns:
        if data[col].dtype == object:
            data[col] = data[col].str.replace('M', 'e6')
            data[col] = data[col].str.replace('k', 'e3')
            data[col] = pd.to_numeric(data[col], errors='coerce')
    return data


def main():
    """plot the life expectancy of France and Belgium from 1800 to 2050"""
    data = load("population_total.csv")
    data.set_index("country", inplace=True)
    data = dataToDataNum(data)
    data.loc['Belgium', "1800":"2050"].plot(kind="line", color="royalblue")
    data.loc['France', "1800":"2050"].plot(kind="line", color="green")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks([0, 40, 80, 120, 160, 200, 240],
               [1800, 1840, 1880, 1920, 1960, 2000, 2040])
    plt.yticks([0.20e8, 0.40e8, 0.60e8],
               ["20M", "40M", "60M"])
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
