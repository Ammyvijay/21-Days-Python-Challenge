"""
Note : Static methods in Python are methods that belong to a class, rather than an instance of the class. They can be called on the class itself. Neither self (the object instance) nor cls (the class) are implicitly passed as the first argument. They behave like plain functions.

This can be useful in situations where we don't need to store any state information for a method and can improve code readability and organization
"""

import re

class DataValidator:

    @staticmethod
    def is_valid_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+",email):
            return True
        else:
            return False
        
email_address = "john.doe@example.com"
is_valid = DataValidator.is_valid_email(email_address)
print(is_valid)