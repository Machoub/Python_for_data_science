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
	data = load_csv('population_total.csv')

	# Check if data is loaded successfully
	if data is not None:
		new_data = data.loc[['France', 'Belgium']].T
		
		def convert_to_millions(value):
			value = str(value).strip().upper()
			if value.endswith('M'):
				return float(value[:-1]) * 1e6
			elif value.endswith('K'):
				return float(value[:-1]) * 1e3
			return value
		
		new_data = new_data.applymap(convert_to_millions)
		

		plt.plot(new_data.index, new_data['France'], label='France')
		plt.plot(new_data.index, new_data['Belgium'], label='Belgium')
		plt.title("Évolution de la population en France et en Belgique")
		plt.xlabel("Année") # Légende pour l'axe des X
		plt.ylabel("Population (en millions)") # Légende pour l'axe des Y
		
		plt.savefig('population_plot.png')

	else:
		print("Failed to load data.")

if __name__ == "__main__":
	main()