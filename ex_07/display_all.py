def display_all(dico):
    lValue = list(dico.values())
    for i in lValue:
        str_type = str(type(i))
        str_type = str_type.replace("<class '", "")
        str_type = str_type.replace("'>", "")
        print("(" + str_type + ": " + str(i) + ")")

# display_all({"a": 1, "b": 2})