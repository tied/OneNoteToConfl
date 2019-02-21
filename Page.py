class Page (object):
    name = ""
    parent_name = ""
    path = ""
    is_file = False

    def __init__(self, name, parent_name, path, is_file):
        self.name = name
        self.parent_name = parent_name
        self.path = path
        self.is_file = is_file