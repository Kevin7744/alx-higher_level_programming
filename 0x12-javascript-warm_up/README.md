# 0x12. JavaScript - Warm up

## Tasks Explanation

### 0. First constant, first print
- Created a script that prints "JavaScript is amazing."
- Used a constant variable called `myVar` with the value "JavaScript is amazing."
- Utilized `console.log(...)` to print the output.
- Not allowed to use `var`.

### 1. 3 languages
- Implemented a script that prints three lines: "C is fun," "Python is cool," and "JavaScript is amazing."
- Utilized `console.log(...)` for printing.
- Avoided the use of `var`.

### 2. Arguments
- Developed a script that prints a message based on the number of arguments passed.
- Conditions:
  - If no arguments: "No argument"
  - If one argument: "Argument found"
  - If more than one argument: "Arguments found"
- Used `console.log(...)` for output.
- Avoided the use of `var`.
- Referenced `process.argv` for argument handling.

### 3. Value of my argument
- Created a script that prints the first argument passed to it.
- If no arguments, printed "No argument."
- Used `console.log(...)` for output.
- Avoided the use of `var` and `length`.

### 4. Create a sentence
- Developed a script that prints two arguments passed to it in the format: "`<arg1>` is `<arg2>`."
- Used `console.log(...)` for output.
- Avoided the use of `var`.

### 5. An Integer
- Implemented a script that prints "My number: `<first argument converted to an integer>`" if the first argument can be converted to an integer.
- If not a number, printed "Not a number."
- Used `console.log(...)` for output.
- Avoided the use of `var`.
- Avoided using try/catch for error handling.

### 6. Loop to languages
- Created a script that prints three lines using an array of strings and a loop.
- Utilized `console.log(...)` for output.
- Avoided the use of `var` and any if/else statement.
- Used a loop (while, for, etc.).

### 7. I love C
- Developed a script that prints "C is fun" x times, where x is the first argument.
- If no argument provided, printed "Missing number of occurrences."
- Used `console.log(...)` for output.
- Avoided the use of `var`.
- Used a loop (while, for, etc.).

### 8. Square
- Implemented a script that prints a square using the character 'X'.
- The size of the square is provided as the first argument.
- If the argument can't be converted to an integer, printed "Missing size."
- Used `console.log(...)` for output.
- Avoided the use of `var`.
- Used a loop (while, for, etc.).

### 9. Add
- Created a script that prints the addition of two integers.
- The integers are taken as the first and second arguments.
- Defined a function with the prototype: `function add(a, b)`.
- Used `console.log(...)` for output.
- Avoided the use of `var`.

### 10. Factorial
- Developed a script that computes and prints a factorial.
- The integer for computing the factorial is provided as an argument.
- If no argument, printed 1 (factorial of NaN).
- Implemented the factorial calculation recursively.
- Used `console.log(...)` for output.
- Avoided the use of `var`.

### 11. Second biggest!
- Implemented a script that searches for the second biggest integer in the list of arguments.
- Printed 0 if no arguments or only one argument is provided.
- Used `console.log(...)` for output.
- Avoided the use of `var`.

### 12. Object
- Updated a script to replace the value 12 with 89 in the `myObject` variable.
- Used `console.log(...)` to print the updated `myObject`.

### 13. Add file
- Implemented a function that returns the addition of two integers.
- The function is visible from outside.
- Used `require` to import the function and demonstrated its usage in the `13-main.js` file.

## How to Run the Scripts
To execute any script, use the following format:
```bash
$ ./script_name.js
