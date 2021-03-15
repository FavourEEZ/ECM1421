import csv
def get_coordinates(user_postcode):
    """This function retrieves the centre coordinates (latitude or longitude) of a postcode"""

    # reading csv file. Using context manager (with open)

    with open('postcodes.csv', 'r') as postcode_csv:
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
                #Making a tuple wiith latitude and longitude so we can call the geodist function in dateSorting module
                location = (float(latitude), float(longitude))

                return location