# Importing required modules
import os
import datetime

try:
    from variables import error_folder, dynamic_filename
except ImportError:
    error_folder = "default_error_folder"
    dynamic_filename = "default_dynamic_filename.txt"


# Function for creating new folder
def create_folder(folder_name):
    """Creates a folder if it doesn't exist."""
    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
            return True
        except Exception as e:
            print(f"Error creating folder '{folder_name}': {e}")
            return False
    else:
        print(f"Folder '{folder_name}' already exists.")
        return False


# Function for submitting error
def submit_error(error_text):
    """Handles error submission by creating the error folder."""
    if create_folder(error_folder):
        # Additional logic for submitting the error (e.g., writing to a log file)
        pass


# Function for creating dynamic file
def create_file_dynamic(file=dynamic_filename):
    """Creates a dynamic file with the current timestamp."""
    try:
        with open(file, "w") as f:
            string = f"Created on {get_full_datetime()}\n"
            f.write(string)
        print(f"File '{file}' created successfully.")
        return file
    except Exception as e:
        print(f"Error creating file '{file}': {e}")
        return None


# Function for appending into file
def append_file(file_name, data):
    """Appends data to the file with a timestamp."""
    try:
        with open(file_name, "a") as f:
            my_data = f"{get_datetime()}\n" \
                      f"------------------------------\n" \
                      f"{data}\n" \
                      f"_______________________________\n\n\n\n"
            f.write(my_data)
        print(f"Data appended to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error appending data to '{file_name}': {e}")


# To calculate short DateTime
def get_datetime():
    """Returns a short-form datetime string."""
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y, %I:%M:%S:%f %p")[:19]  # Trim to match desired format


# To calculate long DateTime
def get_full_datetime():
    """Returns a long-form datetime string."""
    now = datetime.datetime.now()
    return now.strftime("%A, %d %B %Y, %I:%M:%S:%f %p -- %j th Day & %U th Week")[:64]  # Format for long datetime


# Example Usage:
if __name__ == "__main__":
    create_folder(error_folder)  # Creating the error folder
    file = create_file_dynamic()  # Creating a dynamic file with timestamp
    append_file(file, "This is some new clipboard data.")  # Appending some data to the file
