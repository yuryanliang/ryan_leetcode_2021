import logging


def get_class_roster(class_name):
    roster = {'id': '001',
              'class_description': 'math',
              'teacher': 'Smitch',
              'student': ['Bob', 'Ann', 'Tommy']

              }
    return roster
def etl(class_name):
    # extract data from source db
    MAX_TRIES = 3
    tries = 0
    resp = None
    while True:
        try:
            roster = get_class_roster(class_name)# requests.get(API_URL + '/items')
        except TimeoutError as err:
            print(err)
        if resp.status_code == 500 and tries < MAX_TRIES:
            tries += 1
            continue
        break
    # todo_items = resp.json()
    # for item in todo_items:


    # parse data
    # constrains:
    if not roster['id'].isnumeric(): # test class id
        return print('bad status: id is not int')
    id = roster['id']
    student_names = roster['student']
    for name in student_names:
        if len(name) > 63:
            logging.debug('student name is too long')
            student_names.remove(name)


    class_desc = roster['class_description'].strip()[:256]
    teacher = roster['teacher'].strip()[:256]

    # insert classes table
    placeholders = ', '.join(map(lambda x: '\"%s\"' % x, [id, class_desc, teacher][1:]))
    columns = ', '.join(list(roster.keys())[:3])
    sql = "BEGIN TRANSITION INSERT INTO classes (" + columns + ") VALUES ( "+ placeholders +" ) COMMIT"
    try:
        execute_query(sql)
    except SqlError as err:
        print(err)

    print(1)
if __name__ =='__main__':
    etl('dd')
    print('\"%s\"')
    # 'INSERT INTO classes ( id, class_description, teacher ) VALUES ( 001, 'math', 'Smitch' )'

from urllib.parse import quote
import requests
from creds import fb_access_token
facebook_api_url = 'https://graph.facebook.com/me/picture?redirect=false'
picture_data = requests.get(facebook_api_url + '&access_token=' + quote(fb_access_token))
assert picture_data.status_code == 200, 'API call failed: {} {}'.format(
    picture_data.status_code, picture_data.text)
picture_url = picture_data.json()['data']['url']
# Now we have the URL for the photo, and can do something with it.

import requests
from api_info import API_DOMAIN
API_URL = 'https://{}'.format(API_DOMAIN)
resp = requests.get(API_URL + '/items')
assert resp.status_code == 200, 'Cannot get todo items: {}'.format(resp.status_code)
todo_items = resp.json()
for item in todo_items:
    # Do something, like print it out, etc.

# Retry this many times before giving up.
MAX_TRIES = 3
tries = 0
resp = None
while True:
    resp = requests.get(API_URL + '/items')
    if resp.status_code == 500 and tries < MAX_TRIES:
        tries += 1
        continue
    break
todo_items = resp.json()
for item in todo_items:
# Do something, like print it out, etc.