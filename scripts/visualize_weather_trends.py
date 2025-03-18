import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_and_visualize_weather(api_token, location_id, start_date, end_date):
    # Fetch data from NOAA API
    url = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"
    headers = {"token": api_token}
    params = {
        "datasetid": "GHCND",
        "locationid": location_id,
        "startdate": start_date,
        "enddate": end_date,
        "datatypeid": "TMAX",
        "limit": 1000,
    }
    response = requests.get(url, headers=headers, params=params)

    # Handle API response
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return

    data = response.json()
    df = pd.DataFrame(data["results"])
    df["date"] = pd.to_datetime(df["date"])

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df["date"], df["value"], label="Max Temperature (°F)", color="blue")
    plt.title("Trended Weather Events in Oklahoma")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°F)")
    plt.legend()
    plt.grid()
    plt.show()

# Main function
if __name__ == "__main__":
    API_TOKEN = "your_api_token_here"  # Replace with your NOAA API token
    LOCATION_ID = "FIPS:40"  # FIPS code for Oklahoma
    START_DATE = "2020-01-01"
    END_DATE = "2020-12-31"
    
    fetch_and_visualize_weather(API_TOKEN, LOCATION_ID, START_DATE, END_DATE)
