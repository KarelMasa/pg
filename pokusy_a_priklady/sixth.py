import sys
import requests
from lxml import html


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    response = requests.get(url)
    if not response.ok:
        return []

#    print(response.connection)
    root = html.fromstring(response.content)
    
    return [href for href in root.xpath('//a/[@href]') if href.startwith('http:')]

    

if __name__ == "__main__":
    try:
        #url = sys.argv[1]
        url = "http://www.seznam.cz"
        download_url_and_get_all_hrefs(url)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
