weather = {"city": "Moscow","temperature": 20}
print(weather["city"])
weather["temperature"] = weather["temperature"] - 5
print(weather)
print(weather.get("сountry"))
print(weather.get("сountry" , "Россия"))
