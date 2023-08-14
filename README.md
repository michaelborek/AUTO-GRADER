# AUTO-GRADER
### Table of Contents
[Introduction](#table-of-contents)
[Features](#table-of-contents)
[Installation](#table-of-contents)
[Usage](#table-of-contents)
[Example Code Assignments](#table-of-contents)
[Contributing](#table-of-contents)
[License](#table-of-contents)
[Contact](#table-of-contents)
### Introduction
AUTO-GRADER is a software tool designed to assist educators in automating the grading process for students' code assignments. It aims to provide consistent, unbiased, and prompt feedback on students' assignments, reducing the workload of manual grading.

### Features
Automated Grading: Evaluate students' code assignments based on predefined criteria and test cases.
Multiple Projects: Supports a variety of course projects including NumGame, RPSLS, GuessingGame, and more.
Feedback Generation: Provides detailed feedback on the assignments, pointing out errors and suggestions.
Extensible: Easy to add new assignments and their corresponding test cases.
Installation
To install AUTO-GRADER:

### Clone the repository from GitHub:
<pre>
```bash
git clone https://github.com/michaelborek/AUTO-GRADER.git
```
</pre>

Navigate to the project directory and install the required dependencies:
<pre>
```bash
cd AUTO-GRADER
pip install -r requirements.txt
```
</pre>

### Usage
To grade a student's assignment:

<pre>
```bash
python autograder.py -f <path_to_student_code>
```
</pre>

For more detailed usage and options, refer to the built-in help:

<pre>
```bash
python autograder.py --help
```
</pre>

### Example Code Assignments
The following are example code assignments included in the repository:

NumGame (project1.py): A game where the player guesses numbers.
- RPSLS (project2.py): Rock-Paper-Scissors-Lizard-Spock game implementation.
- GuessingGame (project3.py): A classic guessing game with a twist.
- Combined Game (project4.py): A combination of the aforementioned games for advanced challenges.
- Contributing
- Contributions, issues, and feature requests are welcome! Feel free to check [issue pages](https://github.com/michaelborek/AUTO-GRADER/issues) for open issues or to create a new one.

### License
Distributed under the MIT License. See LICENSE for more information.

### Contact
Michael Borek

GitHub: michaelborek
Email: borekmi1@msu.edu
