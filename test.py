import requests
from bs4 import BeautifulSoup


url_to_json_file = 'https://www.idealista.com/maps/api/v1/cadastre/080190485204DF3808E0007WG/valuation'

with open('cookie.txt', 'r') as file:
    cookie_content = file.read().strip()
print(cookie_content)
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Authorization': 'Bearer ZaUU2qE2DWszePaoFb4c/RORYg1z4n4GbNqKodr+ERpFvj8cAhaSoTofjpazI76t8B3Gpyxugd7LzRzlojm41eRI2DJDe+ZMZ0QzKsPORh+9HvWYMeIiJU8+bsB7c/gA/sXqnuhWSxw=',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.idealista.com/maps/barcelona-barcelona/calle-federico-garcia-lorca/18/0485204DF3808E0007WG/',
    'Cookie': cookie_content,
}
response = requests.get(url_to_json_file, headers=headers2)
raw = response.raw
print(response.text)
print(response.content)

if response.status_code == 200:
    json_data = response.json()

else:
    print(f"Error: Unable to retrieve data. Status code: {response.status_code}")

