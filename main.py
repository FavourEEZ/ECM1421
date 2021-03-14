import csv,os, time  #csv lets us read csv files. os lets us execute files in our directory easily. Time allows us to use time/date in our program
from geodist import distance

#TODO Do testing & Assert statements for geodist.py
#TODO Modularise all code
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
            print("A new file has been created!", "\n")
    except:
        print("An error occured while opening the file. Please check if the file is opened else")


def get_crime(coordinate, user_choice, radius):
    """ This function retrives all reported street level within a radius of the centre coordinate """
    sort_radius = []
    sort_date = []
    sort_category = []

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

                #TODO Only open csv files!
                #Now, we are opening the file.
                with open(access_file, 'r') as cur_file:
                    csv_reader = csv.reader(cur_file)
                    next(csv_reader)

                    for line in csv_reader:
                        crime_latitude, crime_longitude = line[5], line[4]
                        try:
                            current_crime_location = (float(crime_latitude), float(crime_longitude)) #Creating a tuple to be able to call geodist.py function
                            if user_choice == "1":
                                # Calling geodist method to retrieve the distance between the person's postcode and the postcode of each crime occurence.
                                #Geodist (local) module returns d. D is the distance between the postcode the user entered and the postcode in each csv file.
                                d = distance(coordinate, current_crime_location)
                                if d <= radius:
                                    line.append(d)
                                    sort_radius.append(line) #Adding this each returned line from the csv into an array so we can sort it. This makes a 2D array.

                            elif user_choice == "2":
                                #sort by date
                                d = distance(coordinate, current_crime_location)
                                if d <= radius:
                                    line.append(d)
                                    sort_date.append(line)

                            elif user_choice == "3":
                                d = distance(coordinate, current_crime_location)
                                if d <= radius:
                                    line.append(d)
                                    sort_category.append(line)
                        except:
                            pass
            if user_choice == "1":
                sort_radius = sorted(sort_radius, key=lambda sorted_radius:sorted_radius[12])
                return sort_radius
            elif user_choice == "2":
                return sort_date
            elif user_choice == "3":
                sort_category = sorted(sort_category, key=lambda row: row[9], reverse=True )
                return sort_category
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
        for line in csv_reader:
            if line[0] == user_postcode:
                latitude, longitude = line[-2], line[-1] #list[-1] and line[-1] takes the last 2 values in a list. Which is conviniently the longitude and latitude
                print(f"Latitude: {latitude}, Longitude {longitude}")
                location = (float(latitude), float(longitude))

                return location


def verify_postcode(postcode):
    """This function opens postcodes.csv and checks if the user entered postcode exists"""
    accepted = False
    accepted_list = []
    # This while loop repeats until user types a radius of 1, 2 or 5 (as stated in the pdf)

    while accepted == False:
        with open(PS_filename, 'r') as postcode_csv:
            #using the reader method to read csv file. Pass file into method.
            csv_reader = csv.reader(postcode_csv)
            next(csv_reader) #ignores the first line
            #Each row becomes a list. Line[0] is the first column that holds the postcode for each row.
            for line in csv_reader:
                if line[0] == postcode:
                    accepted_list.append(line[0])
                else: pass
        if postcode in accepted_list:
            return postcode
        else:
            print("***", postcode, "was not accepted. Please enter an accepted postcode in all caps and a space between incode 'DT1' and outcode '1AD'"
                            "\n" "Please try again" "\n")
            menu()


def menu():
    """This function acts as the CLI for the user"""
    while True:
        #Menu: Distance, date, crime category
        user_choice = input("\n" """Hello, welcome to the Crime Data search tool.
How would you like the data sorted. Please enter the number you would like to select:
        1.Distance (nearest first)
        2.Date (most recent first)
        3.Crime Category 
        4.restart - Restarts the program 
        5.quit - Ends the whole program
            > """)
        if user_choice == "1" or user_choice == "2" or user_choice == "3":
            print("Throughtout the program you can enter 'restart' or 'quit' when prompted to input")
            time.sleep(0.5)

            postcode = input("Please enter a Postcode > ")
            #Adding the quit and restart options for the user
            if postcode == "quit":
                print("Program has ended")
                user_choice = 5 #Assigning user_choice to 5 so that the elif to quit the program gets called.
                break
            elif postcode == "restart":
                menu()
            else: pass

            verified_postcode = verify_postcode(postcode) #Verifying the coordinates by
            coordinate = get_coordinates(verified_postcode)

            #Sorting the data, then retrieving it
            #Error Handling for radius. It includes 'restart' and 'quit' condition.
            accepted = False
            # This while loop repeats until user types a radius of 1, 2 or 5 (as stated in the pdf)
            while accepted == False:

                radius = input("Please enter an integer to search for crimes (Either 1, 2 or 5km): ")
                accept_radius = ["1", "2", "5"]
                if radius in accept_radius:
                    print(f"{radius} is accepted!")
                    accepted = True

                elif radius == "restart":
                    print("Radius restart")
                    menu()
                elif radius == "quit":
                    print("Program has ended")
                    exit(0) #This ends the program
                else:
                    print(f"{radius} IS NOT ACCEPTED an accepted radius. Please try 1, 2 or 5km")


            sorted_data = get_crime(coordinate, user_choice, int(radius))

            filename = input("What would you like to call your report? : ")
            if filename == "restart":
                menu()
            elif filename == "quit":
                print("Program has ended")
                exit(0) #This ends the program
            else: pass
            write_distance(sorted_data, filename)

        elif user_choice == "4": #restart
            print("Program has restarted")
            menu()

        elif user_choice == "5": #quit
            print("Program has ended")
            exit(0) #This ends the program


menu()