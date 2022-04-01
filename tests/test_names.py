from main import redactFiles
import glob


def test_names():
    filesList = glob.glob("*.txt")
    testObj = redactFiles()
    for files in filesList:
        if files != "requirements.txt":
            redactContents = {}
            redactContents = testObj.redactNames(files, redactContents)
            names = redactContents['names']
            assert type(names) == list
            assert type(redactContents) == dict
            assert len(redactContents) != 0
            assert len(redactContents) > 0
            assert redactContents is not None
            assert names is not None



