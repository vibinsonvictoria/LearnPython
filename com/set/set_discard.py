
if __name__ == '__main__':
    s = {1,2,3,4,5,6,7}
    print(f'Original set : {s}')
    s.discard(2)
    print(f'After removing the item (2) : {s}')
    s.discard(100) # it will throw any error if value not found in set
    print(f'After removing the item (100) : {s}')