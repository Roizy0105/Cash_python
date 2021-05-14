import cs50

# initalize value to zero to create a do while loop
amount = 0.0

# create a loop that will make sure the input user enters is greater then 0
while amount < 0.01:
    # prompt user for input
    amount = cs50.get_float("Enter amount: ")

# created a varuble that will keep track of how many coins we need to give
total = 0

# convert amont to int
value = round(amount * 100)

# if value is more than 25 add a quarter    
while value >= 25:
    value -= 25
    total += 1
    
# in this case add a dime    
while value >= 10:
    value -= 10
    total += 1
    
# in this case add a nical    
while value >= 5:
    value -= 5
    total += 1
    
# in this case adda penny    
while value >= 1:
    value -= 1
    total += 1
    
# print total amount of coins needed    
print(total)