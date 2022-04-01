import argparse
from main import redactFiles
import glob


def test_redactContent():
    filesList = glob.glob("*.txt")
    testObj = redactFiles()
    redactContents = {'names': [], 'dates': [], 'phones': [], 'genders': [], 'concept': [], 'address': []}
    parser = argparse.ArgumentParser()
    parser.add_argument("--names", help="if you want names to be redacted", action="store_true")
    parser.add_argument("--dates", help="if you want dates to be redacted", action="store_true")
    parser.add_argument("--phones", help="if you want phones to be redacted", action="store_true")
    parser.add_argument("--genders", help="if you want genders to be redacted", action="store_true")
    parser.add_argument("--address", help="if you want address to be redacted", action="store_true")
    parser.add_argument("--concept", help="if you want any concept to be redacted", action="append", nargs="+")
    parser.add_argument("--stats", help="Stats")
    args = parser.parse_args(['--names', '--dates', '--phones', '--genders', '--address', '--concept', 'kids', 'prison', '--stats', 'stderr'])
    for fileName in filesList:
        content = testObj.redactContent(args, fileName, redactContents)
        assert type(content) == str
        assert len(content) != 0
        assert len(redactContents) > 0
        assert content is not None


