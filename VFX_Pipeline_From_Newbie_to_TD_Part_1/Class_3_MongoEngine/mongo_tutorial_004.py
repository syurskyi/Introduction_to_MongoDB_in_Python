from mongoengine import *

connect("fxphd")

class Project(Document):
    name = StringField()
    client_name = StringField()

project = Project(name="My Test Project", client_name="fxphd").save()

class Shot(Document):

    name = StringField()
    project = ReferenceField("Project")

# for i in range(10):
#     shot = Shot(name = str(i).zfill(4))
#     shot.project = project
#     shot.save()

project = Project(name="My Test Project")
search = Shot.objects()

for shot in search:
    print(shot.name)
print()

for shot in search:
    print(shot.project)
print()

for shot in search:
    print(shot.project.name)
print()

for shot in search:
    print(shot.project.client_name)
print()