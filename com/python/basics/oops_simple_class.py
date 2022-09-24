'''
    Create simple class Box
'''


class Box(object):
    def __init__(self, value):
        self.value = value

if __name__=='__main__':
    box1 = Box(1)
    print(box1.value)

    box2 = Box(2)
    print(box2.value)

    # Box is a class, box1,box2  is an object
    # Value (1,2) is object value , not a class value
