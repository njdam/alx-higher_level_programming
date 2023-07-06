# Python - Test-driven development

***Test-driven development*** (TDD) is a software development approach in which tests are written before the actual code implementation. It follows a cycle of writing a failing test, writing the minimum code necessary to pass the test, and then refactoring the code while ensuring that the tests continue to pass. TDD aims to improve code quality, maintainability, and reliability.

In Python, there are several testing frameworks available for implementing TDD, with the most popular one being `unittest`. Here's an example of how you can practice TDD using `unittest`:

1. Import the necessary modules:
`import unittest`

2. Create a test class by subclassing `unittest.TestCase`:
```
class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Test case code goes here
        pass
```

3. Write a test method within the test class. Test methods should start with the word "test" and should contain assertions to validate the expected behavior of the code being tested:
```
def test_something(self):
    result = some_function()  # Call the function being tested
    self.assertEqual(result, expected_result)  # Assertion
```

4. Implement the minimum code necessary to pass the test. Repeat steps 3 and 4 until all the desired functionality is implemented.

5. Run the tests using the `unittest` test runner. This can be done by executing the following code at the bottom of your script:
```
if __name__ == '__main__':
    unittest.main()
```

6. As you add more features or make changes to your code, re-run the tests to ensure that everything still works as expected.

Following this TDD process helps you catch bugs early, ensures that your code is testable, and provides documentation of the expected behavior of your code.

Apart from `unittest`, there are other testing frameworks in Python like `pytest` and `doctest`, which also support test-driven development. Each framework has its own syntax and features, so you can choose the one that best fits your needs and preferences.

***What is Doctest?***
`Doctest` is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown.

***What is Unittest?***
`Unittest` test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.

Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown.

## ADVANCED TASK

#### Multiplication of 2 Matrices

Let's walk through the steps of mathematical matrix multiplication using an example. Consider the following two matrices:

`Matrix A:`
```
[
  [2, 3],
  [4, 5]
]
```

`Matrix B:`
```
[
  [1, 2],
  [3, 4]
]
```

To multiply these matrices, we follow these steps:

<span style="color: blue; font-family: Times New Roman">Step 1: Determine the dimensions</span>

Matrix A has dimensions 2x2 (2 rows and 2 columns).
Matrix B has dimensions 2x2 (2 rows and 2 columns).


<span style="color: blue; font-family: Times New Roman">Step 2: Check compatibility</span>

The number of columns in Matrix A (2) must be equal to the number of rows in Matrix B (2) for multiplication to be possible. In this case, they are equal, so the matrices are compatible for multiplication.

<span style="color: blue; font-family: Times New Roman">Step 3: Multiply the elements and sum the products</span>

To calculate each element of the resulting matrix, we multiply corresponding elements from each row of Matrix A with each column of Matrix B and sum the products.

<span style="color: green;">For the element in the first row and first column of the resulting matrix:</span>

Multiply the first row of Matrix A: [2, 3]
Multiply the first column of Matrix B: [1, 3]
Multiply corresponding elements and sum the products: (21) + (33) = 11


<span style="color: green;">For the element in the first row and second column of the resulting matrix:</span>

Multiply the first row of Matrix A: [2, 3]
Multiply the second column of Matrix B: [2, 4]
Multiply corresponding elements and sum the products: (22) + (34) = 16


<span style="color: green;">For the element in the second row and first column of the resulting matrix:</span>

Multiply the second row of Matrix A: [4, 5]
Multiply the first column of Matrix B: [1, 3]
Multiply corresponding elements and sum the products: (41) + (53) = 19


<span style="color: green;">For the element in the second row and second column of the resulting matrix:</span>

Multiply the second row of Matrix A: [4, 5]
Multiply the second column of Matrix B: [2, 4]
Multiply corresponding elements and sum the products: (42) + (54) = 28


<span style="color: green;">Putting it all together, the resulting matrix will be:</span>
Resulting Matrix:
```
[
  [11, 16],
  [19, 28]
]
```

[Reference](https://chat.openai.com/)
