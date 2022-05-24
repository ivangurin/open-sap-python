
def is_prime(n):

    for i in range(2, n):
        if (n % i) == 0:
            return False
           
    return True

def prime_list(v):

    result = []

    for i in range(2, v+1):
        if is_prime(i):
            result.append(i)

    return result


number = int(input("Up to which number do you want all prime numbers: "))
print(prime_list(number))
