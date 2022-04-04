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
* This method takes args as input which was passed from the command line and goes through every flag if true and calls appropriate method in main.py to detect and collect sensitive information.
* For input flag, it first collects all the extensions which was passed by user and uses nltk.flatten() method to flatten the list. If no input flag is passed then error message is displayed.
* First, I am looping through the provided extensions and used glob library to collect all relevant files and stored them in a list to iterate them in the future.
* Using for loop, I am iterating every file in the list and based on the flags passed from command line, related methods will be called to detect and collect sensitive information.
  _Example:_ _if args.names is true then redactObj.redactNames(fileName, redactContents) method will be called._
* I am initializing a dictionary called redactContents and passing it to every method to collect the sensitive information as list and storing it in the dictionary.
  _Example: redactContents['names'] = namesHoldingList_
* Multiple flags can be given for concept. So, I am using a for loop to iterate through the list and collecting the sentences in a list. Finally, storing it in the redactContents dictionary. I am using nltk.flatten() method to flatten the list before storing it in the dictionary.
* After detecting and collecting the sensitive information in the dictionary, along with args and fileName passing it to the redactContent method in main.py as parameters for redaction.
* #####Three output cases:
    case 1:
   * The redacted content is stored in content variable. The glob library picks up the filename along with directory name. So, to get the appropriate file name I am using a for loop to read the string from backwards and breaking loop when it encounters characters like '/' or '\\'.
     _Example path picked by glob library: inputFiles/sample4.txt_
   * Before writing the redacted content to the file, I am first checking if the file path exists or not. If not then I am creating the directory with os.mkdir(args.output) and creating a file with open(args.output + fileName + '.redacted', mode="w", encoding='utf-8') method with the mentioned parameters.
   * If file already exits in the specified path then I am opening the file and writing the redacted content to it.
   
  case 2:
   * When stdout is passed, I am using sys library to write the output to console/command line.
      _Example: sys.stdout.write(content)_
  
  case 3:
   * When stderr is passed, I am using sys library to write the output to console/command line.
      _Example: sys.stderr.write(content)_

