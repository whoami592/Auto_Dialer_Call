import pyautogui
import time
import csv
import sys
from datetime import datetime

# Banner
def display_banner():
    print("""
    ╔════════════════════════════════════════════════════╗
    ║         Auto Dialer Script                         ║
    ║   Coded by Pakistani Ethical Hacker: Mr. Sabaz     ║
    ║               Ali Khan                             ║
    ║   Date: June 25, 2025                             ║
    ╚════════════════════════════════════════════════════╝
    """)

# Function to load phone numbers from a CSV file
def load_numbers(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if exists
            for row in reader:
                if row and row[0].strip():
                    numbers.append(row[0].strip())
        return numbers
    except FileNotFoundError:
        print("Error: CSV file not found!")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

# Function to simulate dialing
def dial_number(number):
    print(f"Dialing: {number}")
    pyautogui.write(number)
    pyautogui.press('enter')  # Press enter to initiate the call
    time.sleep(5)  # Wait for the call to connect (adjust as needed)
    pyautogui.press('enter')  # Simulate ending the call or moving to next step
    time.sleep(2)  # Delay between calls

def main():
    display_banner()
    
    # Get CSV file path from user
    file_path = input("Enter the path to your CSV file with phone numbers: ")
    numbers = load_numbers(file_path)
    
    if not numbers:
        print("No valid phone numbers found in the CSV file.")
        return
    
    print(f"Loaded {len(numbers)} phone numbers.")
    input("Ensure your dialer application is open and active. Press Enter to start dialing...")
    
    # Set pyautogui pause and failsafe
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True
    
    # Dial each number
    for number in numbers:
        dial_number(number)
        print(f"Completed call to {number} at {datetime.now().strftime('%H:%M:%S')}")
    
    print("Auto dialing completed!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAuto dialer stopped by user.")
        sys.exit(0)