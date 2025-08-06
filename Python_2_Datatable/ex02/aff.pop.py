from load_csv import load_csv
import matplotlib.pyplot as plt

def convert_to_millions(value):
	"""
    Preprocesses the population string to convert it into
    a numeric value in standard form.

    Args:
        pop_str (str): Population string with or without
        the 'M' suffix for million.

    Returns:
        float: Numeric population value.
    """
	if value.endswith('M'):
		return float(value[:-1]) * 1e6
	elif value.endswith('K'):
		return float(value[:-1]) * 1e3
	return float(value)

def main():
	# Load the CSV file
	data = load_csv('population_total.csv')

	# Check if data is loaded successfully
	if data is not None:
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
		plt.legend()
		plt.tight_layout()
		max_pop = max(max(belgium_pop), max(france_pop))
		y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
		plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
		plt.savefig('france_belgium_population.jpg')

	else:
		print("Failed to load data.")

if __name__ == "__main__":
	main()