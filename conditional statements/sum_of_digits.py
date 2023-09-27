# Get input from the user
number = int(input("Enter a number: ")) #143

# Initialize variables
total_sum = 0

# Loop through each digit
while number > 0:
    digit = number % 10  # Get the last digit #143-->3 14-->4 1
    total_sum = total_sum + digit   # Add the digit to the total sum #0+3 3+4 7+1
    number = number // 10 # Remove the last digit #143 -->14 14-->1 8
    result=total_sum+number

# Print the result
print("The sum of the digits is:", result)



