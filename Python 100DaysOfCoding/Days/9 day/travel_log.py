travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#print(travel_log[0]["country"])
def add_new_country(name,visits,cities = []):
	travel_log.append({})
	travel_log[len(travel_log) - 1] = travel_log[0]
	for key in travel_log[0]:
		travel_log[2]["country"] = name
		travel_log[2]["visits"] = visits
		travel_log[2]["cities"] = cities

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)