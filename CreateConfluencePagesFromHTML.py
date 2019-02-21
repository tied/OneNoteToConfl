import os
from atlassian import Confluence
import html

class Page (object):
    name = ""
    parent_name = ""
    path = ""
    is_file = False

    def __init__(self, name):
        self.name = name


path_to_parent_folder = "C:\\Users\\aswierko\\Documents\\OneNote"
parent_folder = 'OneNote'
space = 'COBA'
pages_tab = []

#połączenie z confluence
confluence = Confluence(
    url='http://conflenecobawroc.corp.capgemini.com',
    username='aswierko',
    password='Wroclaw123456')

def add_to_tab(page):
    global pages_tab
    pages_tab.append(page)

def print_tab():
    for object in pages_tab:
        print("Name: " + object.name + " parent: " + object.parent_name + " path: " + object.path)

def save_pages_to_tab(folder):
    list = os.listdir(folder)
    for entry in list:
        temp = folder+"\\"+entry
        name = entry
        is_file = False

        if os.path.isdir(temp):
            save_pages_to_tab(temp)
        else:
            is_file = True

        parent_dir = os.path.split(os.path.dirname(temp))[1]
        page = Page(name)
        page.parent_name = parent_dir
        page.path = temp
        page.is_file = is_file
        add_to_tab(page)

# tworzenie  strony w confluence
def create_a_single_page_in_confluence(title,body,parent_id):
    status = confluence.create_page(
        space=space,
        title=title,
        body=body,
        parent_id=parent_id,
        type='page')
    print(status)

def create_pages_in_confluence(parent_tab):
    current_parent_tab = []

    for parent in parent_tab:
        for object in pages_tab:
            if object.parent_name == parent and confluence.page_exists(space, object.parent_name) and not confluence.page_exists(space, object.name):
                if os.path.isdir(object.path):
                    body = ""
                else:
                    myfile = open(object.path, 'r')
                    myFileString = ""
                    for x in myfile:
                        myFileString = myFileString + x
                    print("!!!!!!!"+object.path)
                    body = myFileString
                parent_id = confluence.get_page_id(space, object.parent_name)
                create_a_single_page_in_confluence(object.name,body,parent_id)

            current_parent_tab.append(object.name)

    create_pages_in_confluence(current_parent_tab)


#main
save_pages_to_tab(path_to_parent_folder)

tab = []
tab.append(parent_folder)
create_pages_in_confluence(tab)
#print_tab()
