# Thee Glitch's Bubble Tea Stand 
Cost calculator that takes user input for tea base, tea add-ons, and loyalty membership and outputs the total cost of the beverage. 

Simply copy and paste the code in your favorite Python interpreter and run it.

https://www.programiz.com/python-programming/online-compiler/


## Requirements
- You will write a function with the input and outputs specified below.
- Your function must use at least one loop or iterator.
- Your function must use at least one conditional statement.
- Your function must use at least one Dictionary or List to store data. You should be familiar with the features of _**both**_ data types, even if you only use one in your function.
- The Python module math is imported and available to use but not required. Please do not import any additional modules (such as NumPy). 

## Problem Statement
Bubble tea (also known as boba) is a Taiwanese drink consisting of a tea base and many different toppings such as chewy tapioca pearls or slurpable grass jelly. Thee Glitch aims to run the trendiest bubble tea spot in the neighborhood. The shop boasts reliable WiFi, an extensive drinks menu, and a great loyalty program. With your help, Thee Glitch’s Bubble Tea Stand will have the speediest order cost calculator in the industry.

- An order has one and only one base tea. The options are milk, oolong, rose, and mango. Their respective prices are listed below. 
- An order has between none and multiple add ons. The options are boba, lychee, jelly, taro, and chia. Their respective prices are listed below. 
- If a customer is part of the Thee Glitch Bubble Tea Stand loyalty program, _subtract $1.00_ from the order total. 
- The function called `bubble_tea_calculator` accepts three parameters:
  - `tea_base`, a string to represent the base tea in the bubble tea order. 
  - `add_ons`, a list of strings where each string represents the optional add ons to the order
  - `loyalty_discount`, a boolean that represents if the order was made by a customer in the loyalty program
- The function must print the price of the order in dollars (i.e., with two decimal places). Refer to the example output for the specific formatting.

### Tea Base
|Name|Price ($)|
|----|---------|
| milk | 4.35 |
| oolong | 4.60 |
| rose | 5.85 |
| mango | 5.47 |

### Add Ons
|Name|Price ($)|
|----|---------|
| boba | 0.50 |
| lychee | 0.75 |
| jelly | 0.65 |
| taro | 1.00 |
| chia | 0.35 |

### Example 1
#### Input (arguments of the function)
```
tea_base = "milk"
add_ons = ["boba", "jelly", "taro"]
loyalty_discount = False
```
#### Output (printed by the function)
```
The cost is $6.50
```

### Example 2
#### Input (arguments of the function)
```
tea_base = "rose"
add_ons = []
loyalty_discount = False
```
#### Output (printed by the function)
```
The cost is $5.85
```

### Example 3
#### Input (arguments of the function)
```
tea_base = "oolong"
add_ons = ["chia"]
loyalty_discount = True
```
#### Output (printed by the function)
```
The cost is $3.95
```
