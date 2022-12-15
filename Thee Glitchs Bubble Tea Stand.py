# Use print statement to welcome customers to Bubble Tea Stand
print("Welcome to Thee Glitch's Bubble Tea Stand!")

# Use print statement to display horizontal line
print("─" * 33)

# Use print statement to display tea base choices along with their corresponding prices
print("""Your tea base choices are: 
  ~ milk: $4.35
  ~ oolong: $4.60
  ~ mango: $5.47
  ~ rose: $5.85
""")

# Ask for user input for tea base choices and use .lower() method to return lowercase input
tea_base = input("CHOOSE 1 TEA BASE: ").lower()

# Use string interpolation/f-string to print users' tea base choice
print(f"\nYour tea base is {tea_base}!")

# Use print statement to display horizontal line
print("─" * 55)

# Use print statement to display add-on choices along with their corresponding prices
print("""Your add-on options are: 
  ~ chia: 0.35
  ~ boba: $0.50
  ~ jelly: $0.65
  ~ lychee: $0.75
  ~ taro: $1.00
""")

# Ask for user input for tea base choices
add_ons = input("""
* Please input your choices using lowercase letters and separate them with a space.

* If no add-ons, press the Enter key.

___________________________

CHOOSE YOUR ADD-ONS: """).split(" ")

# Use for loop to print users' add-on choices
for i in add_ons:
    print(f"\nYour add-on is: {i.lower()}")

# Use print statement to insert new long and display horizontal line 
print("\n")
print("─" * 55)

# Ask for user input for loyalty discount membership and use .capitalize() method to return user input with capital letter
loyalty_discount = input("You're a loyalty member, right? True or False?: ").capitalize() == "True"

# Use print statement to display horizontal line 
print("─" * 55)

# Define a function with 3 parameters to represent tea base, add-ons, and loyalty discount
def bubble_tea_calculator(tea_base, add_ons, loyalty_discount):

# Create a docstring describing the input and output of function
  """
    *input: 
      - 1 tea base (user input: milk, oolong, rose, or mango)
      - 0-5 optional add ons (user input: boba, lychee, jelly, taro, chia [each choice should be lower case and seperated by a space, if no add on, press the enter key])
      - 1 loyalty discount represented by boolean (user input: True or False)
    
    *output: 
      - function prints out the price of the order in dollars with two decimal places
  """
  
# Use dictionary to assign tea bases to a key-value pair to represent the names of the tea bases and their corresponding prices 
  teaBaseOptions = {"milk": 4.35, "oolong": 4.60, "mango": 5.47, "rose": 5.85}

# Use dictionary to assign add-ons to a key-value pair to represent the names of the add-ons and their corresponding prices 
  addOnOptions = {"chia": 0.35, "boba": 0.50, "jelly": 0.65, "lychee": 0.75, "taro": 1.00}

# Use dict.get() method to assign to tea base key values variable, total tea cost
  teaTotal = teaBaseOptions.get(tea_base, 0.00)

# Use a conditional statement to validate customers' add_on option
  if isinstance(add_ons, list):

# Use a for loop and dict.get() method to iterate through add-on dictionary, get add-on price, and then add the it to total tea cost
    for addOn in add_ons:
      teaTotal += addOnOptions.get(addOn, 0.00)

# Use conditional to validate customers' loyalty_discount status and if "True", then subtract $1 from total tea cost
  if loyalty_discount:
    teaTotal -= 1.00

# Print/output the tea total using string interpolation/f-string; format it to two decimal places
  print(f"\nThe total cost of your bubble tea drink is ${teaTotal:.2f}. \n\nEnjoy and thank you for your support! <3")

# Call the bubble tea stand function calculator
bubble_tea_calculator(tea_base, add_ons, loyalty_discount)

#
# Optional
#

# Manually test function by calling it with the given arguments/inputs

# bubble_tea_calculator("milk", ["boba", "jelly", "taro"], False) # Expected output: "The cost is $6.50"

# bubble_tea_calculator("rose", [], False) # # Expected output: "The cost is $5.85"

# bubble_tea_calculator("oolong", ["chia"], True) # Expected output: "The cost is $3.95"