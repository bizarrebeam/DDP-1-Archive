"""Function to convert binary into integer"""
number_bin = input("Input the binary to be converted: ")

def binary_to_integer(number):  
    # Set some initial variables
    decimal = 0                         
    power = 0

    for digit in reversed(number):                                  # Calculating binary are from the right-most
        if digit == "1":                                            # For digit 1 in binary,
            decimal += 2**power                                           # calculate with base of 2 for the value
        power += 1                                                  # Increment the power
    
    return decimal

# Convert the input binary to an integer
integer_result = binary_to_integer(number_bin)

# Print the result
print(
    f"The integer number from binary {number_bin} is {integer_result}"
    )



"""Function to convert integer into octal"""
number_int = input("Input the integer to be converted: ")
def int_to_octal(number):
    octal = ""                                                      # Store the octal representation

    if number == 0:                                                 # Handle the special case of 0
        return "0"  

    while number > 0:                                               # Convert the decimal number to octal
        remainder = number % 8                                      # Get the remainder when dividing by 8
        octal = str(remainder) + octal                              # Remainder to the left of the octal string
        number //= 8                                                # Integer division to update num

    return octal

# Test the function
octal_result = int_to_octal(number_int)
print(
    f"The octal number from integer {number_int} is {octal_result}"
      )


