'''
    List:
        - Ordered collection. But not sorted
        - Access via index
        - Add methods are
            append(element) - add element at the end.
            insert(index,element) - insert an item at specified index
            extend(anotherlist) - Append elements from anotherlist to the current list
                anotherList - should be iterable
'''


if __name__ =='__main__':
    friends = ['chris','daniel','francis','mark']
    add_friend_using_append = 'silva'
    friends.append(add_friend_using_append) # Key note :  adding element at the end and adding into original list
    print(friends)
    add_friend_using_insert = 'Rony'
    friends.insert(1, add_friend_using_insert) # index start with 0. new element inserted at 1,
    print(friends)
    friends.insert(100, 'victoria') # if index(100) > len(list(friends)) then element will add at end of the list.
    print(friends)

    facebook_friends = ['roy','james']

    friends.extend(facebook_friends) # add element from facebook_friends to existing list.
    print(friends)

    new_friends_obj_list = friends + facebook_friends # it will create new List.
    print(new_friends_obj_list)




