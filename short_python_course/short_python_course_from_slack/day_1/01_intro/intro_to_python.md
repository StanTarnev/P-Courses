# Introduction to Python

**Duration: 20 minutes**

## Learning Objectives

- Understand the key features of Python, and where it is used
- Be aware of some of issues around Python 2 vs Python 3
- Be able to use Atom to save and run a Python script

## Introduction

The Python programming language was created by the Dutch engineer Guido Van Rossum in the early 1990s. In contrast with other programming languages of that time, it was designed to be _fun_. This is reflected in the name of the language, which is named after Monty Python's Flying Circus - not the snake!

Python is a general purpose programming language; it is intended to be used to solve a wide variety of problems in computing, such as:

- Building desktop and web applications
- Solving scientific and statistical problems
- Providing scripting support for other software applications, particularly multimedia apps
- Artificial intelligence and data science

As a language, Python has a clear, readable syntax. Perhaps its most notable feature is its use of whitespace to denote blocks of code, rather than the curly brackets that you might see in other programming languages.

Its community places quite an emphasis on aesthetics. It's common to hear code being described as _Pythonic_ - this is code that meets the community's idea of how Python code should be. This philosophy is laid out in a document called [The Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3).

## A short note about version numbers

In this course, we'll be using Python 3, as it is the current and future implementation of Python.

Unfortunately, many computers still come with Python 2 rather than Python 3. However, the content of this course has been written in such a way that it should work on either version of Python.

## Atom

When Python is installed, it comes with a program known as IDLE: the <b>I</b>ntegrated <b>D</b>evelopment and <b>L</b>earning <b>E</b>nvironment.

This is OK for writing and testing small snippets of python code but we will be building fully-fledged programmes.

There are many, many other ways of writing Python. It's common to use the terminal, and any number of text editors, or [development environments](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).

We will be using a text editor called Atom, which provides a number of benefits:

- It is free
- It is cross-platform
- It provides syntax highlighting / colouring

Let's start coding some Python!


## Starting off

We will need to install python 3 onto our machines.

To do this open a terminal and run the following command:

```bash
  brew install python3
```

Next in terminal we will create a python file.

We do this by running the touch command in terminal and creating a file with a `py` extension.

```bash
touch hello_world.py
```

Next we will open this file in Atom.

To do this we could use the command `atom hello_world.py`.

This will only give us access to this single file though.

Later we will have multiple files so we want to be able to see all of these in atom.

To do this we can tell atom to open and show all files in the folder we are in by running the command `atom .` in the terminal.

When atom opens you will see a project pane on the left hand side showing all the files in the current folder (we only have one so far!)

Double click the `hello_world.py` file to open it in the editor pane.

Now we can write some python in here.

```python
#hello_world.py

print("Hello World!")
```

Save the file and let's run it in the terminal.

We want to use python 3 to run this so we give the command:

```bash
python3 hello_world.py
```

Ace! We now see `Hello World!` printed out in our terminal.

## Variables

We can also assign values to variables to call on them later on.

Change the code in hello_world.py to the following.

```python
#hello_world.py

my_name = "John"
print(my_name)
```

When we save and run this in terminal again we should see `John` printed out.

## Setting Python3 alias.

This is all good and well but we may want to run python 3 as the default.

At the moment if we were to just run `python` in the terminal it will use python 2. We want this to be python 3.

```bash
python

Python 2.7.16 (default, Jun 19 2019, 07:40:37)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To do this we can set the `python alias` in our bash (zsh) profile.

```bash
atom ~/.zshrc
```

Scroll to the bottom of this file and add the line:

```bash
# .zshrc
alias python=/usr/local/bin/python3
```

And back in the terminal reload the profile

```bash
source ~/.zshrc
```
Now if we run python from terminal it will default to Python 3.


```bash
python

Python 3.7.5 (default, Nov  1 2019, 02:16:23)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Conclusion

We've seen how to write and execute a small program using Atom and the terminal. Let's learn more about the Python language, starting with variables, and types.
