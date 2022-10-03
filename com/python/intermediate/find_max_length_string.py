
'''

    input =  ['Hi','How','are','i','am','fine']
    output = fine
    input =  ['Hi','How','are','i','am','fine''when','will','you','come']
    output= ['fine','when','will','come']


'''


if __name__ == '__main__':
    lst = ['Hi','How','are','i','am','fine','when','will','you','come']
    max_word_len = len(max(lst,key=len))
    print(max_word_len)

    # second iteration

    max_words = [ element for element in lst if max_word_len == len(element)]
    print(max_words)

