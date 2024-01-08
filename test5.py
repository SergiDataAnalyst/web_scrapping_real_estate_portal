from bs4 import BeautifulSoup as bs
import random
import time
import requests
import ipaddress




HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "es-ES,es;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "dnt": "1",
    "referer": "https://www.idealista.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
}

def next_page_exists(soup):
    if not soup.find("main", {"class": "listing-items"}).find("div", {"class": "pagination"}):
        return False
    elif not soup.find("main", {"class": "listing-items"}).find("div", {"class": "pagination"}).find("li", {"class": "next"}):
        return False
    return True


def get_search_add_data(url, proxy):
    page = 1
    adds = []
    while True:
        time.sleep(random.randint(3, 10))
        page_url = url + f"/pagina-{page}.htm"
        #response = requests.get(page_url, headers = HEADERS, proxies = {"https": "http://{user}:{password}@{ip}:{port}".format(**proxy)})
        response = requests.get(page_url, headers=HEADERS)
        print("{status} - {url}".format(status=response.status_code, url=page_url))
        soup = bs(response.text, "html.parser")
        articles = soup.find("main", {"class", "listing-items"}).find_all("article")
        zero_results = soup.find("div", {"class": "zero-results-content"})
        if not articles or zero_results:
            return (adds)
        adds += [{
            "add_id": article["data-adid"],
            "price": article.find("span", {"class": "item-price h2-simulated"}).text,
            "info": article.find("div", {"class": "item-detail-char"}).text.replace("'", "''"),
            "location": article.find("a", {"class": "item-link"}).text.replace("'", "''")
        } for article in articles]
        if not next_page_exists(soup):
            return (adds)
        page += 1


if __name__ == "__main__":
    postal_code = '08035'
    a = get_search_add_data(f"https://www.idealista.com/buscar/venta-garajes/{postal_code}", "")
    print(a)