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
