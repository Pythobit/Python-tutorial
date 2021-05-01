# 12. Length & Sum

grades = [80,75,100,90]

total = sum(grades)
length = len(grades)
average = total/length
print(average)      # Output - 86.25

# NOW, HERE IS A QUESTION,
# Q. Which of the following data structures is not-ideal for grades

grades = [80,75,100,90]
grades = {80,75,100,90}
grades = (80,75,100,90)

# - SET is the worst, as you cannot make any modification in it.
# - TUPLE is somewhat bad, unless you need modification.
# - LIST is the safest.
