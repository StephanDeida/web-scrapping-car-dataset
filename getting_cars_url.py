import requests
from bs4 import BeautifulSoup
index = 1
main_url = f"https://autos.mercadolibre.com.mx/autos_Desde_{index}_NoIndex_True"
cars_url = []

for i in range(42):
    print(f"{i}step")
    index = i * 48 + 1
    response =  requests.get(main_url)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.find_all(class_="ui-search-layout__item")
    for result in search_results:
        url = result.find("a")["href"]
        cars_url.append(url)


# Open a file for writing
with open("cars_url.txt", "w", encoding='utf-8') as f:
    # Write each item in the list to a new line in the file
    for item in cars_url:
        f.write("%s\n" % item)
#print(len(cars_url))