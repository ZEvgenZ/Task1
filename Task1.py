def string(arg):
    print("Hello, %s!" % (arg))


string("world")

def sum(s):
    k = 0
    for i in s:
        k = k+i
    return k

s = [1, 2, 3, 4]

print(sum(s))

def multiply(s):
    k = 1
    for i in s:
        k = k*i
    return k

s = [1, 2, 3, 4]

print(multiply(s))


def reverse(str):
    print(str[::-1])


reverse('I am testing')

def isPalindrome(num):
    return num == num[::-1]


print(isPalindrome("radar"))


def histogram(str):
    for i in range(0, len(str)):
        #print(str[i])
        print('*' * str[i])
    return


histogram([4, 9, 7])


f = 'abcdefghijklmnopqrstuvwxyz'


def caesarCipher(number, string):
    result = ''
    for i in string.lower():
        try:
            k = (f.index(i) + number) % 26
            result += f[k]
        except ValueError:
            result += i
    return result.lower()


print(caesarCipher(9, "Hello, world!"))


