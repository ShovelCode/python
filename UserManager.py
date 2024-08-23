class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username, email):
        if self._validate_email(email):
            self.users.append({'username': username, 'email': email})
        else:
            print("Invalid email address.")

    def _validate_email(self, email):
        return '@' in email

    def get_users(self):
        return self.users

# Usage
manager = UserManager()
manager.add_user('john_doe', 'john.doe@example.com')
print(manager.get_users())
