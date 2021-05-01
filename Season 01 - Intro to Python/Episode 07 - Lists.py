# 7. Lists

freinds = ["Pythobit","Boy"]
print(freinds[0])       # Output - Pythobit
print(len(freinds))     # Output - 2

freinds = [["Pythobit",20],["Boy",21]]
print(freinds[0][0])    # Output - Pythobit
print(freinds[1][1])    # Output - 21

freinds = ["Pythobit","Boy"]
freinds.append("Pythobit boy")
print(freinds)      # Output - ["Pythobit", "Boy", "Pythobit boy"]

freinds = ["Pythobit","Boy","Pythobit boy"]
freinds.remove("Pythobit")
print(freinds)      # Output - ['Boy', 'Pythobit boy']
