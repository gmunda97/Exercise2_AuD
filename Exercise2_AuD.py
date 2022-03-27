#!/usr/bin/env python3

# Question 1

def count_integer(numbers, integer):
    count = 0
    for item in numbers:
        if (item == integer):
            count = count + 1
    return count

    if (integer not in numbers):
        return integer

numbers = [1, 3, 9, 42, 999, 645, 42]
integer = 42

count_integer(numbers, integer)

# Question 2

def list_func(numbers, integer):
    count = 0
    for index, value in enumerate(numbers):
        if numbers[index] == integer:
            numbers[index] = 6
            count = count + 1

    if count > 0:
        newnumbers = numbers.copy
        numbers.reverse()
        print(numbers)
        return newnumbers
    else:
        return []


numbers = [1, 2, 3, 4, 5, 6]
integer = 3

list_func(numbers, integer)

# Question 3

def compare_lists(list1, list2):
    list_difference = []
    for item in list1:
        if item in list2:
            list_difference.append(item)
    return list_difference

list1 = ["apple", "orange", "kiwi"]
list2 = ["mango", "watermelon", "orange"]

compare_lists(list1, list2)


# Question 4

def remove_duplicates(lst):
    noduplist = []
    for element in lst:
        if element not in noduplist:
            noduplist.append(element)

    return noduplist


lst = [10, 20, 30, 30, 40, 50, 60, 60]

remove_duplicates(lst)

# there is another way to solve this problem

def remove_duplicates(lst):
    return list(set(lst))  # create a set and convert it into a list


mylist = remove_duplicates([1, 2, 3, 3, 4, 5, 6, 6, 7])


print(mylist)


# Question 5

def dict_func(dictionary):
    if dictionary.get(key1) is None:
        print(new_dict.get("Type", "unknown type"))
    elif dictionary.get(key2) is None:
        print(new_dict.get("Brand", "unknown brand"))
    elif dictionary.get(key3) is None:
        print(new_dict.get("Price", "unknown price"))
    else:
        print("You have a " + (TYPE) + " from " + (BRAND) + " that costs " + str(PRICE))
    return new_dict

dictionary = {"Type": "Macbook", "Brand": "Apple", "Price": 2300}
dictionary["OS"] = "MacOS"

TYPE = dictionary["Type"]
BRAND = dictionary["Brand"]
PRICE = dictionary["Price"]

new_dict = {"Brand": "Apple", "Price": 2300}

key1 = "Type"
key2 = "Brand"
key3 = "Price"

print(dictionary)
dict_func(dictionary)

