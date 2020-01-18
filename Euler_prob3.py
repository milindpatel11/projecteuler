#Largest prime factor

#Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


big_num = 600851475143

list_fact = []

for i in range(2, big_num):
  if big_num % i == 0:
    list_fact.append(i)
    i += 1
  
print(list_fact)

prime_list = [] 



for i in list_fact:    #((for list 2,3,6,9))
  temp_fact_list=[]
  for j in range(1,i+1):  #((from 2 to number in list))
    if i%j == 0:
      temp_fact_list.append(j)
  if len(temp_fact_list) <= 2:
    prime_list.append(i)

''' for i in range(2,9):
  print(i) '''

print("List of Prime Factors:")
print(prime_list)
print("Largest Prime Factor is:")
print(max(prime_list))
