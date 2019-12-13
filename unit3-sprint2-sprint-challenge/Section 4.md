### In the Northwind database, what is the type of relationship between the "Employee" and "Territory" tables?

A many-to-one table is a table that has many values for many each key. Looking at the database layout, 
you can see that there is one territory id for each employee id. Given that, I'd say their relationship
is many-to-one. 


### What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

MongoDB is what's called a NoSQL database, meaning that it enforces no schema and that it will store
raw documents. That means it's more flexible, but also more work. So, it would be suitable when the client
needs to hold a lot of arbitrary data. However, it's not suitable if they need to store data that will reliably
give you typed results every time such as a data structure. It is of note that you can provide that structure 
yourself, but because the database doesn't enforce it, you're a lot more error-prone. 


### What is "NewSQL", and what is it trying to achieve?
For some context, SQL is a structured, schema-enforced database that uses data tables and relations,
and adheres to ACID standards. It has some key drawbacks such as rigidity, inefficient use of storage,
and computationally expensive changes. All of these compound to make it not suitable for Big Data.

Looking to fix these issues, NoSQL was born of the desire to have flexible, scalable databases. 
Its key features are a lack of schemas, auto-balancing of server loads, and improved reliability. However,
it suffers from its own drawbacks such as a lack of consistency, no way to analyze the data since there's no 
model, and worse security. 

Enter NewSQL, an attempt to solve the problems of both systems. It has relational models, adheres to ACID,
carries support for SQL, allows both horizontal and vertical scaling, has efficient query handling, and supports
distributed databases. 



