from atlassian import Confluence

# połączenie z confluence
confluence = Confluence(
    url='http://conflenecobawroc.corp.capgemini.com',
    username='aswierko',
    password='Wroclaw123456')

# status = confluence.create_page(
#     space='Coba',
#     title='147',
#     body='TESTOWY',
#     parent_id=3702829,
#     type='page')
#
# print(status)

page_id = confluence.get_page_id('COBA','OneNote')
print(page_id)

