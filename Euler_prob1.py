##Multiples of 3 and 5
#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

curr_num = 1

list_nums = []


while curr_num < 1000:
  if curr_num % 3 == 0 or curr_num % 5 ==0:
    list_nums.append(curr_num)
  curr_num += 1

#print(list_nums)

result = 0
for i in list_nums:
  result += i


print("The sum is: ") 
print(result)



### Longer slution gotten on the first try
''' 
curr_num = 1

mult_3 = []
mult_5 = []

while curr_num < 1000:
  if curr_num % 3 == 0:
    mult_3.append(curr_num)
  elif curr_num % 5 == 0:
    mult_5.append(curr_num)

  curr_num += 1

#print(mult_3)
#print(mult_5)

result = 0

for i in mult_3:
  result += i

for i in mult_5:
  result += i

print("The sum is: ") 
print(result) '''
