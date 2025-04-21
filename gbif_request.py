import requests
import pandas as pd

def get_gbif_species_data(species_name, country_code="UY"):
    """
    Fetch species data from GBIF for a given species and country.

    :param species_name: Scientific name of the species (e.g., "Puma concolor").
    :param country_code: ISO 3166-1 alpha-2 country code (default is "UY" for Uruguay).
    :return: JSON response with species data.
    """
    base_url = "https://api.gbif.org/v1/occurrence/search"
    params = {
        "scientificName": species_name,
        "country": country_code,
        "limit": 10  # Limit the number of results
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

def print_data_as_dataframe(data):
    """
    Convert GBIF species data to a pandas DataFrame and print it.

    :param data: JSON response with species data.
    """
    if "results" in data:
        df = pd.DataFrame(data["results"])
        print(df)
    else:
        print("No results found in the data.")

# Example usage
if __name__ == "__main__":
    species = "Puma concolor"  # Replace with the desired species name
    try:
        data = get_gbif_species_data(species)
        print_data_as_dataframe(data)
    except Exception as e:
        print(f"Error: {e}")