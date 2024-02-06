import requests
import time
from datetime import datetime
import os
import random
import pygame
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler('/home/ismail/namaz-vakti/ezan_logs.log', 'a'))
print = logger.info


def fetch_data():
    try:
        formatted_date = datetime.now().strftime('%Y-%m-%d')
        params = {
            'country': 'France',
            'region': 'Centre-Val de Loire',
            'city': 'Saint-Denis-les-Ponts',
            'calculationMethod': 'Turkey',
            'date': formatted_date,
            'timezoneOffset': 60,
            'days': 1,
        }
        response = requests.get('https://namaz-vakti.vercel.app/api/timesFromPlace', params=params)
        return response.json()
    except Exception as e:
        current_date = datetime.now().strftime('%Y-%m-%d')
        data['times'][current_date] = ["6:33", "13:13", "15:37", "18:04", "19:32"]
        return data


def refetch_time():
    current_time = datetime.now().time().strftime('%H:%M')
    target_time = '01:00'
    target_time1 = '10:00'
    if current_time == target_time or current_time == target_time1:
        return True
    else:
        return False


def get_files_from_folder(folder_path):
    try:
        # Get the list of files in the specified folder
        files = os.listdir(folder_path)
        return files
    except OSError as e:
        print("Error reading folder: %s", e)
        return []


def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait until the ezan has finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(60000)


def ezan():
    data = fetch_data()
    current_date = datetime.now().strftime('%Y-%m-%d')
    print('%s - Prayer times : %s', datetime.now(), data['times'][current_date])
    while 1:
        if refetch_time():
            data = fetch_data()
            current_date = datetime.now().strftime('%Y-%m-%d')
            print('%s - Prayer times : %s', datetime.now(), data['times'][current_date])

        if data:
            current_date = datetime.now().strftime('%Y-%m-%d')
            current_time = datetime.now().strftime('%H:%M')

            if data.get('times', {}).get(current_date):
                # Check if the current time is within the schedule for the current date
                is_within_schedule = any(current_time == time for time in data['times'][current_date])
                if is_within_schedule:
                    folder_path = '/home/ismail/namaz-vakti/ezan/'
                    files_in_folder = get_files_from_folder(folder_path)
                    
                    # Play a randomly selected audio file
                    random_file = random.choice(files_in_folder)
                    print("%s - Playing Ezan: %s", current_time, random_file)
                    play_mp3(f"/home/ismail/namaz-vakti/ezan/{random_file}")


ezan()
