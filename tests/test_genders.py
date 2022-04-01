from main import redactFiles
import glob


def test_genders():
    filesList = glob.glob("*.txt")
    testObj = redactFiles()
    for files in filesList:
        if files != "requirements.txt":
            redactContents = {}
            redactContents = testObj.redactGenders(files, redactContents)
            genders = redactContents['genders']
            assert type(genders) == list
            assert type(redactContents) == dict
            assert len(redactContents) != 0
            assert len(redactContents) > 0
            assert redactContents is not None
            assert genders is not None

