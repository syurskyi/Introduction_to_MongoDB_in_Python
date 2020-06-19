from mongoengine import *

connect("fxphd")


class User(Document):
    first_name = StringField()
    last_name = StringField()
    gender = StringField(choices=['Female', 'Male'])
    age = IntField()
    married = BooleanField()

    def __str__(self):
        return "<User object>: %s %s, age: %s" % (self.first_name, self.last_name, self.age)


search = User.objects()
for u in search:
    print(u.first_name)
print()

search = User.objects().count()
print(search)
print()

search = User.objects()
for u in search:
    print(u)
print()

search = User.objects().order_by("-age")
for u in search:
    print(u)
print()

search = User.objects().average("age")
print(search)
print()

search = User.objects().sum("age")
print(search)
print()

search = User.objects()[0:2]
print(search)
print()

search = User.objects(age=22)
print(search)
print()

search = User.objects(age=23, first_name="Spike")
print(search)
print()

search = User.objects(age=23, first_name="Spike").get()
print(search)
print()

