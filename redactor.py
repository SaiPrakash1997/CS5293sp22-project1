import argparse
import os
import pathlib
import glob
import nltk

from main import redactFiles


def redactor(args):
    print("args:", args)
    filesList = []
    flattenFilesList = nltk.flatten(args.input)
    if args.input is None:
        print("No input is passed")
    else:
        for extension in flattenFilesList:
            print("File Name extension:", extension)
            print("file String Name:", glob.glob(extension))
            filesList.append(glob.glob(extension))
        filesList = nltk.flatten(filesList)
        print("Files List after glob library:", filesList)
        redactObj = redactFiles()
        if args.stats:
            if not pathlib.Path(args.stats+'/stat.txt').is_file():
                try:
                    os.mkdir(args.stats)
                    open(args.stats + '/stat.txt', mode="w")
                except OSError as dirErr:
                    open(args.stats + '/stat.txt', mode="w")
                    print("Directory already exists. So, no need to create one.")
            else:
                open(args.stats + '/stat.txt', mode="w")

        for fileName in filesList:
            redactContents = {}
            print("*************************************************************************************************")
            print("file Name:", fileName)
            if fileName == "requirements.txt" or fileName == "stderr/stat.txt" or fileName == "stderr\\stat.txt":
                continue
            if args.names:
                redactContents = redactObj.redactNames(fileName, redactContents)
            if args.dates:
                redactContents = redactObj.redactDates(fileName, redactContents)
            if args.phones:
                redactContents = redactObj.redactPhones(fileName, redactContents)
            if args.address:
                redactContents = redactObj.redactAddress(fileName, redactContents)
            if args.concept:
                concepts = nltk.flatten(args.concept)
                resultList = []
                for concept in concepts:
                    print("concept:", concept)
                    resultList.append(redactObj.redactConcept(fileName, concept))
                resultList = nltk.flatten(resultList)
                print(f"Result from redactConcept method: {resultList}")
                redactContents['concept'] = resultList
            if args.genders:
                redactContents = redactObj.redactGenders(fileName, redactContents)
            print("*****************************************************************************************************")
            print("values before redaction starts:", redactContents)
            content = redactObj.redactContent(args, fileName, redactContents)
            print(f"Final redacted content for {fileName}: {content}")
            if args.output:
                tempFileName = ''
                for i in range(len(fileName)-1, -1, -1):
                    if fileName[i] == '/' or fileName[i] == '\\':
                        break
                    tempFileName = tempFileName + fileName[i]
                fileName = ''
                for i in range(len(tempFileName)-1, -1, -1):
                    fileName = fileName+tempFileName[i]
                print("File Name:", fileName)
                if not pathlib.Path(args.output + fileName + '.redacted').is_file():
                    try:
                        os.mkdir(args.output)
                        writeToRedactedFile = open(args.output + fileName + '.redacted', mode="w", encoding='utf-8')
                        writeToRedactedFile.write(content)
                    except OSError as dirErr:
                        print(f"File already exists. So, writing redacted content to it. Error:{dirErr}")
                        writeToRedactedFile = open(args.output + fileName + '.redacted', mode="w", encoding='utf-8')
                        writeToRedactedFile.write(content)
                else:
                    writeToRedactedFile = open(args.output + fileName + '.redacted', mode="w", encoding='utf-8')
                    writeToRedactedFile.write(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Enter type of files to be read", action="append", nargs="+", required=True)
    parser.add_argument("--names", help="if you want names to be redacted", action="store_true")
    parser.add_argument("--dates",  help="if you want dates to be redacted", action="store_true")
    parser.add_argument("--phones",  help="if you want phones to be redacted", action="store_true")
    parser.add_argument("--genders",  help="if you want genders to be redacted", action="store_true")
    parser.add_argument("--address",  help="if you want address to be redacted", action="store_true")
    parser.add_argument("--concept",  help="if you want any concept to be redacted", action="append", nargs="+")
    parser.add_argument("--output", help="Specify the folder name to store redacted files")
    parser.add_argument("--stats", help="Stats")
    args = parser.parse_args()
    redactor(args)

