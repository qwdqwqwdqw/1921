import sqlite3
from bs4 import BeautifulSoup
import requests

connection = sqlite3.connect("urok10.sl3", 5)
cur = connection.cursor()

response = requests.get("https://https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D1%81%D1%8B/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list1 = soup.find_all("p", {"class": "//sinoptik.ua/погода-черкассы/2022-11-18"})

for elem in soup_list1:
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
