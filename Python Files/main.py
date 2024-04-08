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

        sadpepe = QPixmap("../Images/blankFace.svg")
        self.image_label = QLabel()
        self.image_label.setPixmap(sadpepe)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def on_submit(self):
        grinningpepe = QPixmap("../Images/smileyFace.svg")
        sadpepe = QPixmap("../Images/frowningFace.svg")
        user_input = self.input_box.text()
        countryName = ipAddressFinderGUI(user_input).strip()
        self.label2.setText(f"IP Address' Country: {countryName}")
        if (countryName == "Invalid IP Address" or countryName == "Invalid IP Address" or countryName == "An Error Has Occurred." or countryName == "Invalid Input, Try Again"):
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
        full_country_name = findCountryName(country_name)
    else:
        full_country_name = "Invalid Input, Try Again"
    return full_country_name


def findCountryFromURL(url):
    ip_add = socket.gethostbyname(url)
    country_name = ipAddressFinderGUI(ip_add)


def findCountryName(country_acronym):
    file_path = "../CountryNames/wikipedia-iso-country-codes.csv"
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                # Check if acronym matches (case-insensitive)
                if country_acronym.lower() == row[1].strip().lower():
                    return row[0].strip()  # Return country name (strip to remove whitespace)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return None  # Return None if country name not found
# STOP - Functions



# START - Main
def main():
    print("IP Country Finder")
    openGUI()
# STOP  - Main


if (__name__ == "__main__"):
    main()  # Runs the GUI
