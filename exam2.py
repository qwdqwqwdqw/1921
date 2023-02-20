from bs4 import BeautifulSoup
import requests
def Start():
    print(">1")
    print(">2")
    print(">3")
    a = int(input())
    if a == 1:
        print("Paste website link you want to pars")
        b = int(input())
        response = requests.get(b)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup_list = soup.find_all("a", {"href": "/ua/statistic/macro-indicators#1"})
            for elem in soup_list:
                print(elem.text)
    if a == 2:
        print("Nothing added yet")
    if a == 3:
        print("Nothing added yet")
    else:
        print("Theres no function called: ", a)
