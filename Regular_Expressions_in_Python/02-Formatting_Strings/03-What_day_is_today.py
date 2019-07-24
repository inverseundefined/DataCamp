'''
What day is today?
It's lunch time and you are talking with some of your colleagues. They comment that they feel that every morning someone should send them a reminder of what day it is so they can check in the calendar what their assignments are for that day.

You want to help out and decide to write a small script that takes the date and time of the day so that every morning, a message is sent to your colleagues. You remember that you can use the module datetime along with named placeholders to achieve your goal.

The date should be expressed as April 16, 2019 and the time as 16:30.

You can use the IPython Shell to explore the module datetime.

Instructions
100 XP
Import the function datetime from the module datetime .
Obtain the date of today and assign it to the variable get_date.
Complete the string message by adding placeholders named today and the format specifiers to format the date and time as shown in the text.
Print the message using the .format() method and the variable get_date to replace the named placeholders.
Take Hint (-30 XP)
'''
# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date))