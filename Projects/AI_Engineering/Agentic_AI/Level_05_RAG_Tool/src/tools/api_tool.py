import requests
from langchain_core.tools import tool


@tool
def get_country_info(country: str) -> str:
    """Get information about a country using a public REST API."""

    url = f"https://api.restcountries.com/countries/v5/names.common/{country}"

    response = requests.get(
        url,
        headers={
            "Authorization": "Bearer rc_live_demo"
        }
    )

    data = response.json()

    country_data = data["data"]["objects"][0]

    name = country_data["names"]["common"]
    capital = country_data["capitals"][0]["name"]

    return f"Country: {name}, Capital: {capital}"