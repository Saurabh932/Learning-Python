"""
    Check Prime or Not
"""
def checkPrime(num):
    for i in range(2, num-1):
        if num%i == 0:
            return False
        else:
            return True
    
print(checkPrime(12))



"""
    Primes in Range 
"""

def primeRange(num):
    primeList = []
    
    for i in range(2, num+1):
        isPrime = checkPrime(i)
        if isPrime:
                primeList.append(i)
                
                
        else:
            continue
    
    return primeList
        
print(primeRange(11))