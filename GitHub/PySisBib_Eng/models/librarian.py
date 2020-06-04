from Database import Database


class Librarian:

    def __init__(self, user: str, password: str, name: str, age: int, cpf: str):
        self.user = user
        self.password = password
        self.name = name
        self.age = age
        self.cpf = cpf

    def insere_bibliotecario(self):
        database = Database()
        librarians = database.db.librarians

        lib_insert = {
            "name": self.name,
            "age": self.age,
            "cpf": self.cpf,
            "user": self.user,
            "password": self.password
        }
        try:
            result = librarians.insert_one(lib_insert).inserted_id
            print(result)
            return True if result else False
        except ConnectionError:
            print('Inaccessible server.');

    @staticmethod
    def authenticate(user, password):
        database = Database()
        librarians = database.db.librarians

        try:
            lib = librarians.find_one({
                "user": user,
                "password": password
            })
        except ConnectionError:
            print("Inaccessible server.")


        database.client.close()
        return True if lib else None


