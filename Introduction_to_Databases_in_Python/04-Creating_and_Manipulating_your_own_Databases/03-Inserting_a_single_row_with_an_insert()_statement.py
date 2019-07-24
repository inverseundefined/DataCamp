'''
Inserting a single row with an insert() statement
There are several ways to perform an insert with SQLAlchemy; however, we are going to focus on the one that follows the same pattern as the select statement.

It uses an insert statement where you specify the table as an argument, and supply the data you wish to insert into the value via the .values() method as keyword arguments.

Here, the name of the table is data.

Instructions
100 XP
Instructions
100 XP
Import insert and select from the sqlalchemy module.
Build an insert statement for the data table to set name to 'Anna', count to 1, amount to 1000.00, and valid to True. Save the statement as insert_stmt.
Execute insert_stmt with the connection and store the results.
Print the rowcount attribute of results to see how many records were inserted.
Build a select statement to query for the record with the name of 'Anna'.
Hit 'Submit Answer' to print the results of executing the select statement.
Take Hint (-30 XP)
'''
# Import insert and select from sqlalchemy
from sqlalchemy import insert, select

# Build an insert statement to insert a record into the data table: insert_stmt
insert_stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)

# Execute the insert statement via the connection: results
results = connection.execute(insert_stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert: select_stmt
select_stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(connection.execute(select_stmt).first())
