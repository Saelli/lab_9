# Eleonora
# 19 November 2024

#i = 1
# while i == True:
  #print("Infinite")

# Write an infinite loop that prints “Infinite”. An infinite loop never ends. The condition is always true. After you prove to yourself that this works, comment out the code that produces the infinite loop. To break a loop in progress you should be able to do ctrl-C or command-C (depending on your platform)
  

#list = [57, 83]

#counter = 0

#while counter <= 10:
 #   list.append(counter)
  #  counter += 1

#print(f"The list contains {len(list)} elements.")
#print(f"The third element in the list is {list[2]}.")



# Create a list called L that starts with the numbers 57 and 83 in it. Then build a while loop, starting with a counter assigned to the value 0. On each iteration, the loop should append the current value of a counter variable to the list and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10. Finish by printing a statement that tells us a) how many elements are in the list, and b) what the third element in the list is.

numbers = []

total = 0

while total <= 100:
    num = float(input("Enter a number: "))
    numbers.append(num)
    total += num

print(f"The numbers entered are: {numbers}")
print(f"The total sum is: {total}")
#  Using a while loop, ask the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100.