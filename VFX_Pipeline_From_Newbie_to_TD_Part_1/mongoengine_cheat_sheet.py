#MongoEngine cheat sheet

#Let's import MongoEngine and connect to a fxphd database

from mongoengine import *
connect("fxphd")



#Let's define a User class for MongoEngine

class User(Document):

    first_name = StringField(required=True) # We define a first name and tell MongoEngine it is required when making a new doc
    last_name = StringField(required=True) # Same thing as first name
    age = IntField() # A simple field for the age.
    description = StringField(required=True, min_length=10, max_length=200) #Limit the characters in this field between 10 and 200
    artist_type = StringField(choices=["compositor", "modeler"]) # Make sure the value is in the choices

    # An email field that is also required but also needs to be unique inside the DB. Let's also use
    # a function to make sure there is no uppercase in the email...
    def validate_email(val):

        if not val.islower():
            raise ValidationError("Value must be lowercase")
    email = EmailField(unique=True, required=True, validation=validate_email)



    #Here we use the meta property to specify things like search indexes and default ordering
    meta = {
        "ordering" : ["first_name"],
        "indexes" : ["first_name","age"]}

    # Here we define a property to return the full name based on 2 document's properties

    @property
    def name(self):
        return "%s %s" % (self.first_name, self.last_name)

    #We define the __str__ to return a string representation when printing the obj
    def __str__(self):
        return "<Users object: %s %s>" % (self.first_name,self.last_name)


# We create an object with some properties
user1 = User(first_name="John", last_name="Smith", email="jsmith@fxphd.com", artist_type="compositor")

# We can also set some properties like that
user1.description = "This is a description"
user1.age = 20


#Let's save the document in the database
user1.save()

#Lets print it to see if it's working
print user1  #<Users object: John Smith>




#Let's add 4 more...

user2 = User(first_name="Bob", last_name="White", age=19,email="bwhite@fxphd.com", artist_type="compositor",
             description="This is a nice description").save()
user3 = User(first_name="Simon", last_name="Smith", age=54,email="ssmith@fxphd.com", artist_type="modeler",
             description="This is a nice description too").save()
user4 = User(first_name="Robert", last_name="Black", age=23,email="rblack@fxphd.com", artist_type="compositor",
             description="This is another description").save()
user5 = User(first_name="Richard", last_name="Grey", age=41,email="rgrey@fxphd.com", artist_type="modeler",
             description="This is just a description").save()


#Now lets search our database!

#Get all documents
search = User.objects()

#Get the first document that match the query
search = User.objects().first()

#Get documents where the age is higher than 30 years old
search = User.objects(age__gt=30)

#Get documents with an "o" in the first name
search = User.objects(first_name__contains="o")

#Get a unique document
search = User.objects(email="ssmith@fxphd.com").get()

#Delete a document
doc = User.objects(email="ssmith@fxphd.com").get()
doc.delete()



#We can also make dynamic documents

class Software(DynamicDocument):
    name = StringField()

nuke = Software(name="Nuke", version="12.0v1")
nuke.save()




