# Check if number is prime
def is_prime(num):
    for i in range(2,num//2):
        if num%i == 0:
            return False
    return True

prime_list = []
for i in range(1,201):
    if is_prime(i):
        prime_list.append(i)

print("The list of prime numbers ")
print(prime_list)
print("The list again in reverse ")
print(prime_list[-1:0:-1])
