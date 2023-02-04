import requests
from bs4 import BeautifulSoup
from src.constants.complex_types import DICT_OF_STR


from src.models.models import set_on_call_pharmacy

def web_scrap(url_dict:DICT_OF_STR) -> None:
    for name, url in url_dict.items():
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.find_all("a")
        links = [link.text.strip() for link in links]
        links_imp = set()
        for link in links:
            if "pharmacie" in link.lower() and "garde" not in link.lower() and not "pharmacies" == link.lower():
                links_imp.add(link)

        set_on_call_pharmacy(name, list(links_imp))