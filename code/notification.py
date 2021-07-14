from plyer import notification
import time, webbrowser
total_breaks = 1
break_count = 0
while break_count<total_breaks:
    notification.notify(title = 'Lets Have a Break !!',
                    message = 'Close your eyes and feel the music. Take deep breath in and Breath Out for 10 times',
                    timeout = 6 )
    time.sleep(26)
    webbrowser.open("https://www.youtube.com/watch?v=SeNF90b4YT8")
    break_count = break_count + 1
    