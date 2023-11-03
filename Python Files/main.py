# This project sets out to output a country given an IP address
# Function to read and print the lines of a .cidr file



# START - Imports
import csv
import time
import os
# STOP - Imports



# START - Functions
def readCIDR(file_path, inputed_ip, flag=True):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()  # string processing
                if (line == inputed_ip):
                    return 0
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



def findCountryName(file_path, country_acronym):
    data_list = []
    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_list.append(row)
                countryname = row[0]
                #print(country_acronym)
                #print(row[1].lower())
                if (country_acronym == row[1].lower()):  # If the country is located
                    return countryname
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return 1  # Returns 1, the flag for an error



def makeSpace(numOfLines = 20):
    # A function that simply prints new line calls to the console,
    # allowing for more responsive looking console-based GUIs
    for space in range(0, numOfLines):  # For loop that prints new lines to make space
        print("\n")
    return 0



def makePipe(numOfPipes = 3):
    # PAUSE
    for pipes in range(0, numOfPipes):
        # Pause
        print("|")
    return 0



def list_files_in_directory(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)#[-7:-5]
            file_paths.append(file_path)
    return file_paths



def ipAddressFinder(ip_address, file_path):
    directory = 'C:\\Users\Parents\PycharmProjects\ipCountryFinder\ipCountryFinder\IPAddressData'
    # This function will take an argument of an IPADDRESS as a
    # string and output which country it came from
    print("+======================+")
    print("|        Function is running...       |")
    print("+======================+")
    time.sleep(0.5)

    file_path_list = list_files_in_directory(directory)
    # for loop that iterates over the list called "file_path_list"
    # where "country" is the loop variable holding the name
    # of each string index inside of "file_path_list"
    for country in file_path_list:
        if (readCIDR(country, ip_address) == 0):
            countryAcronym = country[-7:-5]
            makeSpace()  # Makes space
            print("+========================+")
            print("|  COUNTRY ACRONYM FOUND |")
            print("+========================+")
            time.sleep(0.75)
            makePipe()
            print("+===================================+")
            print("|   Country Acronym is: " + countryAcronym )
            countryName = findCountryName("../IPAddressData/wikipedia-iso-country-codes.csv", countryAcronym)
            print("|   Country Name is: " + countryName)
            print("+===================================+")
# STOP - Functions



ipAddressFinder("46.172.224.0/19", "../IPAddressData/wikipedia-iso-country-codes.csv")
