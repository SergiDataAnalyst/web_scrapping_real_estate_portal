import json
from reportlab.pdfgen import canvas


json_file = '38.json'

with open(json_file, 'r') as file:
    data = json.load(file)

parcels = data.get('parcels', [])
if not isinstance(parcels, list):
    raise ValueError(" The 'parcels' field is not a list in the response.")

pdf_filename = 'propiedades_calle_garcia_lorca_38_Barcelona.pdf'
c = canvas.Canvas(pdf_filename)

y_coordinate = 750

for parcel in parcels:
    for property_info in parcel.get('properties', []):
        if y_coordinate < 50:
            # Start a new page if there is not enough space
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

        # Process the extracted information as needed (e.g., print or store it)
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


