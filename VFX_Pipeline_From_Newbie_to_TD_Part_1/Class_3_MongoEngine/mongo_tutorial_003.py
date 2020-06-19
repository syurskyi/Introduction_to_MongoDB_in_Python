from mongoengine import *

connect("fxphd")


class User(Document):
    first_name = StringField()
    last_name = StringField()
    gender = StringField(choices=['Female', 'Male'])
    age = IntField()
    married = BooleanField()

    meta = {
        # "ordering": ["first_name"]
        # "ordering": ["age"]
        "ordering": ["-age"],
        "indexes": ["first_name"]

    }

    def __str__(self):
        return "<User object>: %s %s, age: %s" % (self.first_name, self.last_name, self.age)

search = User.objects()
for u in search:
    print(u)