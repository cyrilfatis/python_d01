def display_all(a_list):
    for i in a_list:
        print(str(a_list.index(i)) + "->(" + str(type(i)).replace("<class '", "").replace("'>", "") + ": " + str(i) + ")")


#display_all([5, 2])
