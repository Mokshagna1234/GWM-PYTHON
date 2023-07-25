from playsound import playsound
import time

def play_alarm_sound():
    alarm_sound_path = 'alarm-clock.mp3'        #path to alarm sound file
    playsound(alarm_sound_path)

def set_alarm(alarm_time):
    try:
        alarm_time_obj = time.strptime(alarm_time, '%H:%M')
    except ValueError:
        print("Invalid time format. Please use the HH:MM format.")
        return

    while True:
        current_time = time.strftime('%H:%M')
        if current_time == alarm_time:
            print("Wake up Dude!")
            play_alarm_sound()
            break
        

if __name__ == "__main__":
    alarm_time = input("Enter the time for the alarm (HH:MM format):")

    set_alarm(alarm_time)
