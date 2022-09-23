'''

    input = ['apple','orange','orange','apple','bannana','guva']
    output = {'apple':2,'orange':2,'bannana':1,'guva':1]
'''

if __name__ == '__main__':
    fruits = ['apple', 'orange', 'orange', 'apple', 'bannana', 'guva']
    fruit_count = {fruit: fruits.count(fruit) for fruit in set(fruits)}
    print(fruit_count)
