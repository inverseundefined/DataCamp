'''
Normalizing reviews
It's time to extract some important words present in your movie review dataset. First, you need to normalize them and then, count their frequency. Part of the normalization implies converting all the words to lowercase, removing special characters and extracting the root of a word so you count the variants as one.

So imagine you have the following reviews: The movie surprises me very much and Marvel movies always surprise their audience. If you count the word frequency, you will count surprises one time and surprise one time. However, the verb surprise appears in both and its frequency should be two.

The text of a movie review for only one example has been already saved in the variable movie. You can use print(movie) to view the variable in the IPython Shell.

Instructions 1/4
25 XP
Convert the string in the variable movie to lowercase. Print the result.
Remove the $ that occur at the start and at the end of the string contained in movie_lower. Print the results.
Split the string contained in movie_no_space into as much substrings as possible. Print the results.
To get the root of the second word contained in movie_split, select all the characters except the last one.
'''
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove whitespaces and print the result
movie_no_space = movie_lower.strip("$")
print(movie_no_space)

# Split the string into substrings and print the result
movie_split = movie_no_space.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][:-1]
print(word_root)