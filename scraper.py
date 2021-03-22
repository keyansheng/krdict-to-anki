import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = "https://krdict.korean.go.kr/dicSearch/search?mainSearchWord={}"


def generate_definition(query):
    r = requests.get(URL_TEMPLATE.format(query))
    soup = BeautifulSoup(r.content, "html.parser")
    entries = soup.find_all("dl", class_="printArea")
    results = []
    for entry in entries:
        word = entry.find("span", class_="word_type1_17").text
        definition = entry.find("dd").text
        results.append(" ".join(f"{word} = {definition}".split()))
    return "<br>".join(results)
