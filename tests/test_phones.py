from main import redactFiles
import glob


def test_phones():
    filesList = glob.glob("*.txt")
    testObj = redactFiles()
    for files in filesList:
        if files != "requirements.txt":
            redactContents = {}
            redactContents = testObj.redactPhones(files, redactContents)
            phones = redactContents['phones']
            assert type(phones) == list
            assert type(redactContents) == dict
            assert len(redactContents) != 0
            assert len(redactContents) > 0
            assert redactContents is not None
            assert phones is not None

