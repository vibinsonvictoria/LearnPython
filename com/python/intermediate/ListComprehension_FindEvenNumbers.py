'''

    find odd number from the list using List comprehension

'''

if __name__ == '__main__':
   lst = list(range(1,11))
   print(f'The given list :{lst}')
   odd_numbers = [number for number in lst if number%2==0]
   print(f'The odd numbers are {odd_numbers}')