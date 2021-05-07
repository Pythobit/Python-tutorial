# Intro to Error Handling.
"""
Python has long history with errors.,
error are specially useful as they make code more readable.
We'll learn how you can create them, use them, or deal with them.,
at this very beginner stage no like errors.
"""
print(variable)
"""
Now, notice here, i haven't created my variable before printing it out, and the editor is already showing an error.

So, this code is perfectly reasonable in terms of syntax, python doesn't know whether it exist or not.
We got a NameError
    **
        Traceback (most recent call last):
            File "C:/Users/user/Desktop/Python/Introduction/error.py", line 8, in <module>
                print(variable)
        NameError: name 'variable' is not defined
    **

Here, Traceback is also known as StackTrace., this tells that where the error took place.
"""
# A Complex Traceback example
"""
It is important for you to read all these tracebacks, so you can solve your own errors.
    **
      Traceback (most recent call last):
       File "/Users/Pythobit/Course/Python/Intro/error.py", line 53, in <module>
        menu()  
       File "/Users/Pythobit/Course/Python/Intro/error.py", line 10, in menu  
        show_movies()
       File "/Users/Pythobit/Course/Python/Intro/error.py", line 36, in show_movies  
        show_movie_details(movie)
       File "/Users/Pythobit/Course/Python/Intro/error.py", line 40, in show_movie_details  
        print(f"Name: {movies['name']}")
      TypeError: list indices must be integers or slices, not str
    **
    
1. At Every bottom, it gives you the error that was raised and a description.
(i.e: TypeError: list indices must be integers or slices, not str)

2. what line of your code raised the error.
(i.e: line 53, in <module>)

3. What function that line is in
(i.e:  line 40, in show_movie_details)

4. What function called the function that line is in,
(i.e: File "/Users/Pythobit/Course/Python/Intro/error.py", line 40, in show_movie_details  
        print(f"Name: {movies['name']}") )

5. This shows same as above function called this function, similarly show_movies, and so-on, until you reach the file
that you executed.
"""
"""
 ## CODE THAT RAISED THE ERROR..! ##

***
    def add_movie():
        name = input("Enter the movie name: ")
        director = input("Enter the director: ")
        year = input("Enter the release year: ")
    
        movies.append({
            'name' : name,
            'director' : director,
            'year' : year
        })
    
    def show_movies(movies_list):
        for movie in movie_list:
            show_movie_details(movie)
    
    def show_movie_details(movie):
        print(f"Name: {movies['name']}")
        print(f"Director: {movie['director']}")
        print(f"Year: {movie['year']}")
***

// I'm sure that you remember this code, as we written this in our first milestone project 1
Error in line..!
      print(f"Name: {movies['name']}")
      
* Here, We're accessing dictionary, but here as in line 80, we defined a list and movie parameter is passed as an
dictionary from show_movies function.

## TIPS TO GET ERROR RESOLVED EASILY. ##

1. Look at your code.
2. Put the error message onto google, see if something comes up in stackoverflow.
3. Look at your code, this time more slowly, run through it as, if you were a machine/computer, do you notice 
that could potentially be some of error.
4. Run only some part of code in isolation, that'll help you to identify which part of your code is giving error.
5. Use a Debugger ( We'll learn in next couple lectures, PyCharm has an excellent debugger.,
 debugger helps you to stop at any line containing error line by line.)
"""
