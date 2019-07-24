'''
Put it in order!
Your company is analyzing the best way to provide users with different online courses. Your job is to scrape Wikipedia pages searching for tools used in Data Science subfields. You'll store the tool and field name in a database. After a text analysis, you realize that the information is provided in a specific position of the text but sometimes the field name is given first and the tool after that, while in other cases it's the other way around.

You decide to use positional formatting to handle these situations because it provides a way to reorder placeholders.

The text of one article has already been saved in the variable wikipedia_article. Also, the empty list my_list is already defined. You can use print() to view the variable in the IPython Shell.

Assign the substrings going from the 4th to the 19th character, and from the 22nd to the 44th character of wikipedia_article to the variables first_pos and second_pos, respectively. Adjust the strings so they are lowercase.
Define a string with the text "The tool is used in" adding placeholders after the word tool and the word in for future positional formatting. Append it to the list my_list.
Define a string with the text "The tool is used in" adding placeholders after the word tool and in but reorder them so the second argument passed to the method will replace the first placeholder. Append to the list my_list.
Complete the for-loop so that it uses the .format() method and the variables first_pos and second_pos to print out every string in my_list.
'''

# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))