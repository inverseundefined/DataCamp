'''
Flying home
Your boss assigned you to a small project. They are performing an analysis of the travels people made to attend business meetings. You are given a dataset with only the email subjects for each of the people traveling.

You learn that the text followed a pattern. Here is an example:

Here you have your boarding pass LA4214 AER-CDB 06NOV.

You need to extract the last part:

The two letters indicate the airline (e.g LA),
The 4 numbers are the flight number (e.g. 4214).
The three letters correspond to the departure (e.g AER),
The destination (CDB),
The date (06NOV) of the flight.
All letters are always uppercase.

The variable flight containing one email subject was loaded in your session. You can use print() to view it in the IPython Shell.

Import the re module.
Complete the regular expression to match and capture all the flight information required. Only the first parenthesis were placed for you.
Find all the matches corresponding to each piece of information about the flight. Assign it to flight_matches.
Complete the format method with the elements contained in flight_matches. In the first line print the airline,and the flight number. In the second line, the departure and destination. In the third line, the date.
'''

# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)
    
#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))