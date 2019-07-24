'''
Calling by its name
You have created your database with the tools and the different Data Science subfields they are used in. The company is considering creating courses using these tools and sending personalized emails to the users recommending the different topics. They have asked you to make this process more time-efficient. To do this, you want to create a template email with a standard message changing the different tools and corresponding field name.

First, you want to try doing this with just one example as a proof of concept. You use positional formatting and named placeholders to call the variables in a dictionary.

The variable courses containing one tool and one field name has been saved. You can use print(courses) to view the variable in the IPython Shell.

Create a dictionary assigning the first and second element appearing in the list courses to the keys "field" and "tool" respectively.
Complete the string with placeholders accessing inside to the elements associated with the keys field and tool in the dictionary plan.
Print out the resulting message using the .format() method passing the plan dictionary to replace the placeholders.
'''
# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Define string with placeholders
my_message = "If you are interested in {plan[field]}, you can take the course related to {plan[tool]}"

# Use dictionary to replace placehoders
print(my_message.format(plan=plan))
