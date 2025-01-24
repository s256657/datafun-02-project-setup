"""
Module: wilcox_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Craig Wilcox

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
import pathlib
import time

# Import local modules
# TODO: Change this to import your module and uncomment
# import case_utils 
import utils_wilcox

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # TODO: Implement the actual folder creation logic
    for year in range(start_year, end_year +1):
        year_folder = data_path.joinpath(str(year))
        year_folder.mkdir(exist_ok=True)
        print(f"Created folder: {year_folder}")
        

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase=False, remove_spaces=False) -> None:
    # TODO: Add docstring
    '''Create folders from a list of folder names in years
    Argument:
    folder_list -- list of folder names
    to_lowercase -- is converting folder names to lowercase necessary
    remove_spaces -- is removing spces from folder names necessary'''
    # TODO: Log the function call and its arguments
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "")
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")

    # TODO: Implement this function and remove the temporary pass
    print(f"created folder: {folder_path}")

  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix='{prefix}'")
    prefixed_folders = [f"{prefix}{folder_name}" for folder_name in folder_list]
    for folder_name in prefixed_folders:
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")


#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    print(f"FUNCTION CALLED: create_folders_periodically with duration_seconds={duration_seconds}")
    for i in range(5):
        folder_name = f"folder{i+1}"
        folder_path = data_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")
        time.sleep(duration_seconds)


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    # print(f"Byline: {case_utils.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    # create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.