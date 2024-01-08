from playwright.sync_api import Playwright, TimeoutError
from bs4 import BeautifulSoup
from datetime import datetime
import re


# I HAVE BEEN BLOCKED 7/1/2024. Add a delay...

def extract_cat_code(playwright: Playwright, catastral_code_list):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.sedecatastro.gob.es/Accesos/SECAccDNI.aspx?Dest=3&ejercicio=2024")
    page.click("[placeholder=\"\\39 9999999R\"]")
    page.fill("[placeholder=\"\\39 9999999R\"]", "43554142P") # change to a manual input, from XLSX file or system secret keys
    page.click("[placeholder=\"AAA0000000\\/E00000000\"]")
    page.fill("[placeholder=\"AAA0000000\\/E00000000\"]", "CCF194291") # change to a manual input, from XLSX file or system secret keys
    with page.expect_navigation():
        page.click("button:has-text(\"Validar DNI / Soporte\")")

        pattern = re.compile(r"^\d{10,12}[A-Z]{2}$")
        value_list = []
        for catastral_code in catastral_code_list:
            if not pattern.match(catastral_code):
                print(f"Invalid catastral code: {catastral_code}. Skipping.")
                value_list.append("Error")
                continue
            try:

                page.goto("https://www.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx?VR=SI&ejercicio=2024&Titu=43554142P")
                page.select_option("select[name=\"ctl00\\$Contenido\\$ddlFinalidad\"]", "1")
                page.click("input[name=\"ctl00\\$Contenido\\$txtFechaConsulta\"]")
                today = datetime.now()
                day = today.day
                # Click current day
                page.click(f"a:has-text(\"{day}\")", timeout=5000)
                page.click("input[name=\"ctl00\\$Contenido\\$txtRC2\"]")
                page.fill("input[name=\"ctl00\\$Contenido\\$txtRC2\"]", catastral_code)
                page.click("text=VALOR DE REFERENCIA", timeout=5000)
                raw_html = page.inner_html('#ctl00_Contenido_tblInmueble', timeout=5000)
                soup = BeautifulSoup(raw_html, 'html.parser')
                reference_value_element = soup.find("span", string="Valor de Referencia")
                if reference_value_element:
                    reference_value = reference_value_element.find_next("label").text
                    value_list.append(reference_value)
                    print(f"Valor catastral de referencia de {catastral_code} es:", reference_value)

                else:
                    print(f"Valor catastral de referencia de {catastral_code} no se pudo encontrar.")
            except TimeoutError:
                reference_value = "Error"
                value_list.append(reference_value)
                print(f"Valor catastral de referencia de {catastral_code} es:", reference_value)
                continue

    context.close()
    browser.close()
