# Palindrome
def palindrome(input):
    if len(input) == 1:
        print('Word is only one character long, trivially it is a palindrome.')
        return
    i = 0
    j = len(input)-1
    input = list(input)
    print(input)
    print('Start index:',i,'End index:',j)
    while i < j:
        print('Checking if',input[i],'is equal to',input[j])
        if input[i] != input[j]:
            print('Not a palindrome!')
            return
        else:
            i+=1
            j-=1
    print('Word is a palindrome!')
    return

if __name__ == "__main__":
    inp = input('Enter a word to check: ')
    palindrome(inp)
