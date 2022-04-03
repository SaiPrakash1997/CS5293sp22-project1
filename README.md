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
2) nlp
3) spacy
4) nltk
5) pytest

#### INSTALLATION OF ABOVE LIBRARIES:
1) en_core_web_lg is a large english pipeline trained on written web text. This is automatically installed through Pipfile or you can use this command to install it: pipenv run python -m spacy download en_core_web_lg
2) pipenv install nlp
3) pipenv install spacy
4) pipenv install nltk
5) pipenv install pytest