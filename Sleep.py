import time
from time import sleep

class Sleep:
    def test_sleep(self):
        sleep(2)
        print('Hello world')

    def test_timestamp(self):

        for i in range(5):
            current_time = time.localtime()
            timestamp = time.strftime("%I:%m:%S",current_time)
            time.sleep(2)
            print(timestamp)

    def user_experience(self):
        story_intro = ["It", "was", "a", "dark", "and", "stormy", "night", "..."]

        for word in story_intro:
            sleep(1)
            print(word)