# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_FREEZING_POINT = 32  # Freezing point of water in Fahrenheit

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the global factor
    celsius = (fahrenheit - CELSIUS_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the global factor
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + CELSIUS_FREEZING_POINT
    return fahrenheit

def main():
    try:
        # Get user input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Check for valid input and call the appropriate function
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
    main()

