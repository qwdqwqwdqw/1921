# import urllib.request
# import requests
#
# # opener = urllib.request.build_opener()
# # response = opener.open ("https://httpbin.org/get")
# # print(response.read())
# response = requests.get("https://httpbin.org/get")
# # print(response.content)
# print(f"Datatype - {type(response.content)}")
# print(response.text)
# print(f"Datatype - {type(response.text)}")
#
# response = requests.post("https://httpbin.org/get",
#                         data = "NAZHA ZAPIS",
#                         headers = {"h1" : "NAZHA ZAPISKA"})
#
# print(response.text)

# import requests
#
# res_parse_list = []
#
# response = requests.get("https://coinmarketcap.com/")
# # print(response.text)
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#     if parse_elem_1.startswith("$"):
#         for parse_elem_2 in parse_elem_1.split("</span>"):
#             if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                 # print(parse_elem_2)
#                 res_parse_list.append(parse_elem_2)
# btc = res_parse_list[0]
# print(btc)

from bs4 import BeautifulSoup
import requests
response = requests.get("https://bank.gov.ua/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/ua/statistic/macro-indicators#1"})
for elem in soup_list:
    print(elem.text)
    # res = soup_list[0].find("span")
    # print(res.text)
