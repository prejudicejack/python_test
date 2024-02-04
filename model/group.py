class Group:
    def __init__(self, name=None, header=None, footer=None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id


class SelectGroupByName:
    def __init__(self, name):
        self.name = name
