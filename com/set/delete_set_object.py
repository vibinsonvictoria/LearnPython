
if __name__ == '__main__':
    s = {1,2,3,4,5,1,2,2}
    print(f'original set : {s}') # removed duplicate automatically
    del s
    #print(f'After remove : {s}') #Erro - You will get NameError. del s - it will remove the object from memory.
