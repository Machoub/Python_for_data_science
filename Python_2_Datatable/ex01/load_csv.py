import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_csv(path: str) -> pd.DataFrame:
	"""
	Load a CSV file into a pandas DataFrame.
	
	Parameters:
	file_path (str): The path to the CSV file.
	
	Returns:
	pd.DataFrame: DataFrame containing the data from the CSV file.
	"""
	try:
		if not path.endswith('.csv'):
			raise ValueError("The provided file path does not point to a CSV file.")
		if not isinstance(path, str):
			raise TypeError("The file path must be a string.")
		if len(path) == 0:
			raise ValueError("The file path cannot be an empty string.")
		data = pd.read_csv(path)
		return data
	except FileNotFoundError:
		print(f"File not found: {path}")
		return None
	except pd.errors.EmptyDataError:
		print("No data found in the CSV file.")
		return None
	except pd.errors.ParserError:
		print("Error parsing the CSV file. Please check the file format.")
		return None
	except ValueError as ve:
		print(f"Value error: {ve}")
		return None
	except TypeError as te:
		print(f"Type error: {te}")
		return None
	except Exception as e:
		print(f"An error occurred while loading the CSV file: {e}")
		return None

def main():
	# Load the CSV file
	data = load_csv('life_expectancy_years.csv')
	
	# Check if data is loaded successfully
	if data is not None:
		france_data = data[data['country'] == 'France']
		if france_data.empty:
			print("No data found for France.")
			return
		years = france_data.columns[1:]
		life_expectancy = france_data.iloc[0, 1:].values
		plt.plot(years, life_expectancy)
		
		plt.title('Life Expectancy in France Over the Years')
		plt.xlabel('Year')
		plt.ylabel('Life Expectancy (years)')

		# Définit les graduations de l'axe X pour n'afficher qu'une année toutes les 40 ans
		plt.xticks(years[::40])
		plt.savefig('france_life_expectancy.jpg')
	else:
		print("Failed to load data.")

if __name__ == "__main__":
	main()