''''
    Input = 'PYTHON'
    Expected Out =
    P
    PY
    PYT
    PYTH
    PYTHO
    PYTHON
    PYTHON
    PYTHO
    PYTH
    PYT
    PY
    P

'''

if __name__ == '__main__':
    text = 'PYTHON'
    text_pattern = [text[0:index+1] for index in range(0,len(text))]
    reverse_text_pattern = text_pattern[::-1]
    print(*text_pattern+reverse_text_pattern,sep='\n')