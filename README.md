Required libraries to connect to docker mssql server with python

pip install -r requirements.txt

Since the test included a database with more than 20 thousand rows of data, a name filtering was done with SQL from the beginning.
After filtering by name, filtering studies were carried out with the pandas library using the table resulting from the existing filtering.

