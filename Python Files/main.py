# This project sets out to output a country given an IP address
# Function to read and print the lines of a .cidr file



# START - Imports
import csv
import time
import os
import ipaddress
import socket
# STOP - Imports



# START - Functions
def is_valid_ip(ip_str):
    try:
        socket.inet_pton(socket.AF_INET, ip_str)  # Check for IPv4 address
        return True
    except socket.error:
        pass
    return False



def get_subnet_bounds(subnet):
    try:
        # Parse the subnet using the ipaddress module
        network = ipaddress.ip_network(subnet, strict=False)
        # Calculate the lower and upper bounds
        lower_bound = str(network.network_address)
        upper_bound = str(network.broadcast_address)
        return lower_bound, upper_bound

    except ValueError as e:
        return f"Invalid subnet: {str(e)}"



def is_ip_in_subnet(ip, subnet):
    try:
        # Parse the subnet using the ipaddress module
        network = ipaddress.ip_network(subnet, strict=False)

        # Check if the IP address is in the subnet
        if ipaddress.ip_address(ip) in network:
            return True
        else:
            return False
    except ValueError as e:
        return f"Invalid subnet: {str(e)}"



def readCIDR(file_path, inputed_ip):  # CIDR READER
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                subnet = line.strip()  # string processing
                if (is_ip_in_subnet(inputed_ip, subnet)):
                    return 0
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



def findCountryName(file_path, country_acronym):  # CSV READER
    data_list = []
    try:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data_list.append(row)
                countryname = row[0]
                if (country_acronym == row[1].lower()):  # If the country is located
                    return countryname
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return 1  # Returns 1, showing that it did not find the country name in the csv file



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



def ipAddressFinder():
    print("====================================")
    print("Input IP You Want To Track:")
    ip_address = input("> ")
    print("====================================")

    if (is_valid_ip(ip_address) == False):  # Error catching for invalid IP addresses
        print("+=====================================+")
        print("|        Invalid IP Address           |")
        print("+=====================================+")
        time.sleep(1.25)
        makeSpace()  # Makes space
        return 1  # Error

    if (ip_address == "exit" or ip_address == "e"):  # Checks for user exit
        makeSpace()
        print("+=====================================+")
        print("|        Closing Program...           |")
        print("+=====================================+")
        return 0  # Ran fine

    directory = """/Users/noah/PycharmProjects/ipCountryFinder/ipCountryFinder/IPAddressData"""
    file_path = "../wikipedia-iso-country-codes.csv"
    # This function will take an argument of an IPADDRESS as a
    # string and output which country it came from
    print("+=====================================+")
    print("|        Function is running...       |")
    print("+=====================================+")
    time.sleep(0.5)
    makeSpace()  # Makes space

    file_path_list = list_files_in_directory(directory)
    for filename in file_path_list:
        if (readCIDR(filename, ip_address) == 0):  # If the IP's subnet is found in the directory of .cidr files
            flag = True  # Flag to check for if the IP was found
            print("+=========================+")
            print("|  COUNTRY ACRONYM FOUND  |")
            print("+=========================+")
            time.sleep(1)
            makeSpace()  # Makes space
            countryAcronym = filename[-7:-5]
            countryName = findCountryName(file_path, countryAcronym)
            if (countryName == 1):
                print("ERROR OCCURRED IN findCountryName()")
                return 1  # Error
            print("+=====================================================================+")
            print("|   IP Address: " + ip_address)
            print("|   Country Acronym is: " + countryAcronym)
            print("|   Country Name is: " + countryName)
            print("+=====================================================================+")
# STOP - Functions



ipAddressFinder()
