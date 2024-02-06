from load_csv import load
import matplotlib.pyplot as plt


def main():
    """plot the life expenctancy compared to the income per person in 9000"""
    life_data = load("life_expectancy_years.csv")
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    final_data = life_data[["1900"]].copy()
    final_data.insert(1, "income", income_data["1900"])
    final_data.plot(kind="scatter", x="income",
                    y="1900", logx=True, linewidth=2)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xticks([300, 1000, 10000],
               ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
