# TemperatureMonitoring
A desktop GUI application built with Python and Tkinter to monitor patient body temperatures. It analyzes temperature readings, identifies outliers, and automatically sends email alerts when abnormal temperatures are detected.

# About The Project
This project provides a simple yet effective desktop application for healthcare monitoring. Users can input a series of patient temperature readings through a user-friendly graphical interface. The application immediately analyzes this data to calculate the average temperature and detect any readings that fall outside the normal range (outliers).

When an abnormal temperature is detected, the system automatically dispatches an email alert to a pre-configured address, ensuring that healthcare providers are promptly notified of potential health concerns. This tool is a practical demonstration of how Python can be used to build interactive applications with real-world utility, combining data processing with automated notifications.

# Application Interface
# Key Features
Interactive GUI: A clean and simple user interface built with Tkinter for easy data entry and analysis.
Real-Time Analysis: Instantly calculates the average and identifies outliers from the input temperature readings.
Automated Email Alerts: Sends an email notification automatically using SMTP when an abnormal temperature is recorded.
On-Screen Feedback: Displays the analysis summary directly within the application window.
Error Handling: Provides user-friendly pop-up messages for invalid input and email sending errors.
Standalone Application: Runs as a self-contained desktop application with no external database or service dependencies.
# How It Works
The application's workflow is straightforward:

Enter Data: The user inputs one or more temperature readings, separated by commas, into the input field.
Add Readings: Clicking the "Add Readings" button parses the input and stores the temperatures.
Analyze Data: The application calculates the average of all entered readings and identifies any temperatures above the 37.5°C alert threshold or below the 35.0°C lower threshold.
Display Results: The total number of readings, the average temperature, and a list of any detected outliers are displayed in the "Analysis" text box.
Send Alert: If any outliers are found, the system connects to a Gmail SMTP server and sends a detailed alert email to the specified recipient.
# Technologies Used
This project is built with standard Python libraries:

GUI Framework: Tkinter
Email Communication: smtplib
Data Processing: statistics (for calculating the mean)
# Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites
You will need the following:

Python 3.x installed on your system.
A Gmail Account to be used for sending the alerts.
A Gmail App Password for that account.
Important: Due to Google's security policies, you can no longer use your regular password for applications like this. You must generate an "App Password".
How to get an App Password:
Go to your Google Account settings: myaccount.google.com.
Navigate to the "Security" section.
Ensure "2-Step Verification" is turned ON. You cannot create App Passwords without it.
Click on "App passwords".
Select "Mail" for the app and "Other (Custom name)" for the device. Give it a name like "Python Temp Alert".
Google will generate a 16-character password. Copy this password. This is what you will use in the script.
Configuration
Before running the script, you must configure the email settings directly in the code.

Open the Python script (your_script_name.py).

Navigate to the send_alert method within the BodyTemperatureMonitor class.

Update the following variables with your own credentials:

Python

def send_alert(self, message):
    """Send an alert via email."""
    sender_email = "your_email@gmail.com"  # <-- REPLACE with your Gmail address
    receiver_email = "recipient_email@example.com"  # <-- REPLACE with the receiver's email
    password = "your_16_character_app_password"  # <-- REPLACE with your Gmail App Password

    # ... rest of the code
# Usage
Once the configuration is complete, you can run the application.

Open your terminal or command prompt.
Navigate to the directory where you saved the Python file.
Run the script:
Bash

python TemperatureMonitoring.py
The application window will appear. You can now start adding temperature readings to test its functionality.
