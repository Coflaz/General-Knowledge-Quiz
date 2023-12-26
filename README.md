# General Knowledge Quiz

## Introduction
Welcome to the **General Knowledge Quiz**! This Python program is designed to provide an engaging quiz experience, testing participants' knowledge on a variety of true or false questions. The program utilizes a command-line interface and is implemented using Python.

## Table of Contents
1. [How to Run](#how-to-run)
2. [Program Overview](#program-overview)
   - [Main Features](#main-features)
3. [Code Structure](#code-structure)
   - [main.py](#mainpy)
   - [data.py](#datapy)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Instructions](#instructions)
5. [Gameplay](#gameplay)
   - [Rules](#rules)
   - [Scoring](#scoring)
   - [Ending the Quiz](#ending-the-quiz)
6. [Extending the Quiz](#extending-the-quiz)
7. [Contributing](#contributing)
8. [Acknowledgments](#acknowledgments)

## How to Run <a name="how-to-run"></a>
Ensure that you have Python installed on your system. To run the quiz, execute the following command in your terminal:

```bash
python main.py
```

Program Overview <a name="program-overview"></a>
------------------------------------------------

### Main Features <a name="main-features"></a>

*   Engaging General Knowledge Quiz
*   True or False Questions
*   Ability to Skip Questions
*   Multiplayer Mode (Up to 10 Players)
*   Real-time Score Display
*   Dynamic Question Pool
*   Clearing Console for a Clean Interface

Code Structure <a name="code-structure"></a>
--------------------------------------------

### main.py <a name="mainpy"></a>

This file contains the main logic of the General Knowledge Quiz. It includes classes for `Question` and `Player`, as well as the `Quiz` class responsible for managing the quiz flow.

### data.py <a name="datapy"></a>

The `data.py` file stores the question data used in the quiz. It includes a list of dictionaries, each containing a question's text and its corresponding answer.

Getting Started <a name="getting-started"></a>
----------------------------------------------

### Prerequisites <a name="prerequisites"></a>

*   Python 3.x
*   PrettyTable library (`pip install PrettyTable`)

### Instructions <a name="instructions"></a>

1.  Clone this repository to your local machine.
2.  Navigate to the project directory in your terminal.
3.  Run the quiz using the command mentioned in the [How to Run](#how-to-run) section.

Gameplay <a name="gameplay"></a>
--------------------------------

### Rules <a name="rules"></a>

*   Players are presented with a series of true or false questions.
*   Input 'True' or 'False' for each question.
*   Type 'pass' to skip a question without gaining or losing points.

### Scoring <a name="scoring"></a>

*   Correct answers increase the player's score by 1.
*   Incorrect answers decrease the player's score by 1.
*   Skipping a question gives 0 points.

### Ending the Quiz <a name="ending-the-quiz"></a>

*   Players can choose to end the quiz at any time.
*   The quiz also ends when a player reaches a score of 15 or when all players pass all questions.

Extending the Quiz <a name="extending-the-quiz"></a>
----------------------------------------------------

Feel free to extend the quiz by adding more questions to the `data.py` file or implementing additional features. You can contribute to the project by enhancing the quiz experience or creating different quiz themes.

Contributing <a name="contributing"></a>
----------------------------------------

If you'd like to contribute to this project, please follow the [contributing guidelines](CONTRIBUTING.md).

Acknowledgments <a name="acknowledgments"></a>
----------------------------------------------

This General Knowledge Quiz program was created with passion and dedication. Special thanks to the open-source community and contributors for their support and collaboration. Enjoy the quiz and happy learning!
