# Start with some pseudo-code!


# number from 1 until 100 (loop)
#   if number is divisable by 3
#       print "fizz"
#   if number is divisiable by 5
#       print "buzz"
#   if number is divisable by 3 and 5
#       print "fizzbuzz"
#   else
#       print "wrong answer
    


for number in range(1, 100 + 1):
    if (number % 3) == 0 and (number % 5) == 0:
        print("Fizzbuzz")
    elif (number % 3) == 0:
        print("Fizz")
    elif (number % 5) == 0:
        print("Buzz")
    else:
        print(number)
   
 

    