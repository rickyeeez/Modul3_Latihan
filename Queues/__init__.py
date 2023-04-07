


queue = Queues(4)
queue.add("Java")
queue.add("DotNet")
queue.offer("PHP")
queue.offer("HTML")

print("Remove: " + queue.remove())
print("Element: " + queue.element())
print("Poll: " + queue.poll())
print("Peek: " + queue.peek())