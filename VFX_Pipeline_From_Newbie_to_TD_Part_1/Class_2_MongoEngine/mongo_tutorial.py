from mongoengine import *

connect("fxphd")

class User(Document):

    def validate_description(val):

        if not val.islower():
            raise ValidationError("Description need to be lowercase")

    first_name = StringField(required=True)
    last_name = StringField(required=True)
    description = StringField(min_length=5, max_length=50, validation=validate_description)
    favorite_movies = ListField(StringField())
    active = BooleanField(default=True)
    artist_type = StringField(choices=["compositor", "modeler", "lighter"])
    age = IntField()
    email = EmailField(unique=True)

    @property
    def login(self):
        return(self.first_name[0] + self.last_name).lower()

u = User(first_name='John',
         last_name='Smith',
         artist_type='compositor',
         description='this is a test of the description',
         favorite_movies = ["test"],
         age=20,
         email='john@fxphd.com').save()

print(u.login)
search = User.objects()[0]

search.active = False
search.save()
