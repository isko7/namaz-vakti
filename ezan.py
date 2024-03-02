import requests
import time
from datetime import datetime, timedelta
import os
import random
import pygame
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler('/home/ismail/namaz-vakti/ezan_logs.log', 'a'))
print = logger.info


def authentication():
    access_token, refresh_token = None, None

    url = 'https://awqatsalah.diyanet.gov.tr/Auth/Login'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {
        'email': 'ikilinc07@gmail.com',
        'password': '8R!ex-2Q'
    }
    response = requests.post(url, headers=headers, json=data)
    print("%s - Authentication - Status code: %s", datetime.now(), response.status_code)

    if response.ok:
        json_response = response.json()
        access_token = json_response['data']['accessToken']

    return access_token


def fetch_data():
    # country_code = 21 # France
    # state_code = 704 # France
    # city_code = 13062 # Chateaudun
    access_token = authentication()
    url = 'https://awqatsalah.diyanet.gov.tr/api/PrayerTime/Daily/13062'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + access_token,
    }
    response = requests.get(url, headers=headers)
    print("%s - Fetch data - Status code: %s", datetime.now(), response.status_code)

    if response.ok:
        json_response = response.json()
        data = json_response['data'][0]
        print("%s - Fetched Data - Imsak: %s - Günes: %s - Ogle: %s - Ikindi: %s - Aksam: %s - Yatsi: %s", datetime.now(), data['fajr'], data['sunrise'], data['dhuhr'], data['asr'], data['maghrib'], data['isha'])
    else:
        data = {
            "shapeMoonUrl": "http://namazvakti.diyanet.gov.tr/images/i6.gif",
            "fajr": "06:07",
            "sunrise": "07:44",
            "dhuhr": "13:13",
            "asr": "15:59",
            "maghrib": "18:33",
            "isha": "19:58",
            "astronomicalSunset": "18:26",
            "astronomicalSunrise": "07:51",
            "hijriDateShort": "12.8.1445",
            "hijriDateShortIso8601": None,
            "hijriDateLong": "12 Şaban 1445",
            "hijriDateLongIso8601": None,
            "qiblaTime": "08:56",
            "gregorianDateShort": "22.02.2024",
            "gregorianDateShortIso8601": "22.02.2024",
            "gregorianDateLong": "22 Şubat 2024 Perşembe",
            "gregorianDateLongIso8601": "2024-02-22T00:00:00.0000000+03:00",
            "greenwichMeanTimeZone": 1
        }
        print("%s - Default Data - Imsak: %s - Günes: %s - Ogle: %s - Ikindi: %s - Aksam: %s - Yatsi: %s", datetime.now(), data['fajr'], data['sunrise'], data['dhuhr'], data['asr'], data['maghrib'], data['isha'])

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
        print("%s - Error reading folder: %s", datetime.now(), e)
        return []


def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)

    pygame.mixer.music.play()

    # Wait until the ezan has finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(20000)


def choose_play_ezan_file(folder_path, index, vakit):
    files_in_folder = get_files_from_folder(folder_path)
    # Sort files_in_folder alphabetically
    files_in_folder.sort()
    # Create play_order list from files_in_folder
    play_order = [os.path.join(folder_path, file_name) for file_name in files_in_folder]

    file_name = play_order[index]
    file_path = os.path.join(folder_path, file_name)
    print("%s - Playing %s Ezan: %s - index: %s", datetime.now(), vakit, file_name, index)
    play_mp3(file_path)

    return len(play_order)


def alert_time(time, minutes):
    data_time = datetime.strptime(time, "%H:%M").time()
    # Subtract X minutes from the data time
    converted_data_time = (datetime.combine(datetime.today(), data_time) - timedelta(minutes=minutes)).time()
    formatted_time = converted_data_time.strftime("%H:%M")
    return formatted_time


def ezan():
    data = fetch_data()

    imsak_index = 0
    aksam_index = 0
    ezan_index = 0

    while 1:
        if refetch_time():
            data = fetch_data()
            time.sleep(60)

        if data:
            current_time = datetime.now().strftime('%H:%M')
            fajr_10 = alert_time(data['fajr'], 10)
            fajr_45 = alert_time(data['fajr'], 45)
            dhuhr_10 = alert_time(data['dhuhr'], 10)
            dhuhr_45 = alert_time(data['dhuhr'], 45)
            asr_10 = alert_time(data['asr'], 10)
            asr_45 = alert_time(data['asr'], 45)
            maghrib_10 = alert_time(data['maghrib'], 10)
            maghrib_45 = alert_time(data['maghrib'], 45)
            isha_10 = alert_time(data['isha'], 10)
            isha_45 = alert_time(data['isha'], 45)

            # Check if the current time is within the schedule for the current date
            if current_time == data['fajr']:
                folder_path = '/home/ismail/namaz-vakti/sabah/'
                imsak_ezan = choose_play_ezan_file(folder_path, imsak_index, 'Imsak')
                imsak_index = imsak_index + 1
                if imsak_index >= imsak_ezan:
                    imsak_index = 0

            elif current_time == data['sunrise']:
                folder_path = '/home/ismail/namaz-vakti/bird/'
                files_in_folder = get_files_from_folder(folder_path)
                # Play a randomly selected audio file
                random_file = random.choice(files_in_folder)
                print("%s - Playing bird sound: %s", datetime.now(), random_file)
                play_mp3(f"/home/ismail/namaz-vakti/bird/{random_file}")
                play_mp3(f"/home/ismail/namaz-vakti/bird/{random_file}")
                play_mp3(f"/home/ismail/namaz-vakti/bird/{random_file}")
                time.sleep(60)

            elif current_time == data['maghrib']:
                folder_path = '/home/ismail/namaz-vakti/aksam/'
                aksam_ezan = choose_play_ezan_file(folder_path, aksam_index, 'Aksam')
                aksam_index = aksam_index + 1
                if aksam_index >= aksam_ezan:
                    aksam_index = 0

            elif current_time == data['dhuhr']:
                folder_path = '/home/ismail/namaz-vakti/ezan/'
                ogle_ezan = choose_play_ezan_file(folder_path, ezan_index, 'Ogle')
                ezan_index = ezan_index + 1
                if ezan_index >= ogle_ezan:
                    ezan_index = 0

            elif current_time == data['asr']:
                folder_path = '/home/ismail/namaz-vakti/ezan/'
                ikindi_ezan = choose_play_ezan_file(folder_path, ezan_index, 'Ikindi')
                ezan_index = ezan_index + 1
                if ezan_index >= ikindi_ezan:
                    ezan_index = 0

            elif current_time == data['isha']:
                folder_path = '/home/ismail/namaz-vakti/ezan/'
                yatsi_ezan = choose_play_ezan_file(folder_path, ezan_index, 'Yatsi')
                ezan_index = ezan_index + 1
                if ezan_index >= yatsi_ezan:
                    ezan_index = 0

            elif current_time == fajr_10 or current_time == dhuhr_10 or current_time == asr_10 or current_time == maghrib_10 or current_time == isha_10:
                folder_path = '/home/ismail/namaz-vakti/alert10/'
                files_in_folder = get_files_from_folder(folder_path)
                # Play a randomly selected audio file
                random_file = random.choice(files_in_folder)
                print("%s - Playing Alert 10min sound: %s", datetime.now(), random_file)
                play_mp3(f"/home/ismail/namaz-vakti/alert10/{random_file}")
                time.sleep(60)

            elif current_time == fajr_45 or current_time == dhuhr_45 or current_time == asr_45 or current_time == maghrib_45 or current_time == isha_45:
                folder_path = '/home/ismail/namaz-vakti/alert45/'
                files_in_folder = get_files_from_folder(folder_path)
                # Play a randomly selected audio file
                random_file = random.choice(files_in_folder)
                print("%s - Playing Alert 45min sound: %s", datetime.now(), random_file)
                play_mp3(f"/home/ismail/namaz-vakti/alert45/{random_file}")
                time.sleep(60)

ezan()