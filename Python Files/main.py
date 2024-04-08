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

import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
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
        else:
            self.image_label.setPixmap(grinningpepe)
# STOP  - GUI Class



# START - Functions
def openGUI():
    app = QApplication(sys.argv)
    window = MacStyleGUI()
    window.show()
    sys.exit(app.exec_())


# TO DO:
# 1 - Make a function called "isIPValid(ip)" that checks if an IP is valid before
#     running the "ipAddressFinderGUI()" function
#
# 2 - Make a function to do the same thing for URLs
#
# 3 - Add try, catch exception/error catches in all major functions to ensure cohesion


def isIPValid(ip):
    return all(char.isdigit() or char == '.' for char in ip)


def ipAddressFinderGUI(ip):
    country_name = None
    if ( isIPValid(ip) ): # Checks if IP is valid
        res = DbIpCity.get(ip, api_key="free")
        print(f"IP Address: {res.ip_address}")
        print(f"Location: {res.city}, {res.region}, {res.country}")
        print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
        country_name = f"{res.country}"
    else:
        country_name = "Invalid Input, Try Again"
    return country_name


def findCountryFromURL(url):
    ip_add = socket.gethostbyname(url)
    country_name = ipAddressFinderGUI(ip_add)


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

# STOP - Functions



# START - Main
def main():
    print("IP Country Finder")
    openGUI()
# STOP  - Main


if (__name__ == "__main__"):
    main()  # Runs the GUI
