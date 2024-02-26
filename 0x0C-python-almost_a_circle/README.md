# Almost A Circle Project

Welcome to the "Almost A Circle" project. This project is part of the ALX Higher Level Programming curriculum, focusing on expanding Python programming skills, particularly in dealing with classes, inheritance, file I/O, and unit testing. The project structure is designed to simulate a real-life project scenario where different modules interact to achieve a common goal.

## Project Structure

The project is structured as follows:

- `models/`: This directory contains the Python modules that define the classes and methods for the project. Key components include:
  - `base.py`: Contains the `Base` class, serving as the base class for other classes in the project.
  - `rectangle.py`: Defines the `Rectangle` class, inheriting from `Base`.
  - `square.py`: Defines the `Square` class, inheriting from `Rectangle`.
  - `__init__.py`: An initialization file to make Python treat the `models` directory as a package.
- `tests/`: Contains unit tests for the project. It is crucial to run these tests to ensure the reliability and correctness of the code.
- `README.md`: Provides an overview and guidelines for the project.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/bwambale03/alx-higher_level_programming.git
    ```

2. Navigate to the `0x0C-python-almost_a_circle` directory:

    ```sh
    cd alx-higher_level_programming/0x0C-python-almost_a_circle
    ```

3. You can run the Python scripts within the `models` directory to interact with the classes and methods defined.

## Running Tests

To ensure the integrity and correctness of the project, run the unit tests located in the `tests` directory. Use the following command:

```sh
python3 -m unittest discover tests
