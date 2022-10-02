
if __name__ == '__main__':
    s = {1,2,3,4,5,1,2,2}
    print(f'original set : {s}') # removed duplicate automatically
    s.remove(2)
    print(f'After remove : {s}')
    