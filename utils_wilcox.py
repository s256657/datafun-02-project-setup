"""
Module: utils_wilcox

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Craig Wilcox

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True
is_publicly_traded: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 10
number_of_locations: int = 6

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.7
average_location_net_weekly_income: float = '$8,000'

# declare a list of strings
# TODO: Add or replace this with your own list  
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
tools_available: list = ["SQL", "GitHub", "Python"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
location_net_weekly_income: list = [6000, 9500, 7500, 8500, 6500, 10000]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(client_satisfaction_scores)  
min_weekly_location_income: float = min(location_net_weekly_income)
max_score: float = max(client_satisfaction_scores)  
max_weekly_location_income: float = max(location_net_weekly_income)
mean_score: float = statistics.mean(client_satisfaction_scores)  
mean_income: float = statistics.mean(location_net_weekly_income)
stdev_score: float = statistics.stdev(client_satisfaction_scores)
stdev_income: float = statistics.stdev(location_net_weekly_income)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Wilcox Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Is Publicly Traded:         {is_publicly_traded}
Years in Operation:         {years_in_operation}
Number of Locations:        {number_of_locations}
Skills Offered:             {skills_offered}
Tools Available:            {tools_available}
Client Satisfaction Scores: {client_satisfaction_scores}
Location Weekly Income in Dollars: {location_net_weekly_income}
Minimum Satisfaction Score:        {min_score}
Minimum Location Weekly Income:    ${min_weekly_location_income}
Maximum Satisfaction Score:        {max_score}
Maximum Location Weekly Income:    ${max_weekly_location_income}
Mean Satisfaction Score:           {mean_score:.2f}
Mean Weekly Income:                ${mean_income}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
Standard Deviation of Weekly Income:       ${stdev_income:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.