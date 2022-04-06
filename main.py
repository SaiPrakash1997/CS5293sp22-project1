import nltk
import spacy
from nltk.tree import Tree
from nltk.corpus import wordnet
import re
import pyap
import sys
import en_core_web_lg
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
nltk.download('omw-1.4')


class redactFiles:
    def __init__(self):
        pass

    def redactNames(self, fileName, redactContents):
        try:
            content = open(fileName, 'r').read()
        except (FileNotFoundError, IOError, Exception) as error:
            print(f"Following error was raised when reading a file {error.args}")

        content = content.strip()
        sentenceList = nltk.sent_tokenize(content)
        nlp = en_core_web_lg.load()
        namesHoldingList = []
        for sentence in sentenceList:
            doc = nlp(sentence)
            for token in doc.ents:
                if token.label_ == 'PERSON':
                    namesHoldingList.append(token.text)
        wordsList = nltk.tokenize.word_tokenize(content)
        tagList = nltk.pos_tag(wordsList)
        chunkedList = nltk.ne_chunk(tagList)
        for entities in chunkedList:
            if type(entities) == Tree and entities.label() == 'PERSON':
                namesHoldingList.append(' '.join([chunk[0] for chunk in entities]))
        redactContents['names'] = namesHoldingList
        return redactContents

    def redactDates(self, fileName, redactContents):
        try:
            content = open(fileName, 'r').read()
        except (FileNotFoundError, IOError, Exception) as error:
            print(f"Following error was raised when reading a file {error.args}")
        tempHolder = []
        scenario1 = []
        datesContainerLetters = []
        datesContainerNumbers = []
        redundentValues = ['Monday,', 'monday,', 'mon,', 'Mon,', 'Tuesday,', 'tuesday,', 'Wednesday,', 'wednesday,', 'Wed,', 'wed,', 'Thursday,'
                           'thursday,', 'thurs,', 'Thurs,', 'Friday,', 'friday,', 'Fri,', 'fri,', 'Saturday,', 'saturday,', 'Sat,', 'sat,'
                           'Sunday,', 'sunday,', 'Sun,', 'sun,']
        # Wed, 9 Jan 2002
        scenario1.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)(,)\s([\d]{1,2})\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{4})",
            content))
        scenario1.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)(,)\s([\d]{1,2})\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{4})",
            content))
        scenario1.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)(,)\s([\d]{1,2})\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{4})",
            content))
        scenario1.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)(,)\s([\d]{1,2})\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{4})",
            content))
        # Friday, November 02, 2001
        scenario1.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)(,)\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{1,2})(,)\s([\d]{4})",
            content))
        scenario1.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)(,)\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{1,2})(,)\s([\d]{4})",
            content))
        scenario1.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)(,)\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{1,2})(,)\s([\d]{4})",
            content))
        scenario1.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)(,)\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{1,2})(,)\s([\d]{4})",
            content))
        # Friday 11/9/01
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{1,2}/[\d]{1,2}/[\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{4}/[\d]{1,2}/[\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{1,2}-[\d]{1,2}-[\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{4}-[\d]{1,2}-[\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{1,2}/[\d]{1,2}/[\d]{2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{2}/[\d]{1,2}/[\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{1,2}-[\d]{1,2}-[\d]{2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]onday?|[tT]uesday?|[wW]ednesday?|[tT]hrusday?|[fF]riday?|[sS]aturday?|[sS]unday?)\s([\d]{2}-[\d]{1,2}-[\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{1,2}/[\d]{1,2}/[\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{4}/[\d]{1,2}/[\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{1,2}-[\d]{1,2}-[\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{4}-[\d]{1,2}-[\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{1,2}/[\d]{1,2}/[\d]{2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{2}/[\d]{1,2}/[\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{1,2}-[\d]{1,2}-[\d]{2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([mM]on?|[tT]ues?|[wW]ed?|[tT]hrus?|[fF]ri?|[sS]at?|[sS]un?)\s([\d]{2}-[\d]{1,2}-[\d]{1,2})",
            content))
        # 11/2/01
        datesContainerNumbers.append(re.findall(
            r"[\d]{1,2}/[\d]{1,2}/[\d]{4}",
            content))
        datesContainerNumbers.append(re.findall(
            r"[\d]{4}/[\d]{1,2}/[\d]{1,2}",
            content))
        datesContainerNumbers.append(re.findall(
            r"[\d]{1,2}-[\d]{1,2}-[\d]{4}",
            content))
        datesContainerNumbers.append(re.findall(
            r"[\d]{4}-[\d]{1,2}-[\d]{1,2}",
            content))
        datesContainerNumbers.append(re.findall(
            r"[\d]{1,2}/[\d]{1,2}/[\d]{2}",
            content))
        datesContainerNumbers.append(re.findall(
            r"[\d]{2}/[\d]{1,2}/[\d]{1,2}",
            content))
        datesContainerNumbers.append(re.findall(
            r"[\d]{1,2}-[\d]{1,2}-[\d]{2}",
            content))
        datesContainerNumbers.append(re.findall(
            r"[\d]{2}-[\d]{1,2}-[\d]{1,2}",
            content))
        # January 1, 2002
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2})\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2})\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{1,2},)\s([\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{1,2},)\s([\d]{4})",
            content))
        # December 29
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2})\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{1,2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2})\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)",
            content))
        sentenceList = nltk.sent_tokenize(content)
        nlp = en_core_web_lg.load()
        for sentence in sentenceList:
            doc = nlp(sentence)
            for token in doc.ents:
                if token.label_ == 'DATE':
                    datesContainerNumbers.append(token.text)
        datesContainerNumbers = nltk.flatten(datesContainerNumbers)
        for toReplaceNumbers in datesContainerNumbers:
            toReplace = str(toReplaceNumbers)
            tempHolder.append(toReplace)
        for listValue in scenario1:
            if len(listValue) == 0:
                del listValue
                continue
            for data in listValue:
                temp = ""
                for tupleValue in data:
                    if tupleValue != ",":
                        temp = temp + " " + tupleValue
                    else:
                        temp = temp + tupleValue
                tempHolder.append(temp.strip())
        for temp in datesContainerLetters:
            if len(temp) == 0:
                del temp
                continue
            for value in temp:
                valueToAppend = ''
                for tupleValue in value:
                    valueToAppend = (valueToAppend + tupleValue)+" "
                tempHolder.append(valueToAppend.strip())
        for redundent in redundentValues:
            tempHolder.append(redundent)
        redactContents['dates'] = tempHolder
        return redactContents

    def redactPhones(self, fileName, redactContents):
        try:
            content = open(fileName, 'r').read()
        except (FileNotFoundError, IOError, Exception) as error:
            print(f"Following error was raised when reading a file {error.args}")
        tempHolder = []
        phonesList = []
        phonesSecondaryList = []
        phonesList.append(re.findall(
            r"([+][\d]{1})\s([\d]{10})", content))
        phonesList.append(re.findall(
            r"([+][\d]{1})\s([\d]{3}[-][\d]{3}[-][\d]{4})", content))
        phonesList.append(re.findall(
            r"([+][\d]{1})\s([(][\d]{3}[)][\d]{3}[-][\d]{4})", content))
        phonesList.append(re.findall(
            r"([(][+][\d]{1}[)])\s([\d]{3}[\d]{3}[\d]{4})", content))
        phonesList.append(re.findall(
            r"([(][+][\d]{1}[)])\s([\d]{3}[-][\d]{3}[-][\d]{4})", content))
        phonesSecondaryList.append(re.findall(
            r"([(][\d]{3}[)][-][\d]{3}[-][\d]{4})", content))
        phonesSecondaryList.append(re.findall(
            r"([(][\d]{3}[)][\d]{3}[-][\d]{4})", content))
        phonesSecondaryList.append(re.findall(
            r"([\d]{3}[\d]{3}[\d]{4})", content))
        phonesSecondaryList.append(re.findall(
            r"([\d]{3}[-][\d]{3}[-][\d]{4})", content))
        phonesSecondaryList.append(re.findall(
            r"([(][\d]{3}[)]\s[\d]{3}[-][\d]{4})", content))
        primaryPhonesList = []
        for data in phonesList:
            for secondValue in data:
                temp = ''
                for thirdTupleValue in secondValue:
                    temp = temp + thirdTupleValue + ' '
                primaryPhonesList.append(temp)
        for primaryValue in primaryPhonesList:
            primaryValue = primaryValue.strip()
            tempHolder.append(primaryValue)
        phonesSecondaryList = nltk.flatten(phonesSecondaryList)
        for secondaryValue in phonesSecondaryList:
            if len(secondaryValue) == 10:
                if secondaryValue[0] == 0 or secondaryValue[0] == 1:
                    continue
            else:
                tempHolder.append(secondaryValue)
        redactContents['phones'] = tempHolder
        return redactContents

    def redactAddress(self, fileName, redactContents):
        try:
            content = open(fileName, 'r').read()
        except (FileNotFoundError, IOError, Exception) as error:
            print(f"Following error was raised when reading a file {error.args}")
        tempHolder = []
        addressRedactList = pyap.parse(content, country="US")
        for address in addressRedactList:
            tempHolder.append(str(address))
        redactContents['address'] = tempHolder
        return redactContents

    def redactConcept(self, fileName, concept):
        synonyms = wordnet.synsets(concept)
        conceptWords = []
        resultList = []
        for word in synonyms:
            conceptWords.append(word.lemma_names())
        conceptWords = nltk.flatten(conceptWords)
        try:
            content = open(fileName, 'r').read()
        except (FileNotFoundError, IOError, Exception) as error:
            print(f"Following error was raised when reading a file {error.args}")
        sentenceList = nltk.sent_tokenize(content)
        for sentence in sentenceList:
            addToList = False
            contentList = nltk.word_tokenize(sentence)
            for word in contentList:
                if word in conceptWords and addToList is False:
                    addToList = True
            if addToList:
                resultList.append(sentence)
        return resultList

    def redactGenders(self, fileName, redactContents):
        try:
            content = open(fileName, 'r').read()
        except (FileNotFoundError, IOError, Exception) as error:
            print(f"Following error was raised when reading a file {error.args}")
        tempHolder = []
        genderWords = ['he', 'him', 'his', 'male', 'man', 'men', 'He', 'Him', 'His', 'Male', 'Man', 'Men', 'HE', 'HIM', 'HIS', 'MALE', 'MAN', 'MEN', 'guy',
                       'spokesman', 'spokesperson', 'chairman', "he's", 'boy', 'boys', 'boyfriend', 'boyfriends', 'brother', 'brothers', 'dad', "dad's",
                       'dude', 'father', "father's", 'fiance', 'gentleman', 'gentlemen', 'god', 'grandfather', 'grandpa', 'grandson', 'groom', 'himself',
                       'husband', 'husbands', 'King', 'king', 'nephew', 'nephews', 'prince', 'son', "son's", 'sons', 'uncle', "uncle's", 'she', 'her', 'female',
                       'women', 'woman', 'She', 'Her', 'Female', 'Woman', 'Women', 'SHE', 'HER', 'FEMALE', 'WOMEN', 'WOMAN', 'FIANCE', 'widow', 'Widow',
                       'widower', "Widower's", 'heroine', 'Heroine', 'spokeswoman', 'Spokeswoman', 'Chairwoman', 'chairwoman', 'Fiancee', 'fiancee', 'girl',
                       'Girl', 'girlfriend', 'Girlfriend', 'girlfriends', 'Girlfriends', 'girls', 'Girls', 'goddess', 'Goddess', 'granddaughter', 'Granddaughter',
                       'grandma', 'Grandma', 'grandmother', 'Grandmother', 'herself', 'Herself', 'lady', 'Lady', 'ladies', 'Ladies', 'Mom', 'mom', 'Mother', 'mother'
                       'niece', 'Niece', 'princess', 'queen', 'sister', 'Queen', 'Sister', 'wife', 'Wife', 'wives', 'Wives']
        genderWordsList = nltk.tokenize.word_tokenize(content)
        for word in genderWordsList:
            if word in genderWords:
                tempHolder.append(word)
        redactContents['genders'] = tempHolder
        return redactContents

    def redactContent(self, args, fileName, redactContents):
        try:
            content = open(fileName, 'r').read()
        except (FileNotFoundError, IOError, Exception) as error:
            print(f"Following error was raised when reading a file {error.args}")
        if args.stats == 'stdout':
            sys.stdout.write("\n***********\t" + "stats for " + fileName + "\t***********")
        elif args.stats == 'stderr':
            sys.stderr.write("\n***********\t" + "stats for " + fileName + "\t***********")
        else:
            writeToStatFile = open(args.stats + '/stat.txt', mode="a")
            writeToStatFile.write("\n******************** \t " + fileName + " \t ***********************")

        if args.concept:
            count = 0
            toReplaceList = redactContents.get('concept')
            for sentence in toReplaceList:
                count += 1
                content = content.replace(sentence, "█" * len(sentence))
            if args.stats == 'stdout':
                sys.stdout.write("\n Total concepts Redacted:  " + str(count))
            elif args.stats == 'stderr':
                sys.stderr.write("\n Total concepts Redacted:  " + str(count))
            else:
                writeToStatFile.write("\n Total concepts Redacted:  " + str(count))

        if args.address:
            toReplaceList = redactContents.get('address')
            count = 0
            for word in toReplaceList:
                if word in content:
                    count += 1
                    content = content.replace(word, "█" * len(word))
            if count == 0 and len(toReplaceList) > 0:
                exceptionalCase = []
                for word in toReplaceList:
                    exceptionalCase.append(word.split(","))
                exceptionalCase = nltk.flatten(exceptionalCase)
                for word in exceptionalCase:
                    word = word.strip()
                    if word in content:
                        content = content.replace(word, "█" * len(word))
                count = len(toReplaceList)
            if args.stats == 'stdout':
                sys.stdout.write("\n Total number of address redacted:  " + str(count))
            elif args.stats == 'stderr':
                sys.stderr.write("\n Total number of address redacted:  " + str(count))
            else:
                writeToStatFile.write("\n Total number of address redacted:  " + str(count))

        if args.names:
            toReplaceList = redactContents.get('names')
            count = 0
            for word in toReplaceList:
                if word in content and word != 'PLEASE' and word != 'Please' and word != 'Hello' and word != 'HELLO':
                    count += 1
                    content = content.replace(word, "█" * len(word))
            if args.stats == 'stdout':
                sys.stdout.write("\n Total Names Redacted: \t " + str(count))
            elif args.stats == 'stderr':
                sys.stderr.write("\n Total Names Redacted: \t " + str(count))
            else:
                writeToStatFile.write("\n Total Names Redacted: \t " + str(count))

        if args.dates:
            count = 0
            toReplaceList = redactContents.get('dates')
            for word in toReplaceList:
                if word in content:
                    count += 1
                    content = content.replace(word, "█" * len(word))
            if args.stats == 'stdout':
                sys.stdout.write("\n Total Dates Redacted: \t " + str(count))
            elif args.stats == 'stderr':
                sys.stderr.write("\n Total Dates Redacted: \t " + str(count))
            else:
                writeToStatFile.write("\n Total Dates Redacted: \t " + str(count))

        if args.phones:
            toReplaceList = redactContents.get('phones')
            count = 0
            for word in toReplaceList:
                if word in content:
                    count += 1
                    content = content.replace(word, "█" * len(word))
            if args.stats == 'stdout':
                sys.stdout.write("\n Total Phone Numbers Redacted:  " + str(count))
            elif args.stats == 'stderr':
                sys.stderr.write("\n Total Phone Numbers Redacted:  " + str(count))
            else:
                writeToStatFile.write("\n Total Phone Numbers Redacted:  " + str(count))

        if args.genders:
            count = 0
            toReplaceList = redactContents.get('genders')
            for toReplace in toReplaceList:
                if toReplace in content:
                    count += 1
                    content = re.sub(toReplace + "\s", "█"*len(toReplace) + " ", content)
                    content = re.sub("\W"+toReplace+"\W", " "+"█"*len(toReplace)+" ", content)
                    content = re.sub("\s" + toReplace + "\W", " " + "█"*len(toReplace), content)
            if args.stats == 'stdout':
                sys.stdout.write("\n Total genders Redacted:  " + str(count))
            elif args.stats == 'stderr':
                sys.stderr.write("\n Total genders Redacted:  " + str(count))
            else:
                writeToStatFile.write("\n Total genders Redacted:  " + str(count))
                writeToStatFile.close()

        return content








