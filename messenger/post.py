import datetime
import json

class Post:
    def __init__(self, username, text, timestamp=None, likes=0, liked_users=None, comments=None):
        self.username = username  # Имя пользователя, который создал пост
        self.text = text  # Текст поста
        self.timestamp = timestamp or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Время публикации
        self.likes = likes  # Количество лайков
        self.liked_users = liked_users or []  # Список пользователей, которые лайкнули пост
        self.comments = comments or []  # Список комментариев

    def add_comment(self, comment):
        # Добавление комментария к посту
        self.comments.append(comment)

    def toggle_like(self, username):
        # Если пользователь уже лайкнул пост, убираем его лайк
        if username in self.liked_users:
            self.liked_users.remove(username)
            self.likes -= 1
        else:
            self.liked_users.append(username)
            self.likes += 1

    def to_dict(self):
        # Преобразование поста в словарь для сохранения в JSON
        return {
            "username": self.username,
            "text": self.text,
            "timestamp": self.timestamp,
            "likes": self.likes,
            "liked_users": self.liked_users,
            "comments": self.comments
        }

    @classmethod
    def from_dict(cls, post_data):
        # Восстановление поста из словаря
        return cls(
            username=post_data["username"],
            text=post_data["text"],
            timestamp=post_data["timestamp"],
            likes=post_data["likes"],
            liked_users=post_data["liked_users"],
            comments=post_data["comments"]
        )