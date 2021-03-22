import sys
import requests
from bs4 import BeautifulSoup

URL_TEMPLATE = "https://krdict.korean.go.kr/dicSearch/search?mainSearchWord={}"


def generate_definition(query):
    r = requests.get(URL_TEMPLATE.format(query))
    soup = BeautifulSoup(r.content, "html.parser")
    entries = soup.find_all("dl", class_="printArea")
    results = []
    for entry in entries:
        word = " ".join(entry.find("span", class_="word_type1_17").text.split())
        definitions = entry.find_all("dd")
        result = word
        for definition in definitions:
            result = f"{result}<br>{''.join(definition.text.split())}"
        results.append(result)
    return "<br><br>".join(results)


if __name__ == "__main__":
    print(generate_definition(sys.argv[1]))
