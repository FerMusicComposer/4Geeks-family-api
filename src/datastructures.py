
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint, sample

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id" : self._generateId(),
                "first_name" : "John",
                "last_name" :  last_name,
                "age" : "33 years old",
                "lucky_numbers": tuple(sample(range(0, 100), 3))
            },
            {
                "id" : self._generateId(),
                "first_name" : "Jane",
                "last_name" : last_name,
                "age" : "35 years old",
                "lucky_numbers": tuple(sample(range(0, 100), 3))
            },
            {
                "id" : self._generateId(),
                "first_name" : "Jimmy",
                "last_name" : last_name,
                "age" : "5 years old",
                "lucky_numbers": tuple(sample(range(0, 100), 3))
            } 
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        

    def delete_member(self, id):
        _id = id
        members = self.get_all_members()

        for member in members:
            if member['id'] == _id:
                members.remove(member)

            return members

    def update_member(self, id, name, age):
        _id = id
        members = self.get_all_members()

        for member in members:
            if member['id'] == _id:
                member['first_name'] = name
                member['age'] = "{member_age} years old".format(member_age=age)


    def get_member(self, id):
        _id = id
        members = self.get_all_members()

        for member in members:
            if member['id'] == _id:
                return member

    def get_all_members(self):
        return self._members
