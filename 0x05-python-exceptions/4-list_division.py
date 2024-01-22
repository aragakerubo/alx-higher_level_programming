#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Function that divides element by element 2 lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list with the result of the division.
    """
    result = []
    for index in range(list_length):
        try:
            result.append(my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
