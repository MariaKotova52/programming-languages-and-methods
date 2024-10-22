import json
from post import Post
class Chat:
    def __init__(self, chat_name):
        self.chat_name = chat_name  # Название чата
        self.posts = []  # Список постов

        # Загружаем посты из файла при инициализации
        self.load_posts()

    def add_post(self, post):
        # Добавление нового поста
        self.posts.append(post)
        self.save_posts()  # Сохраняем посты в файл после добавления

    def get_all_posts(self):
        return self.posts

    def save_posts(self):
        # Сохранение всех постов в JSON-файл
        posts_data = [post.to_dict() for post in self.posts]
        with open(f"{self.chat_name}_posts.json", "w", encoding="utf-8") as file:
            json.dump(posts_data, file, ensure_ascii=False, indent=4)

    def load_posts(self):
        # Загрузка постов из JSON-файла
        try:
            with open(f"{self.chat_name}_posts.json", "r", encoding="utf-8") as file:
                posts_data = json.load(file)
                self.posts = [Post.from_dict(post) for post in posts_data]
        except FileNotFoundError:
            # Если файла нет, просто начинаем с пустого списка постов
            self.posts = []
