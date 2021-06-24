def reverse_words(sentence):
    words = sentence.split(' ')
    print(' '.join((words[::-1])))

def reverse_individual_words(sentence):
    words = sentence.split(' ')
    words = [word[::-1] for word in words]
    print(' '.join(words))

s = 'Geeksforgeeks is the best website'
reverse_words(s)
reverse_individual_words(s)