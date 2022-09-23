
def recursivesum(lst):
    if len(lst) == 1 :
        return lst[0]
    else:
        return lst[0] + recursivesum(lst[1:])

if __name__=='__main__':
    total = recursivesum(list(range(1,1000))) #if you change end value to 100000000000, you will get Memory Error.
    print(total)