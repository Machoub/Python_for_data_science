from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def convert_to_millions(value):
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.

    Args:
        value (str): Population string with or without
        the 'M' (million) or 'K' (thousand) suffix.

    Returns:
        float: Numeric population value.
    """
    if value.endswith('M'):
        return float(value[:-1]) * 1e6
    elif value.endswith('K'):
        return float(value[:-1]) * 1e3
    return float(value)


def aff_pop(data):
    """Plot the population of France and Belgium from 1800 to 2050.

    Args:
        data (pd.DataFrame): the population dataset, with a 'country'
            column and one column per year.

    Errors are caught and reported with a message; nothing is plotted then.
    """
    try:
        if data is None:
            raise ValueError("The data provided is None.")
        if not isinstance(data, pd.DataFrame):
            raise TypeError("The data must be a pandas DataFrame.")
        cols_to_drop = data.columns.get_loc('2051')
        data = data.iloc[:, :cols_to_drop]
        France_data = data[data['country'] == 'France'].iloc[:, 1:]
        belgium_data = data[data['country'] == 'Belgium'].iloc[:, 1:]
        france_pop = France_data.values.flatten()
        belgium_pop = belgium_data.values.flatten()
        years = France_data.columns[:].astype(int)
        france_pop = [convert_to_millions(str(pop)) for pop in france_pop]
        belgium_pop = [convert_to_millions(str(pop)) for pop in belgium_pop]

        plt.plot(years, france_pop, label='France', color='blue')
        plt.plot(years, belgium_pop, label='Belgium', color='green')
        plt.title('Population of France and Belgium Over Time')
        plt.xticks(years[::40])
        plt.ylabel('Population')
        plt.xlabel('Year')
        plt.legend()
        max_pop = max(max(belgium_pop), max(france_pop))
        y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
        plt.yticks(y_ticks[::2],
                   ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks[::2]])
        plt.tight_layout()
        plt.show()
    except ValueError as ve:
        print(f"Value error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")
    except KeyError as ke:
        print(f"Key error: {ke} was not found in the data.")
    except Exception as e:
        print(f"An error occurred while plotting the data: {e}")


def main():
    """Load the population data and plot France against Belgium."""
    data = load('population_total.csv')
    if data is not None:
        aff_pop(data)
    else:
        print("Failed to load data.")


if __name__ == "__main__":
    main()
