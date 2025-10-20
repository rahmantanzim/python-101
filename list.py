fruites = ['apple','banana','cherrry']
print(fruites)
f2 = fruites[1]

# List items are indexed
print(f"The selcted fruite is: {f2}")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1:3])

out = []
for x in range(1, 21):
    if x%3==0:
        out.append(x*x)
        
        
output = [x*x for x in range(1,21) if x%3 ==0]
print(output)
