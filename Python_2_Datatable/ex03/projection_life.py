import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def projection_life(data_income, LF_data):
    """Plot life expectancy against GDP per person in 1900."""
    try:
        if data_income is None or LF_data is None:
            raise ValueError("One or both of the data provided are None.")
        if (not isinstance(data_income, pd.DataFrame)
                or not isinstance(LF_data, pd.DataFrame)):
            raise TypeError(
                "Both data_income and LF_data must be pandas DataFrames.")

        years = '1900'
        gdp = data_income[years]
        life_expectancy = LF_data[years]

        plt.scatter(gdp, life_expectancy)
        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.xscale('log')
        plt.ylabel('Life expectancy')
        plt.legend(['GDP vs Life Expectancy'])
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()

    except ValueError as ve:
        print(f"Value error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")
    except KeyError as ke:
        print(f"Key error: {ke}. "
              f"Please check if the year '{years}' exists in the data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """Plot life expectancy against GDP per person in 1900 and save it."""
    # Load the CSV file
    try:
        LF_data = load('life_expectancy_years.csv')
        data_income = load(
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

        # Check if data is loaded successfully
        if LF_data is not None and data_income is not None:
            projection_life(data_income, LF_data)
        else:
            print("Failed to load data.")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
