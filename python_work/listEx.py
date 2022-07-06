bicycles = ['12345', 'trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

print(bicycles[-1])

bicycles.append('honda')

print(bicycles[-1])

bicycles.insert(0, "abc")
print(bicycles)

del bicycles[0]
print(bicycles)


print(bicycles)
x = bicycles.pop()
print(f"{x} {bicycles}")
