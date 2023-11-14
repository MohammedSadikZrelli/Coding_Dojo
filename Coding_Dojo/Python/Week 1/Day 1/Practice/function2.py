# Countdown
def countdown(number):
    return list(range(number, -1, -1))

# Example usage for Countdown
countdown_result = countdown(5)
print(countdown_result)  # Output: [5, 4, 3, 2, 1, 0]


# Print and Return
def print_and_return(numbers):

    print(numbers[0])
    return numbers[1]

# Example usage for Print and Return
print_return_result = print_and_return([1, 2])
print(print_return_result)  # Output: 1


# First Plus Length
def first_plus_length(input_list):
    return input_list[0] + len(input_list)

# First Plus Length
first_plus_length_result = first_plus_length([1, 2, 3, 4, 5])
print(first_plus_length_result)  # Output: 6


# Values Greater than Second
def values_greater_than_second(input_list):
   
    if len(input_list) < 2:
        return False
    
    second_value = input_list[1]
    greater_values = [value for value in input_list if value > second_value]
    
    print(len(greater_values))
    return greater_values

# Example usage for Values Greater than Second
values_greater_than_second_result1 = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(values_greater_than_second_result1)  # Output: 3, [5, 3, 4]

values_greater_than_second_result2 = values_greater_than_second([3])
print(values_greater_than_second_result2)  # Output: False


# This Length, That Value
def length_and_value(size, value):
    return [value] * size

# This Length, That Value 
length_and_value_result1 = length_and_value(4, 7)
print(length_and_value_result1)  # Output: [7, 7, 7, 7]

length_and_value_result2 = length_and_value(6, 2)
print(length_and_value_result2)  # Output: [2, 2, 2, 2, 2, 2]