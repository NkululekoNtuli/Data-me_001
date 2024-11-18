# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    return lst[::-1]# Implement this
# print(reverse_list([1,2,3,4,5,6]))

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    return lst.count(element)# Implement this
# print(count_occurrences([1,1,3,4,5,6], 1))

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    return# Implement this
# print(get_keys_with_value({"nkulu": 1, "one": 2, "ayanda": 3, "tsepo": 4},1))

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    lst1 = lst1.sort()
    lst2 = lst2.sort()
    merged_list = lst2 + lst2
    print(merged_list)
    return merged_list.sort() # Implement this

# print(merge_sorted_lists([2,1,5,4,7,6], [0,9,8,11,10,20,15]))

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    ordered_list = numbers.sort()# Implement this
    return ordered_list[len(ordered_list) - 1]
# print(find_second_largest([2,1,5,4,7,6]))


def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    str1 = str1.upper()
    str2 = str2.upper()
    if str1.sort() == str2.sort():  # Implement this
        return True
    else:
        return False
print(is_anagram("gum", "mug"))


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    for i in nested_list():
        for I in nested_list[i]:
            if type(I) == type([[1,2,3]]):
                nested_list.append(I)
                nested_list[i].remove(I)
    return nested_list


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    set_list = set(lst)
    new_list = set_list.sort()
    return new_list


def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    commons_list = []
    
    if lst1 < lst2:
        for i in range(len(lst1)):
            if  lst1[i] in lst2:
                commons_list.append(i)
    return commons_list