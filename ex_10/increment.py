import sys
def increment(a_list):
    n_list = []

    for i in a_list:
        try:
            int(i)
            for x in range(i + 1, i + 2):
                print(x)
        except ValueError:
            print(i)


increment([1, 2, 3, 'a', {}])
