import os, csv, time
from geodist import distance
from pathlib import Path

def get_crime(coordinate, user_choice, radius):
    """ This function retrives all reported street level within a radius of the centre coordinate """
    sort_radius = []
    sort_date = []
    sort_category = []

    #Finding our current directory and the directory with crime data
    crime_folder = '/Devon_and_Cornwall_crime_data_2020/'
    cur_path = os.path.dirname(__file__) #This gives us out current directory
    path = Path(cur_path) #This imported function allows us to go up to our parent directory
    target_path = str(path.parent) + crime_folder #Both combined makes our target path location
    exists = os.path.isdir(target_path)

    # If target path exists
    if exists: # Aka if exists == True
        for root,dirs,files in os.walk(target_path):
            for file in files: #Looping through each file in the directory
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
                            if user_choice == "1": #If user wants to sort by distance
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

                            elif user_choice == "3": #sort by Crime Category
                                d = distance(coordinate, current_crime_location)
                                if d <= radius:
                                    line.append(d)
                                    sort_category.append(line)
                        except:
                            pass
            if user_choice == "1": #If user wants to sort by distance
                #For distance we get the distance from a 2D
                sort_radius = sorted(sort_radius, key=lambda sorted_radius:sorted_radius[12])
                return sort_radius
            elif user_choice == "2": #sort by date
                return sort_date
            elif user_choice == "3": #sort by Crime Category
                sort_category = sorted(sort_category, key=lambda row: row[9], reverse=True )
                return sort_category
    else:
        print("You don't seem to have the folder/files required to retrieve the crime")
        time.sleep(2) #Program waits 2 seconds then prints the next statement
        print("If you do, please make a folder called: '/Devon_and_Cornwall_crime_data_2020/' and only put the crime csv data files there")
        from main import menu
        menu()
