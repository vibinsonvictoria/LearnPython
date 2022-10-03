'''

'''

def approach_1():
    message_queue_response = ['success','success','success','failure','success']
    is_all_message_sent =True
    is_failure_found = False # Need special variable to monitor the status

    for status in message_queue_response:
        if status =='failure':
            print('Found failure message.')
            is_failure_found =True
            break

        else:
            print('Message sent successfully')

    if not is_failure_found:
        print('All messages were sent successfully. There is no failure.')


def approach_2():
    message_queue_response = ['success','success','success','failure','success']

    for status in message_queue_response:
        if status =='failure':
            print('Found failure message.')
            break
        else:
            print('Message sent successfully')

    else:
        print('All messages were sent successfully. There is no failure.')


if __name__== '__main__':
    approach_1()
    print('*'*20)
    approach_2()