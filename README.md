# cs5293sp22-project1
Name: Sai Prakash Davuluri

Goal: The aim of the project is to use the knowledge of Python and Text Analytics to develop a system that accepts plain text documents then detect and redact 
"sensitive items".

## How to run the application
### steps:
1) First clone the project using : git clone <project-url>
2) check to see if there is a directory named as 'cs5293sp22-project1' using ls
3) open the directory using cd cs5293sp22-project1
4) Run the below command to start the project:

pipenv run python redactor.py --input '*.txt' --input '*/*.txt' --names --dates --phones --genders --address --concept 'kids' --concept 'prison' --output 'files/' --stats stderr

#### WEB OR EXTERNAL LIBRARIES:
1) en_core_web_lg
2) argparse
3) nlp
4) spacy
5) nltk
6) pytest
7) pyap

#### INSTALLATION OF ABOVE LIBRARIES:
1) en_core_web_lg is a large english pipeline trained on written web text. This is automatically installed through Pipfile or you can use this command to install it: pipenv run python -m spacy download en_core_web_lg
2) pipenv install argparse
3) pipenv install nlp
4) pipenv install spacy
5) pipenv install nltk
6) pipenv install pytest
7) pipenv install pyap

### Assumptions made in the project


### Functions and approach
redactor(args) function in redactor.py:
* This method takes args as input which was passed from the command line and goes through every flag if true and calls appropriate method in main.py to collect sensitive information.
* For input flag, it first collects all the extensions which was passed by user and uses nltk.flatten() method to flatten the list. If no input flag is passed then error message is displayed.
* First, I am looping through the provided extensions and using glob library to collect the files and storing the filename in a list to iterate them in the future.
* 
