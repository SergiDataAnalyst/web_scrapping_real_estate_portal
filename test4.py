from sede_catastro import extract_cat_code
from playwright.sync_api import sync_playwright
import pandas as pd


# note, convert to main,

file_path = 'muestra_csv.csv'
df = pd.read_csv(file_path)
if 'REFERENCIA CATASTRAL' in df.columns:
    # Extract elements from the 'REFERENCIA CATASTRAL' column and convert to a list
    catastral_code_list = df['REFERENCIA CATASTRAL'].tolist()
else:
    catastral_code_list = []
    print("Column 'REFERENCIA CATASTRAL' not found in the CSV file.")

print(df.head(10))


if __name__ == "__main__":
    with sync_playwright() as playwright:
        extract_cat_code(playwright, catastral_code_list)

    if len(catastral_code_list) == len(df):

        df['valor ref. catastral'] = catastral_code_list
    else:
        print("The length of referencia_catastral_list does not match the number of rows in the DataFrame.")

    df.to_csv('nuevo_csv.csv', index=False)
