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

- Jython allows Pyton to integrate with Python. Dope.
- CPython allows Python to script C and C++ components.
- Iron Python allos integration with .NET and open source Linux equivilent (Mono). Lets Python programs act as both client and server.

~~~~~QUIZ~~~~~

1) A program that runs the Python files you write
2) Source code is the code the programmer writes
3) Byte code is what souce code gets compiled into, its Python specific and intpreted by the PVM
4) The PVM is the hardware that interprets Byte code, similar to how a CPU interprets machine code for C
5) Psyco JIT Compiler; enchances PVM to translate portions of the byte code all the way down to binary machine code. It collects info about objects being used and generates machine code for those object types. The longer the run, the faster it runs. Psycho. Shedskin C++ translates the source code to C++, then computers compiler turns the C++ into machine code. Frozen binaries pack and ship bundles of byte code along with interpreters of your program files and its executable in binary, and as such can be used by customers.  
6) CPython is most used and the one that comes with most machines, it interfaces easily with C. Jython interfaces with Java, however, most Java developers use it to write Python extensions, not the other way around, and IronPython allows you to interface with .NET at the open source version of Linux. They are alternative compilers for Python.
