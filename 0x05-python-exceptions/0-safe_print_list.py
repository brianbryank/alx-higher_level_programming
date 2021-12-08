#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    li = 0
    for i in range(0, x):
        try:
            print(my_list[i], end="")
            li += 1
        except:
            break
    print()
    return (li)
