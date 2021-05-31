# read from questions.txt and append each line into a list
questions = open("questions.txt", "r")  # read from questions.txt

# read all lines and get rid of line break for each line, then append each stripped line to a list
question_list = [line.strip() for line in questions]
questions.close()

score = 0  # initialize score
total = len(question_list)  # set total score

for line in question_list:
    # split equation with `=` into question and answer
    q, a = line.split("=")

    # print question and wait for user to input their answer
    ans = input(f"{q}=")

    if a == ans:  # if user input matches answer
        score += 1  # increase score

result = open("result.txt", "w")  # open result.txt
# write final score to result.txt
result.write(f"Your final score is {score}/{total}.")
result.close()


