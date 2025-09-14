list1 = [10, 3, 7, 9]
list2 = ["python", "is", "a programming language"]
list3 = [9, True, "string"]
# Listen können mehrere Datentypen halten

allLists = [
    list1,
    list2,
    list3
]
# Man kann eine Liste von Listen machen

print("Original lists:")
print(*allLists,sep='\n')

list1.pop(0)
list2.remove("python")

list1.append(12)
list2.insert(0, "Java")
list3[1] = False

print("\nModified lists:")
print(*allLists,sep='\n')
# Man kann Elemente von Listen nach Indizien (indexes) 
# oder Inhalten löschen, addieren, ändern
