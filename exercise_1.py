N = input("Please enter a number N: ")
N = int(N)
even_sum=0
odd_sum=0
for number in range(1,N+1):
    if ((number%2)==0):
        even_sum=even_sum+number
    else:
        odd_sum=odd_sum+number
average=(even_sum/N)
print("The sum of odd numbers is", odd_sum)
print("The average of even numbers is", average)