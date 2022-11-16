import sqlite3
from bs4 import BeautifulSoup
import requests

connection = sqlite3.connect("urok10.sl3", 5)
cur = connection.cursor()

response = requests.get("https://bank.gov.ua/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/ua/statistic/macro-indicators#1"})
for elem in soup_list:
    text_1 = elem.text
# cur.execute(f"CREATE TABLE Maksim (Data);")
cur.execute(f"INSERT INTO Maksim (Data) VALUES ('{text_1}');")
connection.commit()
# cur.execute("UPDATE first_table SET name='Data' Where rowid=3;")
# connection.commit()
# cur.execute("UPDATE Maksim SET name='name' Where rowid=3;")
# connection.commit()
cur.execute("SELECT rowid, Data FROM Maksim;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()
