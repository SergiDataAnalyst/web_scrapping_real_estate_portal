import requests
import json
import re



# PRECIO MEDIO URL EXTRAIDA DE 

url_to_json = 'https://www.idealista.com/ajax/listingcontroller/listingajax.ajax?locationUri=barcelona%2Fnou-barris%2Fcanyelles&typology=1&operation=1&freeText=&adfilter_pricemin=default&adfilter_price=default&adfilter_area=60&adfilter_areamax=120&adfilter_rooms_0=&adfilter_rooms_1=&adfilter_rooms_2=&adfilter_rooms_3=3&adfilter_rooms_4_more=4&adfilter_baths_1=&adfilter_baths_2=&adfilter_baths_3=&adfilter_newconstruction=&adfilter_goodcondition=&adfilter_toberestored=&adfilter_hasairconditioning=&adfilter_wardrobes=&adfilter_lift=&adfilter_flatlocation=&adfilter_parkingspace=&adfilter_garden=&adfilter_swimmingpool=&adfilter_hasterrace=&adfilter_boxroom=&adfilter_accessibleHousing=&adfilter_top_floor=&adfilter_intermediate_floor=&adfilter_ground_floor=&adfilter_hasplan=&adfilter_digitalvisit=&adfilter_agencyisabank=&adfilter_published=default&ordenado-por=&adfilter_onlyflats=&adfilter_penthouse=&adfilter_duplex=&adfilter_homes=&adfilter_independent=&adfilter_semidetached=&adfilter_terraced=&adfilter_countryhouses=&adfilter_chalets=&device=mobile'

headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.idealista.com/maps/barcelona-barcelona/calle-federico-garcia-lorca/18/0485204DF3808E0003ZA/',
}
response = requests.get(url_to_json, headers=headers2)

if response.status_code == 200:
    json_data = response.json()
    json_data = str(json_data)

    pattern = re.compile(r'Precio medio (\d+\.\d+ eur/m²)')

    # Search for the pattern in the JSON string
    match = pattern.search(json_data)

    # Extract the desired string
    if match:
        extracted_string = match.group(1)
        print(extracted_string)
    else:
        print("Pattern not found in the JSON data.")

else:
    print(f"Error: Unable to retrieve data. Status code: {response.status_code}")