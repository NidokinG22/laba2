import requests

city = "Moscow,RU"
appid = "06560d1c133295bb1aa8efbbc019b2a5"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={"q": city, "units": "metric", "lang": "ru", "APPID": appid})
data = res.json()
print(data)

print("Город:", city)
print("Погодные условия:", data["weather"][0]["description"])
print("Температура:", data["main"]["temp"])
print("Минимальная температура:", data["main"]["temp_min"])
print("Максимальная температура", data["main"]["temp_max"])
print("Скорость ветра", data["wind"]["speed"])
print("Видимиость", data["visibility"])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={"q": city, "units": "metric", "lang": "ru", "APPID": appid})
data = res.json()

print(f"\nПрогноз погоды на неделю:")
for i in data["list"]:
    print(f"={i ['dt_txt']}")
    print(f"Температура ........ {i['main']['temp']:+.0f}")
    print(f"Погодные условия ... {i['weather'][0]['description']}")
    print(f"Скорость ветра ..... {i['wind']['speed']}")
    print(f"Видимость ..... {i['visibility']}")