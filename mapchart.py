class Path:
    """
    "New_Castle__DE"
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

class Group:
    """
        "#cc3333": {
            "div": "#box0",
            "label": "",
            "paths": [
                "New_Castle__DE",
                "Sussex__DE",
                "Kent__DE"
            ]
        },
    """
    def __init__(self, name, color, id_number, paths):
        self.name = name
        self.color = color
        self.id_number = id_number
        self.paths = paths

    def __str__(self):
        out = ''
        out += '"' + self.color +  '":{'
        out += '"div":"#box' +  str(self.id_number) +  '",'
        out += '"label":"' + self.name +  '",'
        out += '"paths":['
        if len(self.paths) > 0:
            for path in self.paths:
                out += '"' + str(path) + '",'
            out = out[:-1]
        out += ']}'
        return out

class MapchartJson:
    """
    {
    "groups": {
        "#cc3333": {
            "div": "#box0",
            "label": "",
            "paths": [
                "New_Castle__DE",
                "Sussex__DE",
                "Kent__DE"
            ]
        },
        "title": "",
        "hidden": [],
        "borders": "#000000"
    }
    """
    def __init__(self, groups, title="", hidden=[], border_color="#000000"):
        self.groups = groups
        self.title = title
        self.hidden = hidden
        self.border_color = border_color

    def __str__(self):
        out = '{"groups": {'
        for i, group in enumerate(self.groups):
            out += str(group)
            out += ','
        out = out[:-1]
        out += '},"'

        out += 'title":"' + self.title + '",'

        out += '"hidden":['
        if len(self.hidden) > 0:
            for hid in self.hidden:
                out += str(hid)
                out += ','
            out = out[:-1]
        out += '],'

        out += '"borders":"' + self.border_color + '"}'

        return out