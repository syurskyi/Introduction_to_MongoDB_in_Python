from mongoengine import *

connect("fxphd")


class User(Document):
    first_name = StringField()
    last_name = StringField()
    gender = StringField(choices=['Female', 'Male'])
    age = IntField()
    married = BooleanField()


def generate_user_collection():
    text_file = open('user.txt', 'r')
    for line in text_file:
        stripped_line = line.strip()
        u = stripped_line.split(',')
        print(u)
        user = User()
        user.first_name = u[0]
        user.last_name = u[1]
        user.gender = u[2]
        user.age = u[3]
        user.married = u[4] == "Married"
        user.save()

generate_user_collection()
