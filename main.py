import csv #lets us read csv files
#import os geodist

# All code will be on one file for now, will split each functions into modules later when I can get everything working here

PS_filename = 'postcodes.csv'
crime_folder = 'Devon_and_Cornwall_crime_data_2020'

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

    #with open()
        #assert radius in accept_radius, "Please enter a radius of 1, 2 or 5 (in km)"

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


# For future use
# dir = os.path.relpath('.\\Devon_and_Cornwall_crime_data_2020\\2020-01-devon-and-cornwall-street.csv')
# with open(dir, 'r') as f:
#     read = csv.reader(f)
#
#     for i in read:
#         print(i)