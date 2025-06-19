from email.mime.text import MIMEText
import smtplib
from statistics import mean
import tkinter as tk
from tkinter import ttk, messagebox

# Define the BodyTemperatureMonitor class
class BodyTemperatureMonitor:
    def __init__(self, alert_threshold=37.5):
        # Initialize the temperature monitor with an alert threshold
        self.temperatures = []  # Array to store temperature readings
        self.alert_threshold = alert_threshold

    def add_readings(self, temps):
        """Store multiple temperature readings."""
        self.temperatures.extend(temps)

    def calculate_average(self):
        """Calculate the average of stored readings."""
        return mean(self.temperatures) if self.temperatures else 0

    def detect_outliers(self):
        """Detect outliers based on the alert threshold."""
        lower_threshold = 35.0  # Define a reasonable lower bound

        # Using a linear scan to identify outliers
        outliers = []
        for temp in self.temperatures:
            if temp > self.alert_threshold or temp < lower_threshold:
                outliers.append(temp)
        return outliers

    def analyze_temperatures(self):
        """Calculate average, detect outliers, and return analysis."""
        average_temp = self.calculate_average()
        outliers = self.detect_outliers()
        return {
            "average": average_temp,
            "outliers": outliers,
            "total_readings": len(self.temperatures),
        }

    def send_alert(self, message):
        """Send an alert via email."""
        sender_email = "your_email"  # Replace with your email
        receiver_email = "receiver_email"  # Replace with the receiver's email
        password = "App_password"  # Replace with your App Password

        try:
            msg = MIMEText(message)
            msg["Subject"] = "Temperature Alert!"
            msg["From"] = sender_email
            msg["To"] = receiver_email

            # Connect to the SMTP server and send the email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(sender_email, password)  # Log in to the server
                server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email

            messagebox.showinfo("Success", "Alert sent successfully!")
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "SMTP Authentication Error: Check your email and password.")
        except smtplib.SMTPConnectError:
            messagebox.showerror("Error", "SMTP Connection Error: Unable to connect to the server.")
        except smtplib.SMTPException as e:
            messagebox.showerror("Error", f"SMTP Error: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected Error: {e}")

# GUI Application
class TemperatureMonitorApp:
    def __init__(self, root):
        # Initialize the GUI application
        self.root = root
        self.root.title("Body Temperature Monitor")
        self.root.geometry("500x400")
        self.monitor = BodyTemperatureMonitor(alert_threshold=37.5)

        # Styling
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", padding=6, font=("Helvetica", 10))
        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 10))

        # Main Frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Temperature Input
        self.label_input = ttk.Label(self.main_frame, text="Enter temperatures (comma-separated):")
        self.label_input.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

        self.entry_input = ttk.Entry(self.main_frame, width=40)
        self.entry_input.grid(row=1, column=0, pady=(0, 10))

        self.button_add = ttk.Button(self.main_frame, text="Add Readings", command=self.add_readings)
        self.button_add.grid(row=2, column=0, pady=(0, 10))

        # Analysis Display
        self.label_analysis = ttk.Label(self.main_frame, text="Analysis:")
        self.label_analysis.grid(row=3, column=0, sticky=tk.W, pady=(10, 5))

        self.text_analysis = tk.Text(self.main_frame, height=8, width=50, state=tk.DISABLED)
        self.text_analysis.grid(row=4, column=0, pady=(0, 10))

        # Buttons
        self.button_clear = ttk.Button(self.main_frame, text="Clear Readings", command=self.clear_readings)
        self.button_clear.grid(row=5, column=0, pady=(0, 10))

        self.button_exit = ttk.Button(self.main_frame, text="Exit", command=root.destroy)  # Fixed exit button
        self.button_exit.grid(row=6, column=0, pady=(0, 10))

    def add_readings(self):
        """Add temperature readings and analyze."""
        try:
            temps_input = self.entry_input.get()
            temps = [float(temp.strip()) for temp in temps_input.split(",")]
            self.monitor.add_readings(temps)
            messagebox.showinfo("Success", "Temperature readings added successfully!")

            # Analyze temperatures and check for outliers
            analysis = self.monitor.analyze_temperatures()
            self.display_analysis(analysis)

            if analysis["outliers"]:
                alert_message = (
                    f"Abnormal temperature readings detected: {analysis['outliers']}\n"
                    f"Average temperature: {analysis['average']:.2f}\n"
                    f"All readings: {self.monitor.temperatures}"
                )
                self.monitor.send_alert(alert_message)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values separated by commas.")

    def display_analysis(self, analysis):
        """Display analysis in the text box."""
        self.text_analysis.config(state=tk.NORMAL)
        self.text_analysis.delete(1.0, tk.END)
        self.text_analysis.insert(tk.END, f"Total readings: {analysis['total_readings']}\n")
        self.text_analysis.insert(tk.END, f"Average temperature: {analysis['average']:.2f}\n")
        self.text_analysis.insert(tk.END, f"Outliers: {analysis['outliers']}\n")
        self.text_analysis.config(state=tk.DISABLED)

    def clear_readings(self):
        """Clear all temperature readings."""
        self.monitor.temperatures = []
        self.text_analysis.config(state=tk.NORMAL)
        self.text_analysis.delete(1.0, tk.END)
        self.text_analysis.config(state=tk.DISABLED)
        messagebox.showinfo("Success", "Temperature readings cleared.")

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureMonitorApp(root)
    root.mainloop()