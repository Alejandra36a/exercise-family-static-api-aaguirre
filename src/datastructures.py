
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "name": "John",
                "age": 33,
                "Lucky_Numbers": [7,13,22],
                "id": self._generate_id(),
                "last_name": self.last_name
            },
            {
                "name": "Jane",
                "age": 35,
                "Lucky_Numbers": [10, 14, 3],
                "id": self._generate_id(),
                "last_name": self.last_name
            },
            {
                "name": "Jimmy",
                "age": 5,
                "Lucky_Numbers": [1],
                "id": self._generate_id(),
                "last_name": self.last_name
            }
        ]

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    
    def add_member(self, member):
        #genero un nuevo ID con la función generate_id y asignarlo al nuevo miembro de la familia:
        if "id" not  in member: 
            member['id'] = self._generate_id()
        #le agrego el apellido (para que tenga el mismo q todos los miembros):
        member['last_name'] = self.last_name
        #agrego al miembro de la familia
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member["id" ]== id:
                self._members.remove(member)
                return {"done": True}
        return False 
        

    def get_member(self,id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members 