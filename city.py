import argparse
import requests
from prettytable import PrettyTable
from colorama import Fore


class YahooService:
    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        url = f"https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20 \
                where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city} \
                %22)%20and%20u%3D%22c%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        print("Sending HTTP requests...")
        yahoo_answer = requests.get(url, city).json()
        data_forecast = yahoo_answer["query"]["results"]["channel"]["item"]["forecast"]

        data = []
        for each_day in data_forecast:
            data.append({
                "date": each_day["date"],
                "day": each_day["day"],
                "high": each_day["high"],
                "low": each_day["low"],
                "text": each_day["text"],
            })

        return data


class CityInfo:
    def __init__(self, city, forecast=None):
        self.city = city
        self._forecast = forecast or YahooService()

    def city_forecast(self):
        return self._forecast.get(self.city)


def _main():
    print("Forecast for {}".format(args.city))
    forecast = YahooService()
    city_info = CityInfo(args.city, forecast)
    forecast_data = city_info.city_forecast()

    pt = PrettyTable()
    pt.field_names = ["Date", "Day", Fore.RED + "Max" + Fore.RESET, Fore.BLUE + "Min" + Fore.RESET, "Text"]

    for day_data in forecast_data:
        pt.add_row([day_data["date"], day_data["day"], Fore.RED + day_data["high"] + Fore.RESET,
                    Fore.BLUE + day_data["low"] + Fore.RESET, day_data["text"]])

    print(pt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", type=str, help="City name")
    args = parser.parse_args()
    _main()
