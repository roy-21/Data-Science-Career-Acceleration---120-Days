'''
12.10 - Equality
Goal: Make User (1) equal to another User (1). 
Deep Dive: By default, checks memory address (identity). 
Override_eq to check content (value).
'''
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    # Override equality
    def __eq__(self, other):
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name})"



user1 = User(1, "Alice")
user2 = User(1, "Alice")
user3 = User(2, "Bob")

print(user1 == user2)
print(user1 == user3)