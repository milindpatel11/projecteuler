#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

##Step 1:making list of Fibonacci sequence

start = 1
next = start + 1
list_fib = [start, next]

while list_fib[-1] < 4000000:
    curr_fib = list_fib[-1] + list_fib [-2]
    list_fib.append(curr_fib)

Print("Testing for correct sequence")
print(list_fib)

##Step 2: sum of the even Fibonacci numbers
final_sum = 0

for i in list_fib:
  if i % 2 == 0:
    final_sum += i

print("Final Answer is")
print (final_sum)
