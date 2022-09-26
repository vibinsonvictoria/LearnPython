'''

    input : [('boys' ,1),('girls',21),('boys',3),('boys',34)]
    output : [{'boys': 38}, {'girls': 21}]
    Desc : Group by key and sum key values

'''

if __name__ == '__main__':
    lst = [('boys' ,1),('girls',21),('boys',3),('boys',34)]
    count = {}
    # res = [count.setdefault(gender,[]).append(cnt) for gender,cnt in lst]
    # print(res)
    for gender,cnt in lst: count.setdefault(gender,[]).append(cnt)
    res = [{gender: sum(values)} for gender,values in count.items()]
    print(res)
