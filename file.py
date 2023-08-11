# Import the necessary Java classes
from java.sql import Connection, DriverManager, ResultSet
from java.io import BufferedReader, FileReader
from java.lang import Class
from prettytable import PrettyTable

# Set up the JDBC connection parameters
db_url = "jdbc:oracle:thin:@your_database_host:your_port:your_service_name"
db_user = "your_username"
db_password = "your_password"

# Load the Oracle JDBC driver class
Class.forName("oracle.jdbc.OracleDriver")

# Create a connection to the database
connection = DriverManager.getConnection(db_url, db_user, db_password)

# Read the SQL file and execute the SELECT statement
sql_file_path = "/path/to/your/sql_file.sql"
sql_query = ""

with BufferedReader(FileReader(sql_file_path)) as reader:
    line = reader.readLine()
    while line is not None:
        sql_query += line
        line = reader.readLine()

# Execute the SQL query
statement = connection.createStatement()
result_set = statement.executeQuery(sql_query)

# Create a PrettyTable instance
table = PrettyTable()

# Get the column names from the ResultSet
metadata = result_set.getMetaData()
column_count = metadata.getColumnCount()
for i in range(1, column_count + 1):
    table.field_names.append(metadata.getColumnName(i))

# Populate the table with data
while result_set.next():
    row = []
    for i in range(1, column_count + 1):
        row.append(result_set.getString(i))
    table.add_row(row)

# Print the formatted table
print(table)

# Close resources
result_set.close()
statement.close()
connection.close()
