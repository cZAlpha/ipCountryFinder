# This project sets out to output a country given an IP address
# Function to read and print the lines of a .cidr file



# START - Imports
import csv
import os
import ipaddress
import socket
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
# STOP - Imports


# START - GUI Class
class MacStyleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('IP Country Finder')
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        self.label1 = QLabel('Enter the Public IPv4 Address You Would Like to Track:')
        self.label1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.label1)

        self.input_box = QLineEdit()
        layout.addWidget(self.input_box)

        self.button = QPushButton('Track')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.on_submit)

        self.label2 = QLabel("")  # Second label for user input
        layout.addWidget(self.label2)

        sadpepe = QPixmap("../Images/sadpepe.png")
        self.image_label = QLabel()
        self.image_label.setPixmap(sadpepe)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def on_submit(self):
        grinningpepe = QPixmap("../Images/grinningpepe.png")
        sadpepe = QPixmap("../Images/sadpepe.png")
        user_input = self.input_box.text()
        countryName = ipAddressFinderGUI(user_input).strip()
        self.label2.setText(f"IP Address' Country: {countryName}")
        if (countryName == "Invalid IP Address" or countryName == "Invalid IP Address" or countryName == "An Error Has Occurred."):
            self.image_label.setPixmap(sadpepe)
        self.image_label.setPixmap(grinningpepe)
# STOP  - GUI Class



# START - Functions
def openGUI():
    app = QApplication(sys.argv)
    window = MacStyleGUI()
    window.show()
    sys.exit(app.exec_())



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



def makeSpace(numOfLines=20):
    # A function that simply prints new line calls to the console,
    # allowing for more responsive looking console-based GUIs
    for space in range(0, numOfLines):  # For loop that prints new lines to make space
        print("\n")
    return 0



def makePipe(numOfPipes=3):
    # PAUSE
    for pipes in range(0, numOfPipes):
        # Pause
        print("|")
    return 0



def list_files_in_directory(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)  # [-7:-5]
            file_paths.append(file_path)
    return file_paths



def ipAddressFinderGUI(ip_address):
    # Init. Vars
    directory = """/Users/noah/PycharmProjects/ipCountryFinder/ipCountryFinder/IPAddressData"""
    file_path = "../CountryNamesCSV/wikipedia-iso-country-codes.csv"

    if (is_valid_ip(ip_address) == False):  # Error catching for invalid IP addresses
        return "Invalid IP Address"

    file_path_list = list_files_in_directory(directory)
    for filename in file_path_list:
        if (readCIDR(filename, ip_address) == 0):  # If the IP's subnet is found in the directory of .cidr files
            countryAcronym = filename[-7:-5]
            countryName = findCountryName(file_path, countryAcronym)
            if (countryName == 1):
                print("ERROR OCCURRED IN findCountryName()")
                return "An Error Has Occurred."  # Error
    if (countryName != None):
        return countryName
    return "An Error Has Occurred."  # Error
# STOP - Functions



# START - Main
def main():
    print("IP Country Finder")
    openGUI()
# STOP  - Main


if (__name__ == "__main__"):
    main()  # Runs the GUI
