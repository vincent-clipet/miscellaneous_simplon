array = []

array.append(int(input("A ?\n")))
array.append(int(input("B ?\n")))
array.append(int(input("C ?\n")))

array = sorted(array)
print(array[-1])

print("Biggest : " + str(array[-1]) + "\n")