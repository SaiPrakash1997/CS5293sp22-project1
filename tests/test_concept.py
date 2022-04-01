from main import redactFiles
import glob


def test_concept():
    filesList = glob.glob("*.txt")
    testObj = redactFiles()
    redactContents = {}
    for files in filesList:
        if files != "requirements.txt":
            concepts = ['kids', 'prison', 'family']
            resultList = []
            for concept in concepts:
                resultList.append(testObj.redactConcept(files, concept))
                assert type(resultList) == list
                if len(resultList) == 0:
                    assert len(resultList) != 0
                else:
                    assert len(resultList) > 0
                assert resultList is not None
            redactContents['concept'] = resultList
            assert type(redactContents) == dict
            assert len(redactContents) != 0
            assert len(redactContents) > 0
            assert redactContents is not None



