# STK-INF4000 Homework Boilerplate Code and Tests

Code to get students started with STK-INF4000 homework. The repository
contains

- Boilerplate code
- Tests

The idea is that you complete the code to make the tests pass, and
thus completing your homework assignment (or parts of it).

## Week 14 Assignments

We use `NLTK` and plain python. Hence you can
run [this week's tests](week14) using plain python:

	python tests.py

## Week 7 Assignments

For week 7 we use [Apache Spark](https://spark.apache.org) for the
first time. This means in particular that the tests need to be
executed using Spark. To do so, you issue the following commands from
the [week07](week07) directory.

    /path/to/spark-2.1.0-bin-hadoop2.7/bin/spark-submit tests.py

## Week 6 Assignments

The templates are located in the folder [week06](week06) and the
instructions to execute the tests are identical to last week's.

## Week 5 Assignments

There were no programming assignments for week 5.

## Week 4 Assignments

The assignments and tests for week 4 are located in the same
[folder](week04) and the tests can be run by calling from the
[week04 directory](week04)

    python tests.py

## Week 3 Assignments

You'll find the boilerplate code in the file
[homework.py](week03/homework.py), together with some descriptions.

### Tests

The tests can be found in the file
[week03/tests/test_hw.py](week03/tests/test_hw.py) and can be run from
the directory [week03](week03) using the command

    python -m unittest tests.test_hw

