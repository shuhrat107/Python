def max_of_three_1(a, b, c):
    return max(a, b, c)

print(max_of_three_1(10, 20, 15))

def max_of_three_2(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three_2(10, 20, 15))

def max_of_three_3(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

print(max_of_three_3(10, 20, 15))

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))  

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_list([1, 2, 3, 4, 5]))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def in_range(number, start, end):
    return start <= number <= end

print(in_range(5, 1, 10))

def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    return upper_count, lower_count

upper, lower = count_upper_lower('The quick Brow Fox')
print(f"Upper case: {upper}, Lower case: {lower}")  

def distinct_elements(lst):
    return list(set(lst))

print(distinct_elements([1, 2, 2, 3, 4, 4, 5]))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))

def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6]))


def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

print(is_perfect(28)) 

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))


def squares_list():
    return [i**2 for i in range(1, 31)]

print(squares_list())
