# Queue simulation using list
queue = []

queue.append("A")
queue.append("B")
queue.append("C")

while queue:
    person = queue.pop(0)
    print("Serving:", person)
