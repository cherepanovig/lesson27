# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы
# добавления видео, авторизации и регистрации пользователя и т.д.

import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        #print(f'{nickname}, {self.password}, {age}+')

    def __hash__(self):
        return hash(self.password)

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __str__(self):
        return f'{self.nickname}'

    def __repr__(self):  # Для читабельного отображения списка users
        return f'({self.nickname}, {self.password})'


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):  # Для читабельного отображения списка videos
        return f'({self.title}, {self.duration}, {self.adult_mode})'


class UrTube:

    current_user = None

    def __init__(self):
        self.users = []
        self.videos = []

    def log_in(self, login, password):

        for i in self.users:
            if login == i.nickname and hash(password) == hash(i.password):
                self.current_user = i

    def log_out(self):
        self.current_user = None  # Сброс текущего пользователя на None

    def register(self, nickname, password, age):

        for client in self.users:
            if nickname in client.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            if any(map(str.isdigit, password)) != True or len(password) < 8 or any(  # Добавлены требования к паролю
                    i.isupper() for i in password) != True:
                print('Пароль должен содержать хотя бы одну цифру, \n'
                      'иметь длину не менее 8 символов и одну заглавную букву')
                return
            client = User(nickname, password, age)
            self.users.append(client)
            self.log_out()
            self.log_in(client.nickname, client.password)

    def find_title(*args):
        tuple_videos = {}
        movie = ''
        for item in tuple_videos:
            if movie in item:
                return True
        return False

    def add(self, *args):
        for movie in args:
            if self.find_title(movie, self.videos):
                print('Видео существует!')
            else:
                self.videos.append(movie)

    def get_videos(self, name_movie):
        list_movie = []
        for item in self.videos:
            if name_movie.upper() in item.title.upper():
                list_movie.append(item.title)
        return list_movie

    def watch_video(self, name_movie):
        for item in self.videos:
            if name_movie not in item.title:
                # print(name_movie)
                # print(item.title)
                continue
            else:
                if self.current_user and item.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                elif self.current_user:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                #print(f'Видео найдено {name_movie} {self.current_user} {item.adult_mode}')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    #  Добавление видео
    ur.add(v1, v2)
    #  Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', '5Hlolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    #ur.register('check_password', 'zfgAk1s', 24) # Для проверки требований к паролю

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    #  Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    # Вывод в консоль:
    # ['Лучший язык программирования 2024 года']
    # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
    # Войдите в аккаунт, чтобы смотреть видео
    # Вам нет 18 лет, пожалуйста покиньте страницу
    # 1 2 3 4 5 6 7 8 9 10 Конец видео
    # Пользователь vasya_pupkin уже существует
    # urban_pythonist
