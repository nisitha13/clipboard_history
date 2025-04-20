#!/usr/bin/env python3.8
import sys
from os.path import dirname, abspath
sys.path.append(dirname(abspath(__file__)))

from utils.functions import create_folder, create_file_dynamic, append_file
import clipboard
from os import chdir
from time import sleep
from variables import folder, limit

try:
    create_folder(folder)
    chdir(folder)
    
    while True:
        file = create_file_dynamic()
        previous = ""
        count = 0
        
        while count <= limit:
            try:
                data = clipboard.paste()  # Access the clipboard data
                if data != previous:  # Check if clipboard content has changed
                    append_file(file, data)  # Append new data to file
                    previous = data  # Update the previous clipboard data
                    count += 1  # Increment count for each unique data entry
                else:
                    sleep(0.2)  # Wait before checking again if no change
                
            except Exception as e:
                print(f"Error reading clipboard: {e}")
                sleep(1)  # Sleep for 1 second before retrying
            
except Exception as e:
    print(f"Error with folder creation or file operations: {e}")
