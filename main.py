# Task 1 Palindrome using python
# Arif Febrianto

# Function to check a number is palindrome or not
def is_palindrome(num):
    temp = num
    rev = 0
    while (temp > 0):
        rem = temp % 10
        rev = (rev * 10) + rem
        temp = temp // 10

    return num == rev

# Function input value and result output value
def main():
    num = int(input("Input: "))
    num = num + 1

    while (True):
        if (is_palindrome(num)):
            break
        num = num + 1

    print(f"Output: {num}")

if __name__ == '__main__':
    main()