import hashlib

class User:
    def __init__(self, username, password, is_hashed = False):
        self.username = username
        if is_hashed:
            self.password = password
        else:
            self.password = self.create_password(password)

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return User(data["username"], data["password"], is_hashed=True)

    def create_password(self, password):
        # Создание хешированного пароля с добавлением "соли"
        hashed_password = hashlib.sha256(
            (
                "!papper4589"
                + password
                + "".join(
                    "0" if char in "aeiouAEIOU" else "1" if char.isalpha() else char
                    for char in password
                )
            ).encode()
        ).hexdigest()
        return hashed_password

    def check_password(self, password):
        # Проверка введенного пароля с сохраненным хешем
        hashed_input_password = hashlib.sha256(
            (
                "!papper4589"
                + password
                + "".join(
                    "0" if char in "aeiouAEIOU" else "1" if char.isalpha() else char
                    for char in password
                )
            ).encode()
        ).hexdigest()
        return self.password == hashed_input_password

    def add_post(self, post):
        # Добавление поста в список постов пользователя
        self.posts.append(post)

    def add_comment(self, post_id, comment):
        # Добавление комментария к конкретному посту
        if post_id not in self.comments:
            self.comments[post_id] = []
        self.comments[post_id].append(comment)

    def __str__(self):
        return self.username
