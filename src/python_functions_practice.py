def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(test_string):
    return (len("A string of length 21"))  

def join_string(string_1, string_2):
    return f"{string_1}{string_2}"

def add_string_as_number(str_1, str_2):
    return int(str_1) + int(str_2)

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

def number_to_full_month_name(month):
    return months[month -1]

def number_to_short_month_name(month_num):
   return months[month_num -1][:3]
