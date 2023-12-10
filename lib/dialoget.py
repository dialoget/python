import sys
sys.path.append('../')
import os
#from functools import wraps
import functools
import csv
from datetime import datetime


# root path to the project
#ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH=''
LOG_FILE='log.csv'
ERROR_FILE='error.csv'
LOG_PATH = os.path.join(ROOT_PATH, LOG_FILE)
ERROR_PATH = os.path.join(ROOT_PATH, ERROR_FILE)

def dialoget(template, logs_path=''):
    USER_ERROR = os.path.abspath( os.path.join(logs_path,ERROR_PATH) )
    USER_LOGS = os.path.abspath( os.path.join(logs_path,LOG_PATH) )
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function argument names
            arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

            # Create a context dictionary that maps argument names to values
            context = dict(zip(arg_names, args))
            context.update(kwargs)

            # Check for undefined variables and log errors
            missing_vars = [name for name in arg_names if context.get(name) is None]
            if missing_vars:
                error_message = f"Warning: The following variables are undefined: {', '.join(missing_vars)}"
                log_to_csv(USER_ERROR, {'timestamp': datetime.now(), 'error': error_message})
                return None

            # Try to replace placeholders in the template with actual argument values
            try:
                filled_template = template.format(**context)
            except KeyError as e:
                error_message = f"Error: in function '{func.__name__}', variable {e} is not defined"
                log_to_csv(USER_ERROR, {'timestamp': datetime.now(), 'error': error_message})
                return None

            # Log the filled template string
            log_to_csv(USER_LOGS, {'timestamp': datetime.now(), 'message': filled_template})

            # Call the original function
            return func(*args, **kwargs)

        return wrapper
    return decorator

def log_to_csv(file_name, log_dict):
    # Write log message or error to a CSV file
    with open(file_name, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=log_dict.keys())
        if file.tell() == 0:  # Write header only if the file is empty
            writer.writeheader()
        writer.writerow(log_dict)


"""
def dialoget(template):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Assuming the function returns a dictionary of replacements
            replacements = func(*args, **kwargs)

            # Replace placeholders in the template with actual values
            filled_template = template.format(**replacements)

            # Print or use the filled template string
            print(filled_template)  # or you can return it, if needed

            # Return the result of the function, if it's necessary.
            return replacements

        return wrapper

    return decorator



# This is the decorator factory that accepts arguments
def dialoget2(sentence="Sentence"):
    # This is the actual decorator
    def decorator(func):
        call_count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            print(f"The sentence: {sentence} {func.__name__} has been called {call_count} times")
            return func(*args, **kwargs)

        return wrapper
    return decorator




# Usage example with decorator arguments

def nfunc(func):
    # This will hold the number of times the function has been called
    call_count = 0

    @wraps(func)  # Use this to preserve the original function's metadata
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"Function {func.__name__} has been called {call_count} times")
        return func(*args, **kwargs)

    return wrapper

"""