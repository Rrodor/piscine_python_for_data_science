from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")
    data.set_index("country", inplace=True)
    data.loc['France'].plot(kind="line")
    plt.title("France Life expectancy Projections")
    plt.xticks([0, 40, 80, 120, 160, 200, 240, 280],
               [1800, 1840, 1880, 1920, 1960, 2000, 2040, 2080])
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
