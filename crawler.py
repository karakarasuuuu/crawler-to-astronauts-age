import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    keyword = input("Enter your keyword: ")
    
    link = "https://pubmed.ncbi.nlm.nih.gov/?term=" + keyword
    web = requests.get(link)

    soup = BeautifulSoup(web.text, "html.parser")
    title = soup.select("a.labs-docsum-title")
    author = soup.select("span.labs-docsum-authors")
    snippet = soup.select("div.full-view-snippet")

    for t, a, s in zip(title, author, snippet):
        print(t.text.strip(), a.text.strip(), s.text.strip(), sep='\n', end='\n\n')