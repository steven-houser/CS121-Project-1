# CS 121 Lab 1

**Author:** Steven Houser  
**Course:** CS 121 - Data Structures & Objects  
**Date:** 01/09/26

---

## About Me

### Learning Goals for the Semester

- Master the *CLI*
- Become proficient with **Vim** as my primary text editor
- Learn **data structures** and how to choose the right one for each problem
- Build strong habits with **Git** version control

### An Interesting Fact

I got into Computer Science by modding games and tinkering with technology, and now as a Cybersecurity major I want to learn how to build things from the ground up and help keep people safe online.

## Program Description

This program asks the user for their name and then greets them with a personalized welcome message.  
If the user does not type anything and just presses Enter, the program uses a friendly default name instead.

## Algorithm / Pseudocode

**Goal:** Create an interactive greeting program that always prints a friendly message, even if the user leaves their name blank.

**Variables needed:**
- `name` - stores the user's input (string)

**Steps:**

1. Display a prompt asking for the user's name
2. Read and store the input in the `name` variable
3. If `name` is empty (user just presses Enter), set `name` to `"friend"` and print a playful message
4. Print a greeting message that includes the (possibly updated) `name`
5. End program

```
START
    DISPLAY "What is your name? "
    READ name
    IF name is empty THEN
        DISPLAY "I didn't catch your name, so I'll just call you friend."
        SET name TO "friend"
    END IF
    DISPLAY "Hello, " + name + "! Welcome to CS 121!"
END
```

---

## How to Run

1. Open a terminal in the project folder
2. Run the command: `python3 hello.py`
3. Enter your name when prompted

*Created for CS 121 - Data Structures & Objects, Spring 2026*
