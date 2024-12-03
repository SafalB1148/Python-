#creating a dictionary
country_capitals={
    "Germany":"Berlin",
    "canada":"otawa",
    "England":"London",
    "Italy":"Naples"
}
#printing the dictionary
print(country_capitals)
print(country_capitals["Germany"])
print(country_capitals["canada"])
country_capitals["America"]="Washington DC"
print(country_capitals)
del country_capitals["canada"]
print(country_capitals)
country_capitals["Italy"]="Rome"
print(country_capitals)
#Printing  dictionary keys one by one
for country in country_capitals:
    print(country)
print()
#printing dictionary values one by one
for country in country_capitals:
    capital=country_capitals[country]
    print(capital)
print()
print(country_capitals.keys())
print(country_capitals.values())

morecountry_capitals={
    "Azerbaizan":"Baku",
    "Japan":"Tokyo"
}
country_capitals.update(morecountry_capitals)
print(morecountry_capitals)
print(country_capitals)
print(country_capitals.get("Italy"))
print(country_capitals.get("America"))



