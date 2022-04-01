from main import redactFiles
import glob


def test_address():
    filesList = glob.glob("*.txt")
    testObj = redactFiles()
    for files in filesList:
        if files != "requirements.txt":
            redactContents = {}
            redactContents = testObj.redactAddress(files, redactContents)
            address = redactContents['address']
            assert type(address) == list
            assert type(redactContents) == dict
            assert len(redactContents) != 0
            assert len(redactContents) > 0
            assert redactContents is not None
            assert address is not None

