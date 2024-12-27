# Mention what command line can be used to load data into Django?
"""
To load data into a Django application, you typically use the loaddata command, which is part of Django's management commands. 
This command loads data from a fixture (a serialized file) into your database.
Command to load data:::

python manage.py loaddata <fixture_file>

Where <fixture_file> is the name of your fixture file (e.g., data.json, data.yaml, data.xml).

Example:
python manage.py loaddata data.json

"""
