'''
    input = 'PYTHON'
    output = PTO
'''

if __name__ == '__main__':
    input = 'PYTHON'
    output = [ch for index,ch in enumerate(input) if index%2 ==0 ]
    print(*output,sep='')

