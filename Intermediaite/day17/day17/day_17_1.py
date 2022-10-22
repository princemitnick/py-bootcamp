class User:

    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.lastname = None
        self.firstname = None

    def user_to_string(self):
        print(f"{self.lastname} - {self.firstname}")
user1 = User(1, "prince");

user1.lastname = "Jean Baptiste"
user1.firstname = "Prince Stanley"


user1.user_to_string()