# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a Fahrenheit temperature to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a Celsius temperature to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to interact with the user.
    Prompts for a temperature and unit, validates input, and performs conversion.
    """
    try:
        # User input for temperature
        temp_input = input("Enter the temperature to convert: ")
        
        # Validate if the input is numeric
        if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)
        
        # User input for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform the appropriate conversion
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

