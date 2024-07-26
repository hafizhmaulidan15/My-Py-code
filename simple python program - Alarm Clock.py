""" Program python sederhana - Alarm Clock
----------------------------------------
"""
import datetime
import os
import time
import random
import webbrowser
# Jika video URL tidak ada, maka buatlah yang baru dengan script di bawah ini
if not os.path.isfile("youtube_alarm_videos.txt"):
    print('Creating "youtube_alarm_videos.txt"...')
    with open("youtube_alarm_videos.txt", "w") as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=HQaCF2F_MRo")
def check_alarm_input(alarm_time):
    """Memeriksa apakah user telah memasukkan waktu alarm yang valid"""
    if len(alarm_time) == 1: # [Hour] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: # [Hour:Minute] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0 and \
           alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False
# User input untuk waktu alarm
print("Set waktu alarm (Contoh 06:30 or 18:30:00)")
while True:
    alarm_input = input(">> ")
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Masukkan format waktu dengan HH:MM atau HH:MM:SS")
# Konversi waktu alarm dari [H:M] atau [H:M:S] ke dalam detik
seconds_hms = [3600, 60, 1] # Jumlah detik dalam jam, menit dan detik
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
#Waktu hari ini dalam detik
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
# Hitung jumlah detik hingga alarm berhenti
time_diff_seconds = alarm_seconds - current_time_seconds
# Jika perbedaan waktunya adalah negatif, set alarm untuk hari selanjutnya
if time_diff_seconds < 0:
    time_diff_seconds += 86400 # jumlah detik dalam satu hari
# Tampilkan jumlah waktu hingga alarm berbunyi
print("Alarm akan berbunyi dalam %s" % datetime.timedelta(seconds=time_diff_seconds))
# Sleep mode hingga alarm berbunyi
time.sleep(time_diff_seconds)
# Waktu alarm berbunyi
print("Ayo bangun!")
# Load daftar video URL
with open("youtube_alarm_videos.txt", "r") as alarm_file:
    videos = alarm_file.readlines()
# Buka random video dari list
webbrowser.open(random.choice(videos))