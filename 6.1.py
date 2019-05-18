Slovar = {"city": "Москва", "temperature": 20}
print(Slovar['city'])
Slovar["temperature"] = Slovar["temperature"] - 5
print(Slovar)
print(Slovar.get("contry"))
Slovar.get("country", "Россия")
Slovar["date"] = '27.05.2019'
print(len(Slovar))
