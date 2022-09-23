'''

    input = [[1,2,3,4],[5,6,7],[8,9,10]]
    output =[1,2,3,4,5,6,7,8,9,10]
'''

if __name__=='__main__':
    lst = [[1,2,3,4],[5,6,7],[8,9,10]]
    print(f'The given list : {lst}')
    flattern_lst = [value for rows in lst for value in rows]
    print(f'The flattern list : {flattern_lst}')

