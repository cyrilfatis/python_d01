def my_args_handler(*args):
    str = ""
    cpt = 1
    maxargs = len(args)

    for i in args:
        if cpt < maxargs:
            str += i + ','
        else:
            str += i
        cpt += 1

    return str

#print(my_args_handler("bob", "bib"))
