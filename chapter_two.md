- 2to3 automatic code conversion script is available to migrate python 2 files to python 3 files
- scope of book is fundamentals, bottom up, not necessarily getting you to write programs right off the bat
- use in conjunction with writing a program (i.e. space adventure)
- concepts, small examples, and sometimes omits small details
- stepping stone to larger texts and tasks

- you are not writing software for yourself. You aren't even writing it for the computer.  You are writing for the next human who has to read your code and maintain it or reuse it. Otherwise your code is useless!

- when you run a python program, python compiles your source code (the stuff i write) into byte code.
- byte code: lower level platform independent representation of source code
- byte code of your programs are stored in files that have .pyc extension (aka compiled .py)
- this is saved to optimize startup speed - then it doesn't have to compile next time
- make sure these are written for larger files (give write access to the python process)
- python can run .pyc files EVEN WITHOUT THE ORIGINAL .py source files
- Python virtual machine is just the run time engine of Python, its always there, and its the thing that actually runs the scripts. It's the last step of the "interpreter"
- All of this is hidden. There's no build step like in C or C++. Also its not binary machine code (whoa!) Its python-specific representation of the code. The PVM loop has to interpret it not the CPU chip (hence why its not AS fast as C, requires more work)
- all we have is runtime, no compile time, everything happens as programming is running. Its all happening (creation of classes, variables, methods, libraries being linked) AS THE PROGRAM IS RUNNING, not before it runs like in static languages.
