import argparse
import os
import pathlib
import glob
import nltk

from main import redactFiles


def redactor(args):
    print("args:", args)
    filesList = []
    if args.input is None:
        print("No input is passed")
    else:
        for extension in args.input:
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

        for fileName in filesList:
            redactContents = {}
            print("*************************************************************************************************")
            print("file Name:", fileName)
            if fileName == "requirements.txt" or fileName == "project1/stderr/stat.txt":
                continue
            if args.names:
                redactContents = redactObj.redactNames(args.stats, fileName, redactContents)
            if args.dates:
                redactContents = redactObj.redactDates(args.stats, fileName, redactContents)
            if args.phones:
                redactContents = redactObj.redactPhones(args.stats, fileName, redactContents)
            if args.address:
                redactContents = redactObj.redactAddress(args.stats, fileName, redactContents)
            if args.concept:
                redactContents = redactObj.redactConcept(args.stats, fileName, redactContents, args.concept)
            if args.genders:
                redactContents = redactObj.redactGenders(args.stats, fileName, redactContents)
            print("values before redaction starts:", redactContents)
            content = redactObj.redactContent(args, fileName, redactContents)
            print(f"Final redacted content for {fileName}: {content}")
            if args.output:
                if not pathlib.Path(args.output + fileName + '.redacted').is_file():
                    try:
                        os.mkdir(args.output)
                        writeToRedactedFile = open(args.output + fileName + '.redacted', mode="w")
                        writeToRedactedFile.write(content)
                    except OSError as dirErr:
                        print("File already exists. So, writing redacted content to it.")
                        writeToRedactedFile = open(args.output + fileName + '.redacted', mode="w")
                        writeToRedactedFile.write(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Enter type of files to be read", nargs="+", required=True)
    parser.add_argument("--names", help="if you want names to be redacted", action="store_true")
    parser.add_argument("--dates",  help="if you want dates to be redacted", action="store_true")
    parser.add_argument("--phones",  help="if you want phones to be redacted", action="store_true")
    parser.add_argument("--genders",  help="if you want genders to be redacted", action="store_true")
    parser.add_argument("--address",  help="if you want address to be redacted", action="store_true")
    parser.add_argument("--concept",  help="if you want any concept to be redacted", type=str)
    parser.add_argument("--output", help="Specify the folder name to store redacted files")
    parser.add_argument("--stats", help="Stats")
    args = parser.parse_args()
    redactor(args)

