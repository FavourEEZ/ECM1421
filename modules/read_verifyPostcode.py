import csv

def verify_postcode(postcode):
    """This function opens postcodes.csv and checks if the user entered postcode exists"""
    accepted = False
    accepted_list = []
    # This while loop repeats until user types a radius of 1, 2 or 5 (as stated in the pdf)

    while accepted == False:
        with open('postcodes.csv', 'r') as postcode_csv:
            #using the reader method to read csv file. Pass file into method.
            csv_reader = csv.reader(postcode_csv)
            next(csv_reader) #ignores the first line
            #Each row becomes a list. Line[0] is the first column that holds the postcode for each row.
            for line in csv_reader:
                if line[0] == postcode:
                    #Adding the accpeted postcode into a list. We then check if the user input postcode is in the list.
                    accepted_list.append(line[0])
                else: pass
        if postcode in accepted_list:
            print("Postcode accepted")
            return postcode
        else:
            #Else, an error message gets printed out to the user and they get prompted to the menu
            print("***", postcode, "was not accepted. Please enter an accepted postcode in all caps and a space between incode 'DT1' and outcode '1AD'"
                                   "\n" "Please try again" "\n")
            from main import menu
            menu()
