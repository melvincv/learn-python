# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# Type checking
print(type(two_digit_number))

# Get the individual digits
astr = two_digit_number[0]
bstr = two_digit_number[1]

# Convert them to integer and print output
result = int(astr) + int(bstr)
print(result)
