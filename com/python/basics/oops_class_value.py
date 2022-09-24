class Box(object):
    class_name ='Container_box'
    def __init__(self,value):
        self.value = value

if __name__ =='__main__':
    box1 = Box(1)
    print(box1.value) # object variable
    print(Box.class_name) #Class Variable.
    '''
        1.How to access class variable ?
            ClassName.variable 
            ex. Box.class_name
        2. How to access instance/object variable?
            object_name.variable
            ex. box1.value
            
        
    '''