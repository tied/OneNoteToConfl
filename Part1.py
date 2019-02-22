from atlassian import Confluence
import json
import requests

mainFolder="C:\\Users\\aswierko\\Documents\\OneNote\\Fold1\\folder1plik1.html"
space='COBA'
parent_page_id=3702847
parent_page_title='OneNote'
auth=('aswierko','Wroclaw123456')

# połączenie z confluence
confluence = Confluence(
    url='http://conflenecobawroc.corp.capgemini.com',
    username='aswierko',
    password='Wroclaw123456')

# reading html file
myfile = open(mainFolder, 'r')
myFileString = ""
for x in myfile:
    myFileString = myFileString + x

html = {
    'value': myFileString,
    'representation': 'editor'
}

def convert_db_to_view(auth2, html):
    url = 'http://conflenecobawroc.corp.capgemini.com/rest/api/contentbody/convert/view'

    data2 = {
        'value': html,
        'representation': 'storage'
    }

    r = requests.post(url,
                      data=json.dumps(data2),
                      auth=auth2,
                      headers={'Content-Type': 'application/json'}
                      )
    print("status  convert_db_to_view")
    print(r.status_code)
    return r.json()

def create_page_data(space, title, body, parent_id,auth):
    url = 'http://conflenecobawroc.corp.capgemini.com/rest/api/content/'
    data = {
        'type': 'page',
        'title': title,
        'space': {'key': space},
        'body': {'storage': body}}
    if parent_id:
        data['ancestors'] = [{'type': 'page', 'id': parent_id}]

    r = requests.post(url,
                      data=data,
                      auth=auth,
                      headers={'Content-Type': 'application/json'}
                      )
    return r.json()


def convert_view_to_db(auth2, html):
    url = 'http://conflenecobawroc.corp.capgemini.com/rest/api/contentbody/convert/storage'

    data2 = {
        'value': html,
        'representation': 'editor'
    }

    r = requests.post(url,
                      data=json.dumps(data2),
                      auth=auth2,
                      headers={'Content-Type': 'application/json'}
                      )

    return r.json()


a=convert_view_to_db(auth, myFileString)
print(a)
status = create_page_data(
    space=space,
    title="NOWA STRONA ONE NOTE",
    body=a,
    parent_id=parent_page_id,
    auth=auth
)
print(status)

