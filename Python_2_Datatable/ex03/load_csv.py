import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("The file path must be a string.")
        if not path:
            raise ValueError("The file path cannot be empty.")
        if not path.endswith('.csv'):
            raise ValueError(
                "The provided file path does not point to a CSV file.")
        if len(path) == 0:
            raise ValueError("The file path cannot be an empty string.")
        data = pd.read_csv(path)
        print('Loading dataset of dimensions:', data.shape)
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
