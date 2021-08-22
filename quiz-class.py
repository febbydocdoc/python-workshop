class Person:
    id = None
    name = None
    age = None
    gender = None

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.gender = kwargs['gender']

    def print_detail():
        '''
        show id, name, age and gender
        '''
        pass   

class People:
    data = []

    def __init__(*args):
        for arg in args:
            arg['id'] = len(self.data) + 1
            self.data.append(Person(**arg))
    
    def search_by_gender(self, gender):
        pass
    
    def search_by_name(self, name):
        pass

    def update_person_by_id(self, id):
        pass
    
    def delete_person_by_id(self, id):
        pass

    def add_person(self, data):
        pass



people = People([
    {'name': 'Michael Jordan','age' : '46', 'gender' : 'Male'},
    {'name': 'Scottie Pippen','age' : '45', 'gender' : 'Male'},
    {'name': 'Tony Kukoc','age' : '43', 'gender' : 'Male'},
    {'name': 'Nicole Kidman','age' : '43', 'gender' : 'Female'},
    {'name': 'Marrie Ahn','age' : '46', 'gender' : 'Female'}
])
