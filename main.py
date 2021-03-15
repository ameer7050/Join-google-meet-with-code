import webbrowser
import time

code = input('Google meet code: ')
print("Joining...")
webbrowser.open('https://meet.google.com/' + code)
time.sleep(30)