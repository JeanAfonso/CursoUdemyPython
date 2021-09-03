"""
public,
_protected/private(public _),
__private(_CLASSNAME__attributeName)
"""


class DataBase:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    def insert_client(self, id, name):
        if 'clients' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})

    def clients_list(self):
        for id, name in self.__data['clients'].items():
            print(id, name)

    def del_client(self, id):
        del self.__data['clients'][id]


bd = DataBase()
bd.insert_client(1, 'Jean')
bd.insert_client(2, 'Juliana')
bd.insert_client(3, 'Rose')

# Here python create other __data, because the __data
# in DataBase Class is not public, is private.
bd.__data = 'Other Thing'
# print(bd.__data)
print(bd._DataBase__data) # To access a private attribute use this.
# bd._data = 'Other thing' - don't access the protected attribute or method, if you do you crash the program.
bd.del_client(2)
# bd.clients_list()
# bd.data = 'Other value' - This variable crash the program because you can't set attribute in data, data is a GETTER,
# for set attribute, create a SETTER.

