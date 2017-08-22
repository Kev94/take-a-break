# Opens youtube page after waiting ten seconds and prompts user to take three breaks

import time
import webbrowser

user_breaks = 0
total_breaks = 3
print "The current time is: " + time.ctime() + "\n"

while user_breaks != total_breaks:
    print "Take a break! \n"
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    user_breaks +=1
    print "You have taken " + str(user_breaks) + " break(s)\n"
print "All out of breaks!"
