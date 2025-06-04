max_range = int(input("Enter N value to check for PRIMES: "))

def is_prime(elm) -> bool:
    for div in range(2,(elm//2)+1):
        if elm%div == 0:
            return False
        
    return True

for num in range(2,max_range+1):
    if is_prime(num):
        print(f"{num} is PRIME")

