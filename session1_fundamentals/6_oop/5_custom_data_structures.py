"""
Builtin data structures
how to build your own data structures
a custom dict example
a custom iterable example
"""


class CaseInsensitiveDict(dict):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.data = {k.lower(): v for k, v in self.data.items()}

    def __getitem__(self, key: str | int):
        return self.data[key.lower()]

    def __setitem__(self, key, value):
        self.data[key.lower()] = value

    def __delitem__(self, key):
        del self.data[key.lower()]

    def __contains__(self, key):
        return key.lower() in self.data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)
