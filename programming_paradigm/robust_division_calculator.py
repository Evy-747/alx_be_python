def safe_divide(numerator, denominator):
    """
    Performs division and handles errors like division by zero and non-numeric inputs.

    :param numerator: The numerator for the division.
    :param denominator: The denominator for the division.
    :return: The result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        result = num / denom
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        return f"Unexpected error: {str(e)}"

