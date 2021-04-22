import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"

def search_city(query):
    '''Look for a given city and disambiguate between several candidates'''
    url = urllib.parse.urljoin(BASE_URI, "/api/location/search")
    cities = requests.get(url, params={'query': query}).json()
    if not cities:
        print(f"Sorry, Metaweather does not know about {query}...")
        return None
    if len(cities) == 1:
        return cities[0]
    for i, city in enumerate(cities):
        print(f"{i + 1}. {city['title']}")
    index = int(input("Oops, which one did you mean?")) - 1
    return cities[index]


def weather_forecast(woeid):
    '''Returns a 5-element list weather forecast for a given woeid'''
    url = urllib.parse.urljoin(BASE_URI, f"/api/location/{woeid}")
    return requests.get(url).json()['consolidated_weather']

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    if city:
        daily_forecasts = weather_forecast(city['woeid'])
        for forecast in daily_forecasts:
            max_temp = round(forecast['max_temp'])
            print(f"{forecast['applicable_date']}: {forecast['weather_state_name']} ({max_temp}°C)")


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
