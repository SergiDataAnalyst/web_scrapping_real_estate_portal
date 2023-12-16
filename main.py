import requests
import streamlit as st
from reportlab.pdfgen import canvas


street_input = st.text_input('Introduce el nombre de la calle', placeholder='Ej: Jose Sangenis')
street = str(street_input.replace(" ", "-"))
print(street)

number_input = str(st.text_input("Introduce el número de la calle", placeholder='Ej: 49'))

search_button = st.button("Buscar info")
if search_button:
    url_to_json_file = f'https://www.idealista.com/maps/api/v1/barcelona-barcelona/calle-{street}/{number_input}'
    print(url_to_json_file)
    #  build rotating User Agents
    #  build rotating proxies
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.idealista.com/maps/barcelona-barcelona/calle-' + street + '/' + number_input + '/',
    }
    response = requests.get(url_to_json_file, headers=headers2)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        json_data = response.json()
        print(json_data)

        parcels = json_data.get('parcels', [])
        if not isinstance(parcels, list):
            raise ValueError("The 'parcels' field is not a list in the response.")

        parts = url_to_json_file.split('/')
        city = parts[6]
        street = parts[7]
        house_number = parts[8]

        formatted_string = f'{city}_{street.replace("-", "_")}_{house_number}'

        pdf_filename = 'propiedades-calle-' + street + number_input + '.pdf'
        c = canvas.Canvas(pdf_filename)

        y_coordinate = 750

        for parcel in parcels:
            for property_info in parcel.get('properties', []):
                if y_coordinate < 50:  # Start a new page if there is not enough space

                    c.showPage()
                    y_coordinate = 750

                property_id = property_info.get('id', '')
                property_name = property_info.get('name', '')
                property_area = property_info.get('area', '')
                is_residential = property_info.get('is_residential', '')
                is_country_house = property_info.get('is_country_house', '')
                property_reference = property_info.get('reference', '')
                reference_real = property_info.get('reference_real', '')
                quality = property_info.get('quality', '')
                reform_year = property_info.get('reform_year', '')
                constructed_year = property_info.get('constructed_year', '')
                energy_certificate = property_info.get('energy_certificate', '')
                room_number = property_info.get('room_number', '')
                bathroom_number = property_info.get('bathroom_number', '')
                coefficient = property_info.get('coefficient', '')

                # Writing all the info for each parcel on the PDF file
                c.drawString(100, y_coordinate, f"ID de Propiedad: {property_id}")
                c.drawString(100, y_coordinate - 15, f"Nombre de Propiedad: {property_name}")
                c.drawString(100, y_coordinate - 30, f"Área de Propiedad: {property_area}")
                c.drawString(100, y_coordinate - 45, f"Es Residencial: {is_residential}")
                c.drawString(100, y_coordinate - 60, f"Es Casa de Campo: {is_country_house}")
                c.drawString(100, y_coordinate - 75, f"Referencia Catastral: {property_reference}")
                c.drawString(100, y_coordinate - 90, f"Referencia Catastral Real: {reference_real}")
                c.drawString(100, y_coordinate - 105, f"Calidad: {quality}")
                c.drawString(100, y_coordinate - 120, f"Año de Reforma: {reform_year}")
                c.drawString(100, y_coordinate - 135, f"Año de Construcción: {constructed_year}")
                c.drawString(100, y_coordinate - 150, f"Certificado Energético: {energy_certificate}")
                c.drawString(100, y_coordinate - 165, f"Número de Habitaciones: {room_number}")
                c.drawString(100, y_coordinate - 180, f"Número de Baños: {bathroom_number}")
                c.drawString(100, y_coordinate - 195, f"Coeficiente: {coefficient}")
                c.drawString(100, y_coordinate - 210, "-" * 20)
                y_coordinate = y_coordinate - 240

        c.save()

    elif response.status_code == 403:
        print(f"Correct request but unwilling to send response, possibly too many requests: {response.status_code}")

    elif response.status_code == 404:
        st.write(f"Please, double check the street name is written correctly or that the street number "
                 f"exists. ")

        st.markdown(f"[LINK](https://www.idealista.com/maps/barcelona-barcelona/calle-{street})")

        # https://www.idealista.com/maps/provincia-municipio/calle-josep-sangenis/
        # el municipio en cataluña esta con el nombre en catalán, en el país vasco parece que está en español

    else:
        print(f"Error: Unable to retrieve data. Status code: {response.status_code}")

