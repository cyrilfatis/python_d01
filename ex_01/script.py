import sys

cpt = 0
iterParam = iter(sys.argv)
next(iterParam)
for i in iterParam:
    for ii in i:
        if ii.isalnum():
            cpt += 1


print(cpt)
