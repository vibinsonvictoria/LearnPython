

def find_sum_tail_recursion(lst,sum=0):
    print(sum)
    if lst:
        return find_sum_tail_recursion(lst[1:],sum+lst[0])
    else:
        return sum


if __name__ == '__main__':
    lst = list(range(1,1000))
    result = find_sum_tail_recursion(lst)
    print(result)