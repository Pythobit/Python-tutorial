# if Statements
"""if statements allow our programs to make decision depending on the boolean"""
friend = 'Rolf'
username = input('Enter your name : ')
if True:
    print('Hello friend..!')    
# Above code will print 'Hello friend..!' only if the user input name as Rolf, otherwise nothing.
""" !! -- as true will be always true, so the print statement will be printed always. -- !! """
if username == friend:
    print('Hello friend..!')    # Output - Enter your name : bob
""" -- What will happen here is that python checks if username is equal to friend, 
if yes, then it will run the print statement inside it. else nothing will be printed -- """
""" SYNTAX
if username == friend }- Boolean Comparison, : }- Colon depicts the start of the body.
    body }- indentation is necessary, so python knows that these statements are inside if statements."""
"""as soon as you terminate the space in front of print statements, python will give an error.."""
"""     if [Bool]:  -- if true, returns print statment, otherwise else
            print()
        else:
            print()
using if and else at same time also known as "Compound if-Statement" -- """
# Things you put inside if condition, doesn't needs to be a bool comparison.
friends = ['Charlie','Smith']
family = ['Johny','Bob']
username = input('Enter your name : ')

if username in friends:
    print('Hello friend..!')
elif username in family:
    print('Hello Family..!')
else:
    print('I Don\'t know you..!')

""" !! -- !! IMPORTANT THINGS TO NOTICE !! -- !! """
# 01. Take care of INDENTATION, mostly beginners make a lot mistake in this
""" 02. AN Example - of not giving indentation properly will give an error.. """
"""
if username = friend:
    print('Hello friend ..!')
print('hello bello') -- Right here this statement will give an error, 
python interprets this as an error.
"""
# 03. from now onwards, i won't be giving the outputs, you have to try yourself..
# Any editor you like, i prefer to PyCharm..
