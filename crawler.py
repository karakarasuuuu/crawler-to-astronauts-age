import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    keyword = input("Enter your keyword: ")
    
    # a class="labs-docsum-title" 
    # div class="labs-docsum-citation full-citation"
    # div class="labs-docsum-snippet"
    link = "https://pubmed.ncbi.nlm.nih.gov/?term=" + keyword
    web = requests.get(link)
    soup = BeautifulSoup(web.text, "html.parser")
    title = soup.select("a.labs-docsum-title")
    author = soup.select("div.labs-docsum-citation full-citation")
    snippet = soup.select("div.labs-docsum-snippet")
    for t in title:
        print(t.text.strip())