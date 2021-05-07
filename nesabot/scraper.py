'''
Actual code to visit, login and retrive the current grades.
'''

import logging
from log import setup_logger
logger = setup_logger()

import requests, json, os, dotenv
from bs4 import BeautifulSoup

FILENAME = './nesabot_grades.json'

# Constans from env variables
dotenv.load_dotenv('.env.local')
NESA_URL = os.environ['NESA_URL']
IFTT_URL = os.environ['IFTT_URL']
NESA_USERNAME = os.environ['NESA_USERNAME']
NESA_PASSWORD = os.environ['NESA_PASSWORD']

def read_json():
    try:
        with open(FILENAME, 'r') as f:
            txt = f.read()
            if txt == '':
                return []
            return json.loads(txt)
    except FileNotFoundError:
        return json.loads('[]')

def write_json(j: str):
    with open(FILENAME, 'w+') as f:
        if j != None: json.dump(j, f)

# Fetch new grades and compare them to 
# the cached ones. Send a new notification if there
# was a change.
def fetch() -> bool:
    # Try to load 'cached' json if avaible
    cached_json = read_json()
    # Fetch new grades 
    new_json = extract_grades(login(NESA_USERNAME, NESA_PASSWORD))
    # Write to cache for future reference
    write_json(new_json)
    # Compare with old one and send a notification
    # if they aren't similair
    if len(cached_json) != len(new_json):
        new_entries = []
        for c in new_json:
            if c not in cached_json:
                new_entries.append(c)
        return notif(new_entries)
    return True

# Send a post request to the iftt endpoint
# and check if it was successful.
def notif(new) -> bool:
    for grade in new: 
        payload = {
            'value1': grade['name'],
            'value2': grade['grade'],
            'value3': grade['subject'],
        }
        resp = requests.post(
            IFTT_URL,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(payload)
        )
        logger.log(msg='[+] Sent notification!', level=logging.INFO)
        if resp.status_code in [400, 404]:
            return False
    return True

# Log into the site and return the a soup of the landing page
def login(uname: str, passwd: str) -> BeautifulSoup:
    with requests.Session() as session:
        soup = BeautifulSoup(session.get(NESA_URL).text, features = 'html.parser')
        # Find post url + dynamic loginhash
        loginhash = soup.find('input', attrs = {'name': 'loginhash'})['value']
        action = soup.find('form', attrs = {'method': 'post'})['action']
        post = '{}/{}'.format(NESA_URL, action)
        payload = {
            'login': uname, 
            'passwort': passwd,
            'loginhash': loginhash
        }
        p = session.post(post, data = payload)
        return BeautifulSoup(p.text, features = 'html.parser')

# Extract grades from landing page
# Grades are stored in tr.td elements
def extract_grades(soup: BeautifulSoup):
    grades = []
    for tr in soup.select('tr.mdl-table--row-dense')[8:]:
        c = list(filter(lambda x: x != '\n', tr.contents))
        subject, name, date, grade = (c[0].string, c[1].string, c[2].string, c[3].string)
        subject = subject[0:2] if subject[1] != '-' else subject[0]
        grades.append({
            'name': name,
            'date': date,
            'grade': grade,
            'subject': subject,
        })
    return grades
