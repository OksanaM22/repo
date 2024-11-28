# Свой YouTube
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.hash_password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration,  time_now=0, adult_mode = False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.hash_password == hash(password):
                self.current_user = user
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user =User(nickname, password, age)
        self.current_user = new_user
        self.users.append(new_user)
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for video in videos:
            flag = True
            for old_video in self.videos:
                if video.title ==old_video.title:
                    flag = False
                    break
            if flag:
                self.videos.append(video)
    def get_videos(self,search_word):
        result_videos = []
        for video_new in self.videos:
            if search_word.upper() in video_new.title.upper():
                result_videos.append(video_new.title)
        return result_videos
    def watch_video(self, name_film):
        if self.current_user:
            for video in self.videos:
                if video.title == name_film:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for second in range(video.time_now+1, video.duration+1):
                            print(second, end=" ")
                            time.sleep(1)
                        print("Конец видео")
                        video.time_now = 0
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

if __name__=='__main__':

    ur = UrTube()

    v1 = Video('Лучший язык программирования 2024 года', 200)

    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



    # Добавление видео

    ur.add(v1, v2)



    # Проверка поиска

    print(ur.get_videos('лучший'))

    print(ur.get_videos('ПРОГ'))



    # Проверка на вход пользователя и возрастное ограничение

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

    ur.watch_video('Для чего девушкам парень программист?')



    # Проверка входа в другой аккаунт

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

    print(ur.current_user)



    # Попытка воспроизведения несуществующего видео

    ur.watch_video('Лучший язык программирования 2024 года!')
