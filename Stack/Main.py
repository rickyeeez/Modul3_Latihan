from Stack import Stack
Stack = Stack(5)
Stack.push("Aku")
Stack.push("Anak")
Stack.push("Indonesia")

print("Next : " + Stack.peek())
Stack.push("Raya")
print(Stack.pop())

count = Stack.search("Aku")
while count > 1:
    Stack.pop()
    count -= 1
print(Stack.pop())
print(Stack.isEmpty())