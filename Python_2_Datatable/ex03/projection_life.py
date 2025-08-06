import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load_csv

def main():
	# Load the CSV file
	LF_data = load_csv('life_expectancy_years.csv')
	data_income = load_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

	# Check if data is loaded successfully
	if LF_data is not None and data_income is not None:
		years = '1900'
		gdp = data_income[years]
		life_expectancy = LF_data[years]

		plt.scatter(gdp, life_expectancy)
		plt.title('1900')
		plt.xlabel('Gross domestic product')
		plt.ylabel('Life expectancy')
		plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
		plt.tight_layout()
		plt.savefig('projection_life_1900.png')

	else:
		print("Failed to load data.")

if __name__ == "__main__":
	main()