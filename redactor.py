import argparse
import os
import pathlib
import glob
import nltk
import sys
from main import redactFiles


def redactor(args):
    print("args:", args)
    filesList = []
    flattenFilesList = nltk.flatten(args.input)
    if args.input is None:
        print("No input file extensions are passed.")
    else:
        for extension in flattenFilesList:
            filesList.append(glob.glob(extension))
        filesList = nltk.flatten(filesList)
        redactObj = redactFiles()
        if not (args.stats == "stdout" or args.stats == "stderr"):
            if not pathlib.Path(args.stats + 'stat.txt').is_file():
                try:
                    os.mkdir(args.stats)
                    open(args.stats + 'stat.txt', mode="w")
                except OSError as dirErr:
                    open(args.stats + 'stat.txt', mode="w")
            else:
                open(args.stats + 'stat.txt', mode="w")
        for fileName in filesList:
            redactContents = {}
            print(f"\n*************************************\t{fileName}\t************************************************************")
            if fileName == "requirements.txt":
                continue
            if 'stats.txt' in fileName:
                continue
            if 'stat.txt' in fileName:
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
                    resultList.append(redactObj.redactConcept(fileName, concept))
                resultList = nltk.flatten(resultList)
                redactContents['concept'] = resultList
            if args.genders:
                redactContents = redactObj.redactGenders(fileName, redactContents)
            content = redactObj.redactContent(args, fileName, redactContents)
            if args.output == 'stdout':
                print(f"\nAfter redaction, the content in the {fileName}:")
                sys.stdout.write(content)
            elif args.output == 'stderr':
                print(f"\nAfter redaction, the content in the {fileName}:")
                sys.stderr.write(content)
            else:
                tempFileName = ''
                for i in range(len(fileName) - 1, -1, -1):
                    if fileName[i] == '/' or fileName[i] == '\\':
                        break
                    tempFileName = tempFileName + fileName[i]
                fileName = ''
                for i in range(len(tempFileName) - 1, -1, -1):
                    fileName = fileName + tempFileName[i]
                if not pathlib.Path(args.output + fileName + '.redacted').is_file():
                    try:
                        os.mkdir(args.output)
                        writeToRedactedFile = open(args.output + fileName + '.redacted', mode="w", encoding='utf-8')
                        writeToRedactedFile.write(content)
                    except OSError as dirErr:
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

