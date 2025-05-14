#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            num = my_list_1[i]
            den = my_list_2[i]
            result = num / den
            result_list.append(result)
        except (TypeError, ValueError):
            print("wrong type")
            result_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            pass
    return result_list
