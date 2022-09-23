'''
    input = 'PYTHON'
    output = PTO
'''

if __name__ == '__main__':
    input = 'PYTHON'
    output = [input[pos] for pos in range(0, len(input), 2)]
    print(f'The given String {input}')
    print(*output, sep="")
