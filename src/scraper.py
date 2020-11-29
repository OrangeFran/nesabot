'''
Actual code to visit, login and retrive the current grades.
'''

import requests, json
from bs4 import BeautifulSoup
from const import URL
from creds import UNAME, PASSWD, MY_CHAT_ID

filename = "/nesabot/cache/grades.json"

def read_json():
    with open(filename, "r") as f:
        txt = f.read()
        if txt == "":
            return []
        return json.loads(txt)

def write_json(j: str):
    with open(filename, "w") as f:
        if j != None: json.dump(j, f)

def fmt(json, new: bool) -> str:
    output = "New grades ... 😄\n" if new else ""
    for g in json:
        output += "{} ({}) at {}: \t{}\n".format(g["name"], g["subject"], g["date"], g["grade"])
    return output if output != "" else "Nothing"

# Data will be stored as json
def fetch(cached: bool, bot = None):
    # Try to load "cached" json if avaible
    cached_json = read_json()
    if cached:
        return fmt(cached_json, new = False)
    # Fetch new grades (if avaible) and write to cache for future ref
    new_json = extract_grades(login(UNAME, PASSWD))
    write_json(new_json)
    # Compare with old one
    if len(cached_json) != len(new_json):
        new_entries = []
        for c in new_json:
            if c not in cached_json:
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
        subject, name, date, grade = (c[0].string, c[1].string, c[2].string, c[3].string)
        subject = subject[0:2] if subject[1] != "-" else subject[0]
        grades.append({
            "name": name,
            "date": date,
            "grade": grade,
            "subject": subject,
        })
    return grades

if __name__ == "__main__":
    print(extract_grades(login(UNAME, PASSWD)))
