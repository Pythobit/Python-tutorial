Hey!

In the next lecture, Windows users might encounter a small issue.

Due to the way Windows forks processes, you must make sure that the code that starts a process is surrounded by *if __name__ == "__main__"*.

Otherwise when we start new processes on Windows, those processes automatically start new processes, and those start new ones, and so on. Python will not allow this to happen, and as protection it requires the above if statement.

So in the next video, when you see something like *process.start()_*, make sure to do:

```python
if __name__ == "__main__":
    process.start()
    ...
    process.join()
```
> It's important that all the code in between starting the process and joining the process is inside the if statement.
