def is_prime(num):
    count = 0
    z = 1
    while True:
        if z == num + 1:
            break
        if count > 2:
            break;
        if num%z == 0:
            count += 1
        z += 1
    if count == 2:
        return True
    else:
        return False

def solution(num1, num2):
    primes = []
    for i in range(num1, num2+1):
        if is_prime(i):
            temp = str(i)
            add = 0
            for j in range(len(temp)):
                add = add + int(temp[j])
            if is_prime(add):
                primes.append(i)
    return(primes)


num1 = 20
num2 = 50
print(solution(num1, num2))