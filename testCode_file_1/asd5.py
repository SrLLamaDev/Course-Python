from queue import Queue

def union(cola1, cola2):
    result = Queue()
    while not cola1.empty():
        element = cola1.get()
        if element not in cola2.queue:
            result.put(element)
    while not cola2.empty():
        element = cola2.get()
        if element not in cola1.queue and element not in result.queue:
            result.put(element)
    return result

def intersection(cola1, cola2):
    result = Queue()
    temp = Queue()
    while not cola1.empty():
        element = cola1.get()
        temp.put(element)
        if element in cola2.queue:
            result.put(element)
    while not temp.empty():
        cola1.put(temp.get())
    return result

cola1 = Queue()
cola1.put('A')
cola1.put('B')
cola1.put('C')

cola2 = Queue()
cola2.put('D')
cola2.put('A')
cola2.put('F')

print("A: ", list(cola1.queue))
print("B: ", list(cola2.queue))

union_result = union(cola1, cola2)
print("Union: ", list(union_result.queue))

intersection_result = intersection(cola1, cola2)
print("Inter: ", list(intersection_result.queue))
