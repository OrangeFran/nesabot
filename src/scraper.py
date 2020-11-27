'''
Actual code to visit, login and retrive the current grades.
'''

import requests, json
from bs4 import BeautifulSoup
from const import URL
from creds import UNAME, PASSWD, MY_CHAT_ID

filename = "/var/www/nesabot/cache/grades.json"

def read_json():
    with open(filename, "r") as f:
        return json.loads(f.read())

def write_json(j: str):
    with open(filename, "w") as f:
        json.dump(j, f)

def fmt(json, new: bool) -> str:
    output = "New grades ... 😄\n" if new else ""
    for g in json:
        output += "{} at {}: \t{}\n".format(g["name"], g["date"], g["grade"])
    return output

# Data will be stored as json
def fetch(cached: bool, bot = None):
    # Try to load "cached" json if avaible
    cached_json = read_json()
    if cached:
        return fmt(cached_json, new = False)
    # Fetch new grades (if avaible) and write to cache for future ref
    j = extract_grades(login(UNAME, PASSWD))
    write_json(j)
    if len(cached_json) == 0:
        # Compare with old one
        if cached_json != j:
            new_entries = []
            for c in j:
                try:
                    if c == cached_json[0]:
                        break
                except:
                    pass
                new_entries.append(c)
            if bot != None:
                bot.send_message(
                    chat_id = MY_CHAT_ID,
                    text = fmt(new_entries, new = True)
                )
            return fmt(new_entries, new = True)
    return fmt(j, new = False)

# Log into the site and return the a soup of the landing page
def login(uname: str, passwd: str) -> BeautifulSoup:
    with requests.Session() as session:
        soup = BeautifulSoup(session.get(URL).text, features = "html.parser")
        # Find post url + dynamic loginhash
        loginhash = soup.find("input", attrs = {"name": "loginhash"})["value"]
        action = soup.find("form", attrs = {"method": "post"})["action"]

        post = "{}/{}".format(URL, action)
        payload = {
            'login': uname, 
            'passwort': passwd,
            'loginhash': loginhash
        }
        p = session.post(post, data = payload)
        return BeautifulSoup(p.text, features = "html.parser")

# Extract grades from landing page
# Grades are stored in tr.td elements
def extract_grades(soup: BeautifulSoup):
    grades = []
    for tr in soup.select("tr.mdl-table--row-dense")[8:]:
        c = list(filter(lambda x: x != "\n", tr.contents))
        name, date, grade = (c[0].string, c[2].string, c[3].string)
        grades.append({
            "name": name[0:8],
            "date": date,
            "grade": grade
        })
    return grades

if __name__ == "__main__":
    print(extract_grades(login(UNAME, PASSWD)))
