import os

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_FREEZING_POINT = 32  # Freezing point of water in Fahrenheit

# Function to check if the file exists and is not empty
def check_file(file_path):
    if os.path.exists(file_path):
        if os.path.getsize(file_path) > 0:
            print(f"File '{file_path}' exists and is not empty.")
        else:
            print(f"File '{file_path}' exists but is empty.")
    else:
        print(f"File '{file_path}' does not exist.")

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - CELSIUS_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + CELSIUS_FREEZING_POINT
    return fahrenheit

# Main function to handle user interaction
def main():
    try:
        # Get user input for temperature and unit
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Check for valid unit and call appropriate function
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    # Check a sample file (for testing purpose)
    file_path = 'temp_conversion_tool.py'  # Change the path if needed
    check_file(file_path)
    
    # Run the temperature conversion functionality
    main()

