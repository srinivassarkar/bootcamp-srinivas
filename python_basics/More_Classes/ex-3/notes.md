# Python Book Class with Static Variable Example

<div class="content">

## Problem Approach

This Python code defines a class called `Book` that represents a book with a title and an author. The class includes a static variable `num_books` to keep track of the total number of book instances created.

### Why?

Static variables (class variables) are useful for maintaining state that is shared across all instances of a class. In this case, it allows the class to keep track of how many books have been created without needing to store this information in each instance.

### What?

The `num_books` variable is incremented each time a new instance of the `Book` class is created. The class method `get_num_books` returns the current count of books.

### How?

The class method is defined using the `@classmethod` decorator, which allows it to access class variables. It takes `cls` as the first parameter, representing the class itself.

</div>

## Python Code

<pre>class Book:
    num_books = 0  # Static variable to track the number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.num_books += 1  # Increment the count

    @classmethod
    def get_num_books(cls):
        return cls.num_books

# Create instances of Book
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Get the number of books created
print(f"Total books created: {Book.get_num_books()}")  # Output: 2
    </pre>

<div class="note">**Note:** This code demonstrates how to use static variables and class methods in Python to track the number of instances created for a class, providing a way to maintain shared state across all instances.</div>
