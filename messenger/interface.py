from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter.simpledialog import askstring
from user import User
from post import Post
from chat import Chat
import json


class MessengerInterface:
    def __init__(self, master):
        # Инициализация главного окна приложения
        self.master = master
        self.master.title("Messenger")
        self.master.geometry("800x600")
        self.master.configure(bg="#B1A296")

        self.users = {}  # Словарь для хранения пользователей
        self.current_user = None  # Текущий пользователь
        self.current_chat = None  # Текущий чат

        # Создаем три чата с названиями тем
        self.chats = {
            "Настольные игры": Chat("Настольные игры"),
            "Книжный клуб": Chat("Книжный клуб"),
            "Фильмы и сериалы": Chat("Фильмы и сериалы"),
        }
        # Список всех чатов сохраняется в отдельном файле
        self.load_chat_list()  # Загрузка списка чатов
        # Загрузка данных пользователей и постов из файлов
        self.load_users()
        self.load_chats()  # Загрузка чатов при инициализации

        # Основной фрейм для размещения виджетов
        self.frame = Frame(self.master, bg="#B1A296")
        self.frame.pack(pady=20)

        # Фреймы для логина и регистрации
        self.login_frame = Frame(self.frame, bg="#B1A296")
        self.register_frame = Frame(self.frame, bg="#B1A296")

        self.create_login_widgets()
        self.create_register_widgets()

        # Событие закрытия окна
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_login_widgets(self):
        self.login_frame.pack()

        Label(self.login_frame, text="Login", bg="#7395AE", fg="white").grid(
            row=0, column=1, pady=10
        )

        Label(self.login_frame, text="Username:", bg="#B1A296").grid(row=1, column=0)
        self.login_username = Entry(self.login_frame)
        self.login_username.grid(row=1, column=1)

        Label(self.login_frame, text="Password:", bg="#B1A296").grid(row=2, column=0)
        self.login_password = Entry(self.login_frame, show="*")
        self.login_password.grid(row=2, column=1)

        Button(
            self.login_frame, text="Login", command=self.login, bg="#379683", fg="white"
        ).grid(row=3, column=1, pady=5)
        Button(
            self.login_frame,
            text="Register",
            command=self.show_register_frame,
            bg="#557A95",
            fg="white",
        ).grid(row=4, column=1, pady=5)

    def create_register_widgets(self):
        self.register_frame.pack_forget()

        Label(self.register_frame, text="Register", bg="#7395AE", fg="white").grid(
            row=0, column=1, pady=10
        )

        Label(self.register_frame, text="Username:", bg="#B1A296").grid(row=1, column=0)
        self.register_username = Entry(self.register_frame)
        self.register_username.grid(row=1, column=1)

        Label(self.register_frame, text="Password:", bg="#B1A296").grid(row=2, column=0)
        self.register_password = Entry(self.register_frame, show="*")
        self.register_password.grid(row=2, column=1)

        Button(
            self.register_frame,
            text="Register",
            command=self.register,
            bg="#379683",
            fg="white",
        ).grid(row=3, column=1, pady=5)
        Button(
            self.register_frame,
            text="Back to Login",
            command=self.show_login_frame,
            bg="#557A95",
            fg="white",
        ).grid(row=4, column=1, pady=5)

    def show_register_frame(self):
        self.login_frame.pack_forget()
        self.register_frame.pack()

    def show_login_frame(self):
        self.register_frame.pack_forget()
        self.login_frame.pack()

    def register(self):
        username = self.register_username.get().strip()
        password = self.register_password.get().strip()

        if not username or not password:
            showerror("Error", "Username and password cannot be empty!")
            return

        if username in self.users:
            showerror("Error", "User already exists!")
        else:
            new_user = User(username, password)
            self.users[username] = new_user
            showinfo("Success", "Registration successful!")
            self.save_users()  # Сохранение пользователей после регистрации
            self.show_login_frame()

    def login(self):
        username = self.login_username.get().strip()
        password = self.login_password.get().strip()

        if not username or not password:
            showerror("Error", "Username and password cannot be empty!")
            return

        user = self.users.get(username)
        if user and user.check_password(password):
            self.current_user = user
            self.show_chat_window()
        else:
            showerror("Error", "Invalid username or password!")

    def show_chat_window(self):
        # Скрываем все элементы основного окна
        self.frame.pack_forget()
        if hasattr(self, 'chat_list_frame') and self.chat_list_frame.winfo_exists():
            self.chat_list_frame.destroy()
        if hasattr(self,'chat_frame'):
            self.chat_frame.destroy()
        # Создаем и показываем фреймы для чатов и сообщений
        self.chat_list_frame = Frame(self.master, bg="#557A95", width=200)
        self.chat_list_frame.pack(side=LEFT, fill=Y)

        self.chat_frame = Frame(self.master, bg="white", width=600)
        self.chat_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        Label(self.chat_list_frame, text="Чаты", bg="#557A95", fg="white").pack(pady=10)
        Button(
            self.chat_list_frame,
            text="Создать новый чат",
            command=self.create_new_chat,
            bg="#557A95",
            fg="white",
            width=20,
            relief=RAISED
        ).pack(pady=10)
        # Кнопка выхода из аккаунта
        Button(
            self.chat_list_frame,
            text="Logout",
            command=self.logout,
            bg="#B1A296",
            fg="white",
        ).pack(side=BOTTOM, pady=10)

        # Отображение списка чатов
        for chat_name in self.chats.keys():
            chat_button = Button(
                self.chat_list_frame,
                text=chat_name,
                command=lambda name=chat_name: self.show_chat_content(name),
                bg="#379683",
                fg="white",
                width=20,
                relief=RAISED
            )
            chat_button.pack(padx=10, pady=5, fill=X)

        # Поле ввода постов и кнопка отправки
        self.post_entry = Entry(self.chat_frame, state=DISABLED)
        self.post_entry.pack(side=BOTTOM, fill=X, padx=10, pady=10)

        self.send_button = Button(
            self.chat_frame,
            text="Отправить",
            command=self.send_post,
            bg="#379683",
            fg="white",
            state=DISABLED,
        )
        self.send_button.pack(side=BOTTOM, padx=10, pady=5)


    def create_new_chat(self):
        """Функция для создания нового чата"""
        chat_name = askstring("Новый чат", "Введите название нового чата:")
        if chat_name and chat_name not in self.chats:
            self.chats[chat_name] = Chat(chat_name)
            self.save_chat_list()  # Сохраняем обновленный список чатов
            self.show_chat_window()  # Перерисовываем окно чатов
        elif chat_name:
            showerror("Ошибка", "Чат с таким именем уже существует.")

    def save_chat_list(self):
        """Сохраняем список чатов в отдельный файл."""
        with open("chats_list.json", "w", encoding="utf-8") as file:
            chat_names = list(self.chats.keys())
            json.dump(chat_names, file, ensure_ascii=False, indent=4)

    def load_chat_list(self):
        """Загружаем список чатов из файла."""
        try:
            with open("chats_list.json", "r", encoding="utf-8") as file:
                chat_names = json.load(file)
                for chat_name in chat_names:
                    if chat_name not in self.chats:
                        self.chats[chat_name] = Chat(chat_name)
        except FileNotFoundError:
            pass  # Если файла нет, просто игнорируем

    def logout(self):
        # Clear current user
        self.current_user = None
        self.current_chat = None

        # Destroy all widgets in the main window
        for widget in self.master.winfo_children():
            widget.destroy()

        # Recreate the main frame
        self.frame = Frame(self.master, bg="#B1A296")
        self.frame.pack(pady=20)

        # Recreate login and register frames
        self.login_frame = Frame(self.frame, bg="#B1A296")
        self.register_frame = Frame(self.frame, bg="#B1A296")

        # Recreate login and register widgets
        self.create_login_widgets()
        self.create_register_widgets()

        # Show the login frame
        self.show_login_frame()

        # Reset the window size
        self.master.geometry("800x600")

    def send_post(self):
        post_text = self.post_entry.get()
        if not post_text.strip():
            showerror("Error", "Введите текст поста.")
            return

        if self.current_chat is None:
            showerror("Error", "Выберите чат для отправки поста.")
            return

        chat = self.chats[self.current_chat]

        new_post = Post(self.current_user.username, post_text)
        chat.add_post(new_post)

        self.post_entry.delete(0, END)
        self.show_chat_content(self.current_chat)

    def show_chat_content(self, chat_name):
        self.current_chat = chat_name

        # Очищаем предыдущее содержимое чата, кроме поля ввода и кнопки отправки
        for widget in self.chat_frame.winfo_children():
            if widget not in [self.post_entry, self.send_button]:
                widget.destroy()

        # Если поле ввода и кнопка отправки еще не существуют, создаем их
        if not hasattr(self, 'post_entry') or not self.post_entry.winfo_exists():
            self.post_entry = Entry(self.chat_frame)
            self.post_entry.pack(side=BOTTOM, fill=X, padx=10, pady=10)

        if not hasattr(self, 'send_button') or not self.send_button.winfo_exists():
            self.send_button = Button(
                self.chat_frame,
                text="Отправить",
                command=self.send_post,
                bg="#379683",
                fg="white"
            )
            self.send_button.pack(side=BOTTOM, padx=10, pady=5)

        # Активируем поле ввода и кнопку
        self.post_entry.config(state=NORMAL)
        self.send_button.config(state=NORMAL)

        # Получаем и отображаем посты
        chat = self.chats[chat_name]
        for post in chat.get_all_posts():
            post_frame = Frame(self.chat_frame, bg="lightgrey", bd=1, relief=SUNKEN)
            post_frame.pack(fill=X, padx=10, pady=5)

            username_label = Label(post_frame, text=post.username, bg="lightgrey", font=("Arial", 10, "bold"))
            username_label.pack(anchor=W)

            text_label = Label(post_frame, text=post.text, bg="lightgrey", wraplength=550)
            text_label.pack(anchor=W)
            time_label = Label(post_frame, text=post.timestamp, bg="lightgrey", font=("Arial", 8))
            time_label.pack(anchor=W)

            # Добавим кнопку для комментариев
            comment_button = Button(post_frame, text="Комментировать", command=lambda p=post: self.show_comments(p), bg="#379683", fg="white")
            comment_button.pack(side=BOTTOM, padx=5, pady=5)

            # Определяем текст кнопки лайка в зависимости от того, лайкнул ли пост текущий пользователь
            if self.current_user.username in post.liked_users:
                like_button_text = f"Unlike ({post.likes})"
            else:
                like_button_text = f"Like ({post.likes})"

            # Добавим кнопку для лайков
            like_button = Button(post_frame, text=like_button_text, command=lambda p=post: self.like_post(p), bg="#557A95", fg="white")
            like_button.pack(side=LEFT, padx=5, pady=5)

    def like_post(self, post):
        # Текущий пользователь ставит или убирает лайк
        post.toggle_like(self.current_user.username)
        self.show_chat_content(self.current_chat)  # Обновляем содержимое чата, чтобы отобразить количество лайков



    def save_chats(self):
        """Сохранение всех постов и чатов в файлы"""
        for chat in self.chats.values():
            chat.save_posts()

    def load_chats(self):
        """Загрузка всех чатов и постов из файлов"""
        for chat in self.chats.values():
            chat.load_posts()


    def on_closing(self):
        self.save_users()  # Сохранение пользователей
        self.save_chats()  # Сохранение постов и чатов
        self.save_chat_list()  # Сохранение списка чатов
        self.master.destroy()


    def save_users(self):
        with open("users.json", "w") as file:
            json_users = {
                username: user.to_dict() for username, user in self.users.items()
            }
            json.dump(json_users, file)

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                json_users = json.load(file)
                for username, user_data in json_users.items():
                    self.users[username] = User.from_dict(user_data)
        except FileNotFoundError:
            pass  # Если файла нет, просто пропускаем

    def show_comments(self, post):
        # Сохраняем текущий чат перед показом комментариев
        current_chat_name = self.current_chat

        # Скрываем поле ввода и кнопку отправки, вместо уничтожения
        self.post_entry.pack_forget()
        self.send_button.pack_forget()

        # Очищаем текущее содержимое
        for widget in self.chat_frame.winfo_children():
            widget.destroy()

        # Кнопка "Назад"
        back_button = Button(
            self.chat_frame,
            text="Назад к чату",
            command=lambda: self.show_chat_content(current_chat_name),
            bg="#557A95",
            fg="white"
        )
        back_button.pack(anchor=NW, padx=10, pady=5)

        # Отображение самого поста
        post_frame = Frame(self.chat_frame, bg="lightgrey", bd=1, relief=SUNKEN)
        post_frame.pack(fill=X, padx=10, pady=5)

        post_label = Label(
            post_frame, 
            text=post.username, 
            bg="lightgrey", 
            font=("Arial", 10, "bold")
        )
        post_label.pack(anchor=W)

        text_label = Label(
            post_frame, 
            text=post.text, 
            bg="lightgrey",
            wraplength=550
        )
        text_label.pack(anchor=W)

        time_label = Label(
            post_frame, 
            text=post.timestamp, 
            bg="lightgrey", 
            font=("Arial", 8)
        )
        time_label.pack(anchor=W)

        comments_frame = Frame(self.chat_frame, bg="white")
        comments_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)

        # Отображение комментариев
        for comment in post.comments:
            comment_frame = Frame(
                comments_frame, 
                bg="lightyellow", 
                bd=1, 
                relief=SUNKEN
            )
            comment_frame.pack(fill=X, pady=2)

            comment_label = Label(
                comment_frame, 
                text=comment, 
                bg="lightyellow",
                wraplength=550
            )
            comment_label.pack(anchor=W, padx=5, pady=2)

        # Поле для ввода нового комментария
        self.comment_entry = Entry(self.chat_frame)
        self.comment_entry.pack(side=BOTTOM, fill=X, padx=10, pady=5)

        # Кнопка для отправки комментария
        submit_button = Button(
            self.chat_frame,
            text="Отправить комментарий",
            command=lambda: self.submit_comment(post, current_chat_name),
            bg="#379683",
            fg="white"
        )
        submit_button.pack(side=BOTTOM, padx=10, pady=5)

    def submit_comment(self, post, chat_name):
        comment_text = self.comment_entry.get()
        if not comment_text.strip():
            showerror("Error", "Введите текст комментария.")
            return

        post.add_comment(comment_text)
        self.comment_entry.delete(0, END)
        self.show_comments(post)  # Обновляем отображение комментариев


if __name__ == "__main__":
    root = Tk()
    messenger = MessengerInterface(root)  # Создаем экземпляр интерфейса мессенджера
    root.mainloop()  # Запускаем главный цикл приложения
