import csv #lets us read csv files
import os, geodist

# All code will be on one file for now, will split each function into modules later when I can get everything working here

PS_filename = 'postcodes.csv'
crime_folder = '/Devon_and_Cornwall_crime_data_2020/'

def get_crime(user_postcode):
    """ This function retrives all repoerted street level within a radius of the centre coordinate """
    accepted = False
    # This while loopr repeats until user types a radius of 1, 2 or 5 (as stated in the pdf)
    while accepted == False:
        radius = int(input("Please enter an integer to search for crimes within that radius"))
        accept_radius = [1, 2, 5]
        if radius in accept_radius:
            print(f"Accepted radius = {radius}")
            accepted = True

    #TODO Test for if file exists etc. Tests

    # Retrieving all repoerte street level crime. It is not sorted yet. Neither is it confined to the allowed radius. It just prints everything for now.
    #Finding our current directory and the directory with crime data
    cur_path = os.path.dirname(__file__)
    target_path = cur_path + crime_folder
    exists = os.path.isdir(target_path)

    # If target path exsits, loop through each file in the directory
    if exists: # Aka if exists == True
        for root,dirs,files in os.walk(target_path):
            for file in files:
                #Making a variable to open each csv. Using the path and the file name
                access_file = target_path + file
                print(access_file)

                #Now, we are openning the file.
                with open(access_file, 'r') as cur_file:
                    csv_reader = csv.reader(cur_file)
                    next(csv_reader)

                    for line in csv_reader:
                        print(line)
                    #print(cur_file)
                    #  perform calculation


def get_coordinates(user_postcode):
    """This function retrieves the centre coordinates (latitude or longitude) of a postcode"""
    #TODO Try and except needed for postcode validation

    # reading csv file. Using context manager (with open)
    with open(PS_filename, 'r') as postcode_csv:
        #using the reader method to read csv file. Pass file into method.
        csv_reader = csv.reader(postcode_csv)

        # next: steps over a value in an iterable.
        next(csv_reader) #Loops over first line (which is just Postcode)

        #Iterating trhough file. Remember, we are starting from our second value (to ignore table headers).
        #Each row becomes a list. Line[0] is the first column that holds the postcode for each row.
        for line in csv_reader:
            if line[0] == user_postcode:
                latitude, longitude = line[-2], line[-1] #list[-1] and line[-1] takes the last 2 values in a list. Which is conviniently the longitude and latitude
                print(f"Latitude: {latitude}, Longitude {longitude}")

                return latitude, longitude    #When this is split into modules, this variable will be useful.
    # Do you need to close "with open" files?!


def menu():
    """This function acts as the CLI """
    #TODO there should be a menu with welcome message, help/menu, quit, option to start program -> then enter postcode.
    #TODO whenever program prompt for user input, it must always accept the options of quit and restart.

    while True:
        #Todo Display menu!
        #User enters postcode
        postcode = input("Please enter a Postcode")
        #TODO validate postcode.

        get_coordinates(postcode)

        get_crime(postcode)

menu()

