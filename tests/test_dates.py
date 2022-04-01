from main import redactFiles
import glob


def test_dates():
    filesList = glob.glob("*.txt")
    testObj = redactFiles()
    for files in filesList:
        if files != "requirements.txt":
            redactContents = {}
            redactContents = testObj.redactDates(files, redactContents)
            dates = redactContents['dates']
            assert type(dates) == list
            assert type(redactContents) == dict
            assert len(redactContents) != 0
            assert len(redactContents) > 0
            assert redactContents is not None
            assert dates is not None

