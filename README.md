# test
python.dialoget.com is a test framework for multilanguage source code, based on decorators

## init
```bash
pip install --upgrade pip
pip install requests
pip install behave
chmod +x test.sh
```

## Start testing
with one bash script
```bash
./test.sh
```

or each script in command line

```bash
cd test
python3 update_repo_on_github.py
python3 update_repo_on_github2.py
python3 create_repo_on_org_github.py
```



The test directory structure for Python and Java projects will often follow conventions that are supported by popular testing frameworks and project management tools.
Below, are typical structures for both languages, which help in organizing tests based on their type (e.g., unit tests, functional tests, integration tests).


### Python

In Python projects, tests are often placed in a separate directory, commonly named `tests`. Each category of test may be placed in its own subdirectory. Here is an example structure that might be used in a Python project:

```
my_python_project/
│
├── my_project/
│   ├── module1.py
│   └── module2.py
│
├── tests/
│   ├── unit/
│   │   ├── test_module1.py
│   │   └── test_module2.py
│   │
│   ├── functional/
│   │   └── test_something_functional.py
│   │
│   └── integration/
│       └── test_integration.py
│
└── setup.py (or pyproject.toml, or requirements.txt, depending on the project)
```

This structure separates the test types into different subdirectories, making it easier to manage them and execute them separately. Note that each test directory typically contains an `__init__.py` file, which is necessary for the Python test discovery mechanisms in most testing frameworks, such as `unittest` or `pytest`.

### Java

Java projects often use Maven or Gradle as build tools, and the default conventions for these tools define specific directories for different types of tests. Here's how a Maven project might structure its tests:

```
my_java_project/
│
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/
│   │           └── mycompany/
│   │               └── myproject/
│   │                   ├── Module1.java
│   │                   └── Module2.java
│   │
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── mycompany/
│       │           └── myproject/
│       │               ├── unit/
│       │               │   ├── Module1Test.java
│       │               │   └── Module2Test.java
│       │               │
│       │               ├── functional/
│       │               │   └── SomethingFunctionalTest.java
│       │               │
│       │               └── integration/
│       │                   └── IntegrationTest.java
│       │
│       └── resources/
│
└── pom.xml
```

In this structure, all Java source files are located in `src/main/java`, and test files are located in `src/test/java`. Tests are further organized into subdirectories (unit, functional, and integration), corresponding to each type of test within the `test` directory.

It's important to note that while you can organize the tests into subdirectories in Java, the use of package naming conventions is more common. Test frameworks like JUnit do not enforce a particular directory structure, but they do differentiate tests based on annotations or naming conventions within the code.

The Maven directory structure (`src/main/java` for source code and `src/test/java` for test code) is a convention that tools recognize, and they are configured to compile and execute tests based on this layout.

As best practice, both Python and Java projects should have good separation of test types. This makes it clear what each test is designed to achieve and allows for the selective execution of test suites based on the scope of changes or the stage of the development pipeline.