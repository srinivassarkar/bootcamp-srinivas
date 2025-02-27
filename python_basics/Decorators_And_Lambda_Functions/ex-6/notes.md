# Python Access Control Decorator Example

<div class="content">

## Problem Approach

This Python code defines a decorator called `role_required` that restricts access to a function based on the user's role. The decorator is applied to the `delete_user` function to demonstrate its functionality.

### Why?

Access control decorators are useful for enforcing security measures in applications. They help ensure that only users with the appropriate permissions can execute certain functions, thereby protecting sensitive operations.

### What?

The `role_required` decorator checks the user's role before allowing access to the `delete_user` function. If the user's role does not match the required role, access is denied.

### How?

The decorator is defined as a function that takes a role as an argument, which returns another function (the actual decorator). This inner function wraps the original function and adds the access control behavior.

</div>

## Python Code

<pre>def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                print("Access Denied!")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user_id):
    print(f"User  {user_id} deleted!")

# Example Usage
delete_user("admin", 42)  # Access granted
delete_user("guest", 42)   # Access denied
    </pre>

<div class="note">**Note:** This code demonstrates how to implement an access control decorator in Python to restrict function execution based on user roles, enhancing security in applications.</div>
