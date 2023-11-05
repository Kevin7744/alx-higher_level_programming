0x07. Python - Test-driven development
#Author: Kevin Kipkoech


 

### doctest- Testing through documentation
The purpose of doctest is to write automated tests as part of the documentation for a module.
Doctest test source code by running examples embedded in the documentation and verifying they produce the expected results. It works by parsing the help text to find examples, running them then comparing the output against the expected value. Many developers find doctest easier to use than unit test because, in its simplest form, there is no APi  to learn before using it.
#### unittest
Unittest test case runners allow more options when running tests, like reporting test statictcs as tests that passed and failed.
Unittests used methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. It has several inbuilt features that are unavailable in doctest, including genarators and group fixture managers like setup and teardown.

##### For ALX tasks
The learning objectives of this project was;
General
•	Why Python programming is awesome
•	What’s an interactive test
•	Why tests are important
•	How to write Docstrings to create tests
•	How to write documentation for each module and function
•	What are the basic option flags to create tests
•	How to find edge cases


	
## Tests :heavy_check_mark:

* [tests](./tests): Test files.
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |
