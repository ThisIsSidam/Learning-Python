#Healthy Programmer

'''
This time we'll be programming an alarm. The alarm will be for drinking water,
eyes' exercise and a little streching. The working time for a programmer is around
9AM to 5PM, so in these 8 hours you have to make that programmer drink water at intervals,
eyes' exercise would be every half an hour and streching would be every 45mn.
Also, make the a log file of when the the alarm shoots off.
Also, this is a prototype program that we'll have to test so, we'll keep intervals
in seconds instead of hours. Last thing, only stuff learnt until Day20 is allowed
along with Pygame, that we haven't actually learnt but have to study ourselves.
'''


from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogsEx7.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 4
    exsecs = 3
    eyessecs = 4.5

while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('Water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('exercise.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")

        