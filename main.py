'''
TASK 1:
Given a string (the input will be in the form of an array of characters), write a function that returns the reverse of the given string.

TIME AND SPACE COMPLEXITY:
O(n)
'''
def csReverseString(chars):
    reverse_str = chars[::-1]
    return reverse_str



'''
TASK 2:
A palindrome is a word, phrase, number, or another sequence of characters that reads the same backward or forward. This includes capital letters, punctuation, and other special characters.

Given a string, write a function that checks if the input is a valid palindrome.


TIME AND SPACE COMPLEXITY:
The time and space complexity for this solution would be O(n). The string transformations are applied to each of the texts characters. 
'''

def csCheckPalindrome(input_str):
    reverse_input = input_str[::-1]
    
    if input_str == reverse_input:
        return True
    else:
        return False


'''
TASK 3:
Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.


TIME AND SPACE COMPLEXITY:
O(n) and O(1) space complexity
'''

def csRemoveDuplicateWords(input_str):
    remove_dups = input_str.split()
    return(" ".join(sorted(set(remove_dups), key=remove_dups.index)))
