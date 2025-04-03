import queue
from collections import deque

##funcion para la union
def union(cola1, cola2):
    result = deque(cola1)
    for element in cola2:
        if element not in result:
            result.append(element)
    return result
##funcion para la interseccion
def intersection(set1, cola2):
    result = deque()
    temp = deque(set1)
    while temp:
        element = temp.popleft()
        if element in cola2:
            result.append(element)
    return result
cola1 = deque(['A', 'B', 'C'])
cola2 = deque(['D', 'A', 'F'])
print("A: ", cola1)
print("B: ", cola2)
union_result = union(cola1, cola2)
##print("Union: ", union_result)
intersection_result = intersection(cola1, cola2)
##-----

##print("Inter: ", intersection_result)
print("Union:")
print("A U B:", union_result)
print("Interseccion:")
print("A ∩ B", intersection_result)
