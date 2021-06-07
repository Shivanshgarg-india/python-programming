
# while loop
count = 0
while (count < 5): count += 1; print("hey!!!")


# while with continue
i = 0
a = 'Shivansh'

while i < len(a):
    if a[i] == 'i' or a[i] == 'n':
        i += 1
        continue
    print('Current Letter :', a[i])
    i += 1


# while with break
i = 0
a = 'Shivansh'

while i < len(a):
    if a[i] == 'i' or a[i] == 'n':
        i += 1
        break
    print('Current Letter :', a[i])
    i += 1



# while with pass

a = 'shivansh'
i = 0

while i < len(a):
    i += 1
    pass
print('Value of i :', i)