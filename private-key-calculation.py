#function for the prime numbers derived from the value (n)
def prime_numbers(n):
    primeNumber = [] 
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            primeNumber.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return primeNumber #end of function to calculate the prime number

#function for the phi 
def phivalue(p, q):
    phi_value = (p-1) * (q-1)
    return phi_value    #end of function to calculate the phi

#function to calculate the value d 
# private key (KR) = {d,e}
def calculate_d_value(e, phi): #parameters for the equation
    d = pow(e, -1, phi) #formula for the d
    return d  #end of the function to calculate the value of d

#check that non-integers are not entered
while True: #This line ensure that only integers are provided for e and n
    try:
        #Provide input of the values e and n provided
        e = int(input("Enter the value of e: ")) #The e value
        n = int(input("Enter the value of n: ")) #The n value
        break
    except ValueError:
        print("Only integer numbers are acceptable")
        
primeNumber_value = prime_numbers(n) #This call the function to calculate prime numbers defined on line 1 and put the result into an array (primeNumber)

# append the output of the two variables into variable p and q
p = primeNumber_value[1]
q = primeNumber_value[0]
print("The two prime numbers of n=", n, "are:", p, "and", q) #this print out the prime numbers

# Calculate the phi value
phi = phivalue(p, q) #call the function for phi defined on line 14
print("The value of p=", p, "and the value of q=", q, "give the phi value of:", phi) #This print out the phi value

d = calculate_d_value(e, phi) #call the function of d defined on line 19 ; find d
print("The value of d=",d) #This print out the value of d

private_key = (d, n) #This put the value of d and n together into same array and append it to variable private_key
print()
print("THE PRIVATE KEY OF THIS USER IS", private_key) #output of the private key

