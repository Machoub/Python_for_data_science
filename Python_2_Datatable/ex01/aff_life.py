import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(data, country: str = None):
    """Plot the life expectancy of a given country over the years."""
    try:
        if data is None:
            raise ValueError("The data provided is None.")
        if not isinstance(data, pd.DataFrame):
            raise TypeError("The data must be a pandas DataFrame.")
        if country is not None and not isinstance(country, str):
            raise TypeError("The country parameter must be a string or None.")
        if country is None:
            print("No country specified.")
            return
        france_data = data.loc[country]
        if france_data.empty:
            print("No data found for the specified country.")
            return
        years = france_data.index
        life_expectancy = france_data.values
        plt.plot(years, life_expectancy)
        plt.title(f'Life Expectancy in {country} Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.xticks(years[::40])
        plt.show()
    except ValueError as ve:
        print(f"Value error: {ve}")
        return
    except TypeError as te:
        print(f"Type error: {te}")
        return
    except KeyError:
        print(f"Key error: The country '{country}' "
              "does not exist in the data.")
        return
    except Exception as e:
        print(f"An error occurred while plotting the data: {e}")
        return


def main():
    """Plot the life expectancy of France over the years and save it."""
    data = load('life_expectancy_years.csv')
    if data is not None:
        data.set_index('country', inplace=True)
        aff_life(data, country='France')
    else:
        print("Failed to load data.")


if __name__ == "__main__":
    main()
