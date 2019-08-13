print('its prime time!')

checkPrime = input('Enter an integer: ')

# find the range up to but not including the integer entered.
# disregard 0 and 1 loops
# From 2 to last in range, divide integer by that number using modulo
# if modulo ever equals 0, it's NOT PRIME

x = 0


def prime():
    print("It's prime!")


def notPrime():
    global x
    x += 1
    print('Not prime!')


for i in range(2, int(checkPrime)):

    if int(checkPrime) % i == 0:
        notPrime()
        break

print()
if x == 0:
    prime()


print('Sieve of Eratosthenes')

sieveNumber = input('Sieve: ')

sieveArray = []
for i in range(2, int(sieveNumber)+1):
    sieveArray.append(i)

for num in sieveArray:
    for i in range(1, sieveArray[-1]):
        value = num+num*i
        if value in sieveArray:
            sieveArray.remove(value)


print(sieveArray)
