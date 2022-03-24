import argparse
import os
import pathlib
import glob
import nltk

from redactor import redactFiles


def main(args):
    print("args:", args)
    for input in args.input:
        print("input:", input)
        filesNameList = input.split(",")
    print("Files in List before glob library:", filesNameList)
    newFilesNameList = []
    # for fileName in filesNameList:
    #     print("File Name extension:", fileName)
    #     print("file String Name:", glob.glob(fileName))
    #     newFilesNameList.append(glob.glob(fileName))
    # newFilesNameList = nltk.flatten(newFilesNameList)
    print("Files List after glob library:", newFilesNameList)
    redactObj = redactFiles()
    content = ''
    # if args.stats:
    #     if not pathlib.Path(args.stats+'/stat.txt').is_file():
    #         try:
    #             os.mkdir('project1/' + args.stats)
    #             open('project1/' + args.stats + '/stat.txt', mode="w")
    #         except OSError as dirErr:
    #             open('project1/' + args.stats + '/stat.txt', mode="w")
    #             print("Directory already exists. So, no need to create one.")
    #
    # for fileName in newFilesNameList:
    #     print("file Name:", fileName)
    #     if fileName == "requirements.txt" or fileName == "stat.txt":
    #         continue
    #     if args.names:
    #         content = redactObj.redactNames(fileName, args.stats)
    #     if args.dates:
    #         content = redactObj.redactDates(args.stats, content)
    #     if args.phones:
    #         content = redactObj.redactPhones(args.stats, content)
    #     if args.genders:
    #         content = redactObj.redactGenders(args.stats, content)


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

    print(args)
    main(args)

