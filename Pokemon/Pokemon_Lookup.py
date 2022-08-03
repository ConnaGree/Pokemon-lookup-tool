import requests

while True:	
	pokemon = input("Which pokemon do you want to find?")
	pokemon = pokemon.lower()

	url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

	req = requests.get(url)

	if req.status__code == 200:
		data = req.json()

		print(f"Name is: '{data['name']}")
		print("Ability:")
		for ability in data['abilities']:
			print(ability['ability']['name'])
	else: 
		print("Pokemon not found")

