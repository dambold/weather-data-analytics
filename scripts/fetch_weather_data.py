import requests
import pandas as pd

# NOAA API token
API_TOKEN = "ViJNhQgbWQtfvdEYLJoxMrWcFPYXiBMp"  # Replace with your actual API key

# API endpoint and headers
url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
headers = {"token": API_TOKEN}

# Request parameters
params = {
    "datasetid": "GHCND",          # Dataset: Global Historical Climatology Network Daily
    "locationid": "FIPS:40",       # Location: FIPS code for Oklahoma
    "startdate": "2020-01-01",     # Start date for data
    "enddate": "2020-12-31",       # End date for data
    "datatypeid": "TMAX",          # Data type: Maximum temperature
    "limit": 1000                  # Maximum number of records to retrieve
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check for success
if response.status_code == 200:
    # Convert JSON response to a pandas DataFrame
    data = response.json()["results"]
    df = pd.DataFrame(data)
    print(df.head())
else:
    # Print error message if the request fails
    print(f"Error: {response.status_code}, {response.text}")
