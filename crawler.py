import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    file = open('data.txt', 'a')

    link = r"https://en.wikipedia.org/wiki/List_of_astronauts_by_name"
    web = requests.get(link)
    soup = BeautifulSoup(web.text, "html.parser")

    ul = soup.select('.mw-parser-output > ul')
    for item in ul:
        li = item.select('li')
        for it in li:
            a = it.select('a')
            for a_item in a:
                if a_item.find('img'): continue # ignore those national flags
                else: 
                    personal_link = r'https://en.wikipedia.org' + a_item['href']
                    personal_web = requests.get(personal_link)
                    personal_soup = BeautifulSoup(personal_web.text, 'html.parser')
                    
                    try:
                        age = personal_soup.select_one('.noprint.ForceAgeToShow')
                        name_and_age = a_item.text + ' ' + age.text.split()[1][:-1]
                        print(name_and_age)
                        file.write(name_and_age + '\n')
                    except AttributeError:
                        pass
                    finally:
                        break

    file.close()