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
        print("Error fetching data: %s", e)
        current_date = datetime.now().strftime('%Y-%m-%d')
        data['times'][current_date] = ["6:33", "13:13", "15:37", "18:04", "19:32"]
        return data

def fetch_data_nv():
    try:
        response = requests.get('https://namazvakitleri.com.tr/_next/data/CqhQpGPfJKTMlJur3oXqo/en/city/6024/chateaudun-prayer-times.json?id=6024&id=chateaudun-prayer-times')
        data = response.json()
        return data["pageProps"]["data"]["PrayerTimes"]
    except Exception as e:
        print("Error fetching nv data: %s", e)
        data["pageProps"]["data"]["PrayerTimes"] = [{'date': '2024-01-30', 'imsak': '06:39', 'yatsi': '19:25', 'ogle': '13:13', 'gunes': '08:19', 'aksam': '17:56', 'ikindi': '15:30', 'hDate': '1445-07-19'}, {'date': '2024-01-31', 'imsak': '06:38', 'yatsi': '19:26', 'ogle': '13:13', 'gunes': '08:18', 'aksam': '17:58', 'ikindi': '15:32', 'hDate': 
            '1445-07-20'}, {'date': '2024-02-01', 'imsak': '06:36', 'yatsi': '19:28', 'ogle': '13:13', 'gunes': '08:17', 'aksam': '17:59', 'ikindi': '15:33', 'hDate': '1445-07-21'}, {'date': '2024-02-02', 'imsak': '06:35', 'yatsi': '19:29', 'ogle': '13:13', 'gunes': '08:15', 'aksam': '18:01', 'ikindi': '15:34', 'hDate': '1445-07-22'}, {'date': '2024-02-03', 'imsak': '06:34', 'yatsi': '19:30', 'ogle': '13:13', 'gunes': '08:14', 'aksam': '18:03', 'ikindi': '15:36', 'hDate': '1445-07-23'}, {'date': '2024-02-04', 'imsak': '06:33', 'yatsi': '19:32', 'ogle': '13:13', 'gunes': '08:13', 'aksam': '18:04', 'ikindi': '15:37', 'hDate': '1445-07-24'}, {'date': '2024-02-05', 'hDate': '1445-07-25', 'imsak': '06:32', 'gunes': '08:11', 'ogle': '13:14', 'ikindi': '15:38', 'aksam': '18:06', 'yatsi': '19:33'}, {'date': '2024-02-06', 'hDate': '1445-07-26', 'imsak': '06:31', 'gunes': '08:10', 'ogle': '13:14', 'ikindi': '15:39', 'aksam': '18:07', 'yatsi': '19:35'}, {'date': '2024-02-07', 'hDate': '1445-07-27', 'imsak': '06:29', 'gunes': '08:08', 'ogle': '13:14', 'ikindi': '15:41', 'aksam': '18:09', 'yatsi': '19:36'}, {'date': '2024-02-08', 'hDate': '1445-07-28', 'imsak': '06:28', 'gunes': '08:07', 'ogle': '13:14', 'ikindi': '15:42', 'aksam': '18:11', 'yatsi': '19:37'}, {'date': '2024-02-09', 'hDate': '1445-07-29', 'imsak': '06:27', 'gunes': '08:05', 'ogle': '13:14', 'ikindi': '15:43', 'aksam': '18:12', 'yatsi': '19:39'}, {'date': '2024-02-10', 'hDate': '1445-07-30', 'imsak': '06:25', 'gunes': '08:04', 'ogle': 
            '13:14', 'ikindi': '15:45', 'aksam': '18:14', 'yatsi': '19:40'}, {'date': '2024-02-11', 'hDate': '1445-08-01', 'imsak': '06:24', 'gunes': '08:02', 'ogle': '13:14', 'ikindi': '15:46', 'aksam': '18:15', 'yatsi': '19:42'}, {'date': '2024-02-12', 'hDate': '1445-08-02', 'imsak': '06:23', 'gunes': '08:01', 'ogle': '13:14', 'ikindi': '15:47', 'aksam': '18:17', 'yatsi': '19:43'}, {'date': '2024-02-13', 'hDate': '1445-08-03', 'imsak': '06:21', 'gunes': '07:59', 'ogle': '13:14', 'ikindi': '15:48', 'aksam': '18:19', 'yatsi': '19:45'}, {'date': '2024-02-14', 'hDate': '1445-08-04', 'imsak': '06:20', 'gunes': '07:57', 'ogle': '13:14', 'ikindi': '15:50', 'aksam': '18:20', 'yatsi': '19:46'}, {'date': '2024-02-15', 'hDate': '1445-08-05', 'imsak': '06:18', 'gunes': '07:56', 'ogle': '13:14', 'ikindi': '15:51', 'aksam': '18:22', 'yatsi': '19:47'}, {'date': '2024-02-16', 'hDate': '1445-08-06', 'imsak': '06:17', 'gunes': '07:54', 'ogle': '13:14', 'ikindi': '15:52', 'aksam': '18:23', 'yatsi': '19:49'}, {'date': '2024-02-17', 'hDate': '1445-08-07', 'imsak': '06:15', 'gunes': '07:52', 'ogle': '13:14', 'ikindi': '15:53', 'aksam': '18:25', 'yatsi': '19:50'}, {'date': '2024-02-18', 'hDate': '1445-08-08', 'imsak': '06:13', 'gunes': '07:51', 'ogle': '13:14', 'ikindi': '15:55', 'aksam': '18:27', 'yatsi': '19:52'}, {'date': '2024-02-19', 'hDate': '1445-08-09', 'imsak': '06:12', 'gunes': '07:49', 'ogle': '13:14', 'ikindi': '15:56', 'aksam': '18:28', 'yatsi': '19:53'}, {'date': '2024-02-20', 'hDate': '1445-08-10', 'imsak': '06:10', 'gunes': '07:47', 'ogle': '13:13', 'ikindi': '15:57', 'aksam': '18:30', 'yatsi': '19:55'}, {'date': '2024-02-21', 'hDate': '1445-08-11', 'imsak': '06:09', 'gunes': '07:45', 'ogle': '13:13', 'ikindi': '15:58', 'aksam': '18:31', 'yatsi': '19:56'}, {'date': '2024-02-22', 'hDate': '1445-08-12', 'imsak': '06:07', 'gunes': '07:44', 'ogle': '13:13', 'ikindi': '15:59', 'aksam': '18:33', 'yatsi': '19:58'}, {'date': '2024-02-23', 'hDate': '1445-08-13', 'imsak': '06:05', 'gunes': '07:42', 'ogle': '13:13', 'ikindi': '16:01', 'aksam': '18:35', 'yatsi': '19:59'}, {'date': '2024-02-24', 'hDate': '1445-08-14', 'imsak': '06:03', 'gunes': '07:40', 'ogle': '13:13', 'ikindi': '16:02', 'aksam': '18:36', 'yatsi': '20:01'}, {'date': '2024-02-25', 'hDate': '1445-08-15', 'imsak': '06:02', 'gunes': '07:38', 'ogle': '13:13', 'ikindi': '16:03', 'aksam': '18:38', 'yatsi': '20:02'}, {'date': '2024-02-26', 'hDate': '1445-08-16', 'imsak': '06:00', 'gunes': '07:36', 'ogle': '13:13', 'ikindi': '16:04', 'aksam': '18:39', 'yatsi': '20:04'}, {'date': '2024-02-27', 'hDate': '1445-08-17', 'imsak': '05:58', 'gunes': '07:34', 'ogle': '13:13', 'ikindi': '16:05', 'aksam': '18:41', 'yatsi': '20:05'}, 
            {'date': '2024-02-28', 'hDate': '1445-08-18', 'imsak': '05:56', 'gunes': '07:32', 'ogle': '13:12', 'ikindi': '16:06', 'aksam': '18:42', 'yatsi': '20:07'}, {'date': '2024-02-29', 'hDate': '1445-08-19', 'imsak': '05:54', 'gunes': '07:30', 'ogle': '13:12', 'ikindi': '16:07', 'aksam': '18:44', 'yatsi': 
            '20:08'}, {'date': '2024-03-01', 'hDate': '1445-08-20', 'imsak': '05:52', 'gunes': '07:29', 'ogle': '13:12', 'ikindi': '16:08', 'aksam': '18:45', 'yatsi': '20:10'}, {'date': '2024-03-02', 'hDate': '1445-08-21', 'imsak': '05:50', 'gunes': '07:27', 'ogle': '13:12', 'ikindi': '16:09', 'aksam': '18:47', 'yatsi': '20:11'}, {'date': '2024-03-03', 'hDate': '1445-08-22', 'imsak': '05:48', 'gunes': '07:25', 'ogle': '13:12', 'ikindi': '16:11', 'aksam': '18:48', 'yatsi': '20:13'}, {'date': '2024-03-04', 'hDate': '1445-08-23', 'imsak': '05:46', 'gunes': '07:23', 'ogle': '13:11', 'ikindi': '16:12', 'aksam': '18:50', 'yatsi': '20:14'}, {'date': '2024-03-05', 'hDate': '1445-08-24', 'imsak': '05:44', 'gunes': '07:21', 'ogle': '13:11', 'ikindi': '16:13', 'aksam': '18:52', 'yatsi': '20:16'}, {'date': '2024-03-06', 'hDate': '1445-08-25', 'imsak': '05:42', 'gunes': '07:19', 'ogle': '13:11', 'ikindi': '16:14', 'aksam': '18:53', 'yatsi': '20:17'}]
        return data


def refetch_time():
    current_time = datetime.now().time().strftime('%H:%M:%S')
    target_time = '01:00:00'
    target_time1 = '10:00:00'
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
        pygame.time.Clock().tick(10000)


def ezan(is_nv: bool = False):
    if not is_nv:
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

    else:
        data = fetch_data_nv()
        current_date = datetime.now().strftime('%Y-%m-%d')
        today_object = next((obj for obj in data if obj['date'] == current_date), None)
        print('%s - Prayer times : %s', datetime.now(), today_object)

        while 1:
            if refetch_time():
                data = fetch_data_nv()
                current_date = datetime.now().strftime('%Y-%m-%d')
                today_object = next((obj for obj in data if obj['date'] == current_date), None)
                print('%s - Prayer times : %s', datetime.now(), today_object)

            if data:
                current_date = datetime.now().strftime('%Y-%m-%d')
                current_time = datetime.now().strftime('%H:%M')
                today_object = next((obj for obj in data if obj['date'] == current_date), None)
                if today_object:
                    # Check if the current time is within the schedule for the current date
                    if current_time == today_object['imsak']:
                        folder_path = '/home/ismail/namaz-vakti/sabah/'
                        files_in_folder = get_files_from_folder(folder_path)

                        # Play a randomly selected audio file
                        random_file = random.choice(files_in_folder)
                        print("%s - Playing Sabah Ezan: %s", current_time, random_file)
                        play_mp3(f"/home/ismail/namaz-vakti/sabah/{random_file}")

                    elif current_time == today_object['gunes']:
                        folder_path = '/home/ismail/namaz-vakti/bird/'
                        files_in_folder = get_files_from_folder(folder_path)

                        # Play a randomly selected audio file
                        random_file = random.choice(files_in_folder)
                        print("%s - Playing bird sound: %s", current_time, random_file)
                        play_mp3(f"/home/ismail/namaz-vakti/bird/{random_file}")

                    elif current_time in [today_object['ogle'], today_object['ikindi'], today_object['aksam'], today_object['yatsi']]:
                        folder_path = '/home/ismail/namaz-vakti/ezan/'
                        files_in_folder = get_files_from_folder(folder_path)

                        # Play a randomly selected audio file
                        random_file = random.choice(files_in_folder)
                        print("%s - Playing Ezan: %s", current_time, random_file)
                        play_mp3(f"/home/ismail/namaz-vakti/ezan/{random_file}")

ezan(True)
