import sys
import re

input_string = raw_input('Enter string of numbers ')
num_list = re.split(", |: |\-",input_string)
print(num_list)
input("Press enter to quit")
