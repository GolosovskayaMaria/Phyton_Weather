import urllib.parse
import requests

def print_weather(latitude, lontitude):
    params = {"lat": f'{latitude}', "lon": f'{lontitude}', "appid": "2d82ff0ac22e044c3e70a3f36f4a162c"}
    result = urllib.parse.urlencode(params)
    link = "http://api.openweathermap.org/data/2.5/weather?" + result
    response = requests.get(link)
    return response.json()

print("\n")

town = input("Введите город: ") or "Gatchina"
print(town, "\n")

country = input("Введите инициалы страны: ") or "RU"
print(country, "\n")

params = {"q": f'{town},{country}', "appid": "2d82ff0ac22e044c3e70a3f36f4a162c"}
result = urllib.parse.urlencode(params)

link = "http://api.openweathermap.org/geo/1.0/direct?" + result
response = requests.get(link)
print("Запрос", link)

results = response.json()

print("Ответ", results)

print("По названию", town, "найдено", len(results), "городов", sep=" ")

for town_weather in results:
    print("1:", town_weather['name'])
    w = print_weather(town_weather['lat'], town_weather['lon'])
    print("2:", w['weather'])
    print("3:", results)
