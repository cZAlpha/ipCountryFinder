# This project sets out to output a country given an IP address
# Function to read and print the lines of a .cidr file



# START - Imports
import csv
# STOP - Imports



# START - Functions
def readCIDR(file_path, inputed_ip, flag = True):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()  # string processing
                if(line == inputed_ip):
                    return 0
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def readCSV(file_path, country_acronym):
    data_list = []
    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_list.append(row)
                countryname = row[0]
                #print(country_acronym)
                print(row[1].lower())
                if (country_acronym == row[1].lower()):
                    print(countryname)
                    return 0

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return data_list


def ipAddressFinder(ip_address, file_path):
    # This function will take an argument of an IPADRESS as a string
    # and output which country it came from
    print("Function is running...")

    file_path_list = ["ad.cidr", "ae.cidr", "af.cidr"]

    # for loop that iterates over the list called "file_path_list"
    # where "country" is the loop variable holding the name
    # of each string index inside of "file_path_list"
    for country in file_path_list:
        if (readCIDR(country, ip_address) == 0):
            print("Country Acronym is: " + country[0:2])
        if (readCSV("../IPAddressData/wikipedia-iso-country-codes.csv", country[0:2]) == 0):
            print("Country Name is:      " )

    print("Done.")

# STOP - Functions

ipAddressFinder("46.172.224.0/19", "../IPAddressData/wikipedia-iso-country-codes.csv")
