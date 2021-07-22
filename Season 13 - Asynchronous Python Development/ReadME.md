# A Glossary of terms used in Concurrency

- **Synchronous**: actions that happen one after another. Programming as we've seen it until now is synchronous, because each line executes after the previous one.
- **Asynchronous**: actions that don't necessary happen after one another, or that can happen in arbitrary order ("without synchrony").
- **Concurrency**: The ability of our programs to run things in different order every time the program runs, without affecting the final outcome.
- **Parallelism**: Running two or more things at the same time.
- **Thread**: A line of code execution that can run in one of your computer's cores.
- **Process**: One of more threads and the resources they need (e.g. network connection, mouse pointer, hard drive access, or even the core(s) in which the thread(s) run).
- **GIL**: A key, critical, important resource in any Python program. Only one is created per Python process, so it's unique in each.
