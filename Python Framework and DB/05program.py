# What is a QuerySet?Write program to create a new Post object in database:
"""
In Django's Object-Relational Mapper (ORM), a QuerySet represents a collection of objects from your database. It's not just a list of objects in memory; instead, it's a lazy representation of a database query. This means that the database is only queried when you actually need the data (e.g., when you iterate over the QuerySet, access its elements, or evaluate it in a context that requires the data).

=> Here are key characteristics of QuerySets:

- Lazy Evaluation: As mentioned, QuerySets are evaluated only when necessary. This optimizes performance, especially when dealing with large datasets.

- Chaining: You can chain multiple filter methods together to refine your query.

- Caching: Django caches the results of a QuerySet the first time it's evaluated. Subsequent uses of the same QuerySet (within the same request) will retrieve the data from the cache, avoiding further database queries.

- Methods: QuerySets provide a variety of methods for filtering, ordering, and manipulating data.


=> Common QuerySet methods:

filter(): Filters objects based on specified criteria.
exclude(): Excludes objects that match specified criteria.
order_by(): Orders the results by specified fields.
values(): Returns a QuerySet of dictionaries, rather than model instances.
all(): Returns all objects in the table.
get(): Returns a single object matching the criteria. Raises an exception if no object is found or multiple objects are found.
first(): Returns the first object in the QuerySet or None if the QuerySet is empty.
last(): Returns the last object in the QuerySet or None if the QuerySet is empty.
exists(): Returns True if the QuerySet contains any objects, False otherwise.
"""


# env3 program
