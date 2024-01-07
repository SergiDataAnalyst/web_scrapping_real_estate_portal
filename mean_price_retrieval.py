import requests
import json
import selenium
import seleniumbase
import re




url = f"https://www.idealista.com/ajax/listingcontroller/listingajax.ajax?locationUri=barcelona/nou-barris/vilapicina-i-la-torre-llobeta&typology=1&operation=1&freeText=&adfilter_pricemin=default&adfilter_price=default&adfilter_area=default&adfilter_areamax=default&adfilter_rooms_0=&adfilter_rooms_1=&adfilter_rooms_2=2&adfilter_rooms_3=&adfilter_rooms_4_more=&adfilter_baths_1=1&adfilter_baths_2=&adfilter_baths_3=&adfilter_newconstruction=&adfilter_goodcondition=&adfilter_toberestored=&adfilter_hasairconditioning=&adfilter_wardrobes=&adfilter_lift=1&adfilter_flatlocation=&adfilter_parkingspace=&adfilter_garden=&adfilter_swimmingpool=&adfilter_hasterrace=&adfilter_boxroom=&adfilter_accessibleHousing=&adfilter_top_floor=&adfilter_intermediate_floor=&adfilter_ground_floor=&adfilter_hasplan=&adfilter_digitalvisit=&adfilter_agencyisabank=&adfilter_published=default&ordenado-por=&adfilter_onlyflats=&adfilter_penthouse=&adfilter_duplex=&adfilter_homes=&adfilter_independent=&adfilter_semidetached=&adfilter_terraced=&adfilter_countryhouses=&adfilter_chalets=&device=mobile"


def mean_price_retrieval(location, district, neighborhood, typology, number_of_rooms, number_of_bathrooms):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.idealista.com/maps/barcelona-barcelona/calle-federico-garcia-lorca/18/0485204DF3808E0003ZA/',
    }

    # (2,2,2,1,3,1) Example
    url = f"https://www.idealista.com/ajax/listingcontroller/listingajax.ajax?locationUri=barcelona/nou-barris/vilapicina-i-la-torre-llobeta&typology={typology}&operation=1&freeText=&adfilter_pricemin=default&adfilter_price=default&adfilter_area=default&adfilter_areamax=default&adfilter_rooms_{number_of_rooms}={number_of_rooms}&adfilter_baths_{number_of_bathrooms}={number_of_bathrooms}&device=mobile"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        json_data = str(json_data)
        print(json_data)

        pattern = r"Precio medio ([\d,.]+) eur/m²"

        # Search for the pattern in the JSON string
        match = re.search(pattern, json_data)

        # Extract the desired string
        if match:
            extracted_string = match.group(1)
            print(extracted_string)
        else:
            print("Pattern not found in the JSON data.")

    else:
        print(f"Error: Unable to retrieve data. Status code: {response.status_code}")


if __name__ == '__main__':
    # (2,2,2,1,3,1) Example
    mean_price_retrieval(3, 3, 3, 1, 3, 1)

