import csv,os, time  #csv lets us read csv files. os lets us execute files in our directory easily. Time allows us to use time/date in our program
from geodist import distance

#TODO Do testing & Assert statements for geodist.py
#TODO Modularise all code
PS_filename = 'postcodes.csv'
crime_folder = '/Devon_and_Cornwall_crime_data_2020/'


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
            print("Throughout the program you can enter 'restart' or 'quit' when prompted to input")
            time.sleep(0.5)

            postcode = input("Please enter a Postcode > ")
            #Adding the quit and restart options for the user
            if postcode == "quit":
                print("Program has ended")
                exit(0)
            elif postcode == "restart":
                menu()
            elif postcode == "":
                while postcode == "":
                    postcode = input("Incorrect input. Please enter a Postcode > ")
                
            else: pass
            #Importing the verify_postcode module to check our postcode
            
            try:
                from modules import read_verifyPostcode
                verified_postcode = read_verifyPostcode.verify_postcode(postcode) #Verifying the coordinates by calling the module
                from modules import read_getCoordinates
                coordinate = read_getCoordinates.get_coordinates(verified_postcode)
            except ImportError as i:
                print("Ensure 'read_verifyPostcode' is opened before program execution")
            except UnboundLocalError as u:
                print("Local variable error. Please try program later.")
        
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
                    print("Program has been restarted")
                    menu()
                elif radius == "quit":
                    print("Program has ended")
                    quit(0) #This ends the program
                else:
                    print(f"{radius} IS NOT ACCEPTED an accepted radius. Please try 1, 2 or 5km")

            from modules import dataSorting
            sorted_data = dataSorting.get_crime(coordinate, user_choice, int(radius))

            filename = input("What would you like to call your report? : ")
            if filename == "restart":
                menu()
            elif filename == "quit":
                print("Program has ended")
                quit(0) #This ends the program
            else: pass
            from modules import fileWriting
            fileWriting.write_distance(sorted_data, filename)

        elif user_choice == "4": #restart
            print("Program has been restarted")
            menu()

        elif user_choice == "5": #quit
            print("Program has ended")
            quit(0) #This ends the program


menu()

