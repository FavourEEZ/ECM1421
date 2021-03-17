import csv
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
            print(f"{filename} has been created!", "\n")
    except:
        print("An error occured while opening the file. Please check if the file is opened else", "\n")