class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.active = True

    def delete_user(self, target):
        print("Permission denied: Only admin can delete users.")

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, active={self.active})"


class Admin(User):
    def delete_user(self, target):
        if isinstance(target, User):
            target.active = False
            print(f"Admin deleted user: {target.name}")
        else:
            print("Invalid target")

u1 = User(1, "Aman")
u2 = User(2, "Riya")
admin = Admin(99, "Ankur")

print(u1)
print(u2)

admin.delete_user(u2)
print(u2)
