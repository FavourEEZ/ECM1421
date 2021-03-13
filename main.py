import csv,os, time  #csv lets us read csv files. os lets us execute files in our directory easily. Time allows us to use time/date in our program
from geodist import distance

# All code will be on one file for now, will split each function into modules later when I can get everything working here
#TODO Do testing for geodist.py
#TODO Assert statements & More try & except

PS_filename = 'postcodes.csv'
crime_folder = '/Devon_and_Cornwall_crime_data_2020/'

def write_distance(sorted_data, filename):
    """This function creates (writes to) a new user defined file"""
    header = ["Crime ID", "Month", "Reported by", "Falls within", "Longitude", "Latitude", "Location", "LSOA code", "LSOA name", "Crime type", "Last outcome category", "Context", "Distance"]
    # Write Values to file
    filename = filename+".csv"
    try:
        with open(filename, 'w', newline="") as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(header)
            csv_writer.writerows(sorted_data)
            print("A new file has been created!")
    except:
        print("An error occured while opening the file. Please check if the file is opened else")


def get_crime(coordinate, user_choice):
    """ This function retrives all reported street level within a radius of the centre coordinate """
    sort_radius = []
    accepted = False
    # This while loop repeats until user types a radius of 1, 2 or 5 (as stated in the pdf)
    while accepted == False:
        #TODO Add, restart, quit function
        radius = int(input("Please enter an integer to search for crimes (Either 1, 2 or 5km): "))
        accept_radius = [1, 2, 5]
        if radius in accept_radius:
            print(f"Accepted radius = {radius}")
            accepted = True
        else:
            print(f"{radius} IS NOT ACCEPTED. Please try 1, 2 or 5km")

    #Finding our current directory and the directory with crime data
    cur_path = os.path.dirname(__file__)
    target_path = cur_path + crime_folder
    exists = os.path.isdir(target_path)

    # If target path exists, loop through each file in the directory
    if exists: # Aka if exists == True
        for root,dirs,files in os.walk(target_path):
            for file in files:
                #Making a variable to open each csv. Using the path and the file name
                access_file = target_path + file
                print(access_file)

                #TODO pass the input choice here and do your ifs and elifs. Then create a function for each type of retrieval.
                #TODO Only open csv files!
                #Now, we are opening the file.
                with open(access_file, 'r') as cur_file:
                    csv_reader = csv.reader(cur_file)
                    next(csv_reader)

                    for line in csv_reader:
                        crime_latitude, crime_longitude = line[5], line[4]
                        try:
                            current_crime_location = (float(crime_latitude), float(crime_longitude)) #Creating a tuple to be able to call geodist.py function

                            # Calling geodist method to retrieve the distance between the person's postcode and the postcode of each crime occurence.
                            #Geodist (local) module returns d. D is the distance between the postcode the user entered and the postcode in each csv file.
                            d = distance(coordinate, current_crime_location)
                            if d <= radius:
                                line.append(d)
                                sort_radius.append(line) #Adding this each returned line from the csv into an array so we can sort it. This makes a 2D array.
                        except:
                            pass
            sort_radius = sorted(sort_radius, key=lambda sorted_radius:sorted_radius[12])
            return sort_radius
    else:
        print("You don't seem to have the folder/files required to retrieve the crime")
        time.sleep(2) #Program waits 2 seconds then prints the next statement
        print("If you do, please make a folder called: '/Devon_and_Cornwall_crime_data_2020/' and only put the crime csv data files there")
        menu()

def get_coordinates(user_postcode):
    """This function retrieves the centre coordinates (latitude or longitude) of a postcode"""

    # reading csv file. Using context manager (with open)
    with open(PS_filename, 'r') as postcode_csv:
        #using the reader method to read csv file. Pass file into method.
        csv_reader = csv.reader(postcode_csv)

        # next: steps over a value in an iterable.
        next(csv_reader) #Loops over first line (which is just Postcode)

        #Iterating trhough file. Remember, we are starting from our second value (to ignore table headers).
        #Each row becomes a list. Line[0] is the first column that holds the postcode for each row.
        #TODO Instead of hardcode header, just import (When I've split up modules
        for line in csv_reader:
            if line[0] == user_postcode:
                latitude, longitude = line[-2], line[-1] #list[-1] and line[-1] takes the last 2 values in a list. Which is conviniently the longitude and latitude
                print(f"Latitude: {latitude}, Longitude {longitude}")
                location = (float(latitude), float(longitude))

                return location


def menu():
    """This function acts as the CLI """
    #TODO there should be a menu with welcome message, help/menu, quit, option to start program -> then enter postcode.
    #TODO whenever program prompt for user input, it must always accept the options of quit and restart.

    while True:
        #Menu: Distance, date, crime category
        #TODO Add restart, quit etc, Validate the number
        user_choice = input("""Hello, welcome to the Crime Data search tool.
How would you like the data sorted. Please enter the number you would like to select:
        1.Distance (nearest first)
        2.Date (most recent first)
        3.Crime Category 
            > """)

        #TODO validate postcode to exist in the file, add a space in the middle. Caps everuthing for user.
        postcode = input("Please enter a Postcode: ")
        coordinate = get_coordinates(postcode)

        #Sorting the data, then retrieving it
        sorted_data = get_crime(coordinate, user_choice)

        filename = input("What would you like to call your report? : ")
        write_distance(sorted_data, filename)


menu()

