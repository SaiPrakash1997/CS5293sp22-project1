import nltk
import spacy
from nltk.tree import Tree
from nltk.corpus import wordnet
import re
import pyap
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
nltk.download('omw-1.4')


class redactFiles:
    def __init__(self):
        pass

    def redactNames(self, directoryName, fileName, redactContents):
        content = open(fileName, 'r').read()
        print("content:", content)
        content = content.strip()
        sentenceList = nltk.sent_tokenize(content)
        print("sentence List:", sentenceList)
        nlp = spacy.blank("en")
        nlp = spacy.load('en_core_web_lg')
        namesHoldingList = []
        for sentence in sentenceList:
            print("sentence:", sentence)
            doc = nlp(sentence)
            print("doc:", doc)
            for token in doc.ents:
                print("token:", token, "label:", token.label_)
                if token.label_ == 'PERSON':
                    namesHoldingList.append(token.text)
        print(" Values in namesHoldingList selected by spacy library:", namesHoldingList)
        wordsList = nltk.tokenize.word_tokenize(content)
        print("words in list:", wordsList)
        tagList = nltk.pos_tag(wordsList)
        print("tag list:", tagList)
        chunkedList = nltk.ne_chunk(tagList)
        print("chunk list:", chunkedList)
        for entities in chunkedList:
            if type(entities) == Tree and entities.label() == 'PERSON':
                namesHoldingList.append(' '.join([chunk[0] for chunk in entities]))
        print("contents in the redactContent list:", namesHoldingList)
        print("File Path:", directoryName+'/stat.txt')
        writeToStatFile = open(directoryName+'/stat.txt', mode="a")
        writeToStatFile.write("\n******************** \t "+fileName+" \t ***********************")
        writeToStatFile.write("\n Total Names Redacted: \t "+str(len(namesHoldingList)))
        writeToStatFile.close()
        redactContents['names'] = namesHoldingList
        return redactContents

    def redactDates(self, directoryName, fileName, redactContents):
        content = open(fileName, 'r').read()
        tempHolder = []
        datesContainerLetters = []
        datesContainerNumbers = []
        finalDatesContainer = []
        monthsContainer = ['january', 'January', 'February', 'february', 'March', 'march', 'April', 'april', 'May', 'may', 'June', 'june', 'July',
                  'july', 'August', 'august', 'September', 'september', 'October', 'october', 'November', 'november', 'december', 'December',
                  'jan', 'Jan', 'feb', 'Feb', 'mar', 'Mar', 'apr', 'Apr', 'may', 'May', 'jun', 'Jun', 'jul', 'Jul', 'aug', 'Aug', 'sep', 'Sep',
                  'oct', 'Oct', 'nov', 'Nov', 'dec', 'Dec']
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2}.{2})\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2}.{2})\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{1,2}.{2},)\s([\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{1,2}.{2},)\s([\d]{4})",
            content))
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2}.{2})\s([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]anuary?|[fF]ebruary?|[mM]arch?|[aA]pril?|[mM]ay?|[jJ]une?|[jJ]uly?|[aA]ugust?|[sS]eptember?|[oO]ctober?|[nN]ovember?|[dD]ecember?)\s([\d]{1,2}.{2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)\s([\d]{1,2}.{2})",
            content))
        datesContainerLetters.append(re.findall(
            r"([\d]{1,2}.{2})\s([jJ]an?|[fF]eb?|[mM]ar?|[aA]pr?|[mM]ay?|[jJ]un?|[jJ]ul?|[aA]ug?|[sS]ep?|[oO]ct?|[nN]ov?|[dD]ec?)",
            content))
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
        print("String format dates in datesContainer:", datesContainerLetters)
        print("Number format dates in datesContainer:", datesContainerNumbers)
        for temp in datesContainerLetters:
            print('temp:', temp)
            print("Value:", temp, "length:", len(temp))
            if len(temp) == 0:
                del temp
                continue
            for value in temp:
                print('value:', value)
                valueToAppend = ''
                for tupleValue in value:
                    print('tupleValue:', tupleValue)
                    valueToAppend = (valueToAppend + tupleValue)+" "
                print("Values appended:", valueToAppend)
                finalDatesContainer.append(valueToAppend)
        print("String format in finalDatesContainer:", finalDatesContainer)
        for toReplace in finalDatesContainer:
            toReplace = toReplace.strip()
            print("Value to be replaced:", toReplace)
            tempHolder.append(toReplace)
        datesContainerNumbers = nltk.flatten(datesContainerNumbers)
        for toReplaceNumbers in datesContainerNumbers:
            toReplace = str(toReplaceNumbers)
            print("Value to be replaced:", toReplace)
            tempHolder.append(toReplace)
        monthsInWords = nltk.tokenize.word_tokenize(content)
        print("months in list:", monthsInWords)
        matched = 0
        for month in monthsInWords:
            if month in monthsContainer:
                print("Value matched:", month)
                matched += 1
                tempHolder.append(month)
        print("dates in the redactContent list:", tempHolder)
        writeToStatFile = open(directoryName + '/stat.txt', mode="a")
        print("\n Total Dates Redacted: \t " + str(len(finalDatesContainer)+len(datesContainerNumbers)+matched))
        writeToStatFile.write("\n Total Dates Redacted: \t " + str(len(finalDatesContainer)+len(datesContainerNumbers)+matched))
        writeToStatFile.close()
        redactContents['dates'] = tempHolder
        return redactContents

    def redactPhones(self, directoryName, fileName, redactContents):
        content = open(fileName, 'r').read()
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
        print("Selected phone Values:", phonesList)
        primaryPhonesList = []
        for data in phonesList:
            print("value selected in phonesList:", data)
            for secondValue in data:
                temp = ''
                print("value selected in inner List:", secondValue)
                for thirdTupleValue in secondValue:
                    print("value selected in tuple:", thirdTupleValue)
                    temp = temp + thirdTupleValue + ' '
                print("value adding before list:", temp)
                primaryPhonesList.append(temp)
        print("Primary Phone type values in list:", primaryPhonesList)
        print("Secondary Phone type values in list:", phonesSecondaryList)
        for primaryValue in primaryPhonesList:
            primaryValue = primaryValue.strip()
            tempHolder.append(primaryValue)
        phonesSecondaryList = nltk.flatten(phonesSecondaryList)
        for secondaryValue in phonesSecondaryList:
            tempHolder.append(secondaryValue)
        print("phone numbers in the redactContent list:", tempHolder)
        writeToStatFile = open(directoryName + '/stat.txt', mode="a")
        print("\n Total Phone Numbers Redacted:  " + str(len(primaryPhonesList)+len(phonesSecondaryList)))
        writeToStatFile.write(
            "\n Total Phone Numbers Redacted:  " + str(len(primaryPhonesList)+len(phonesSecondaryList)))
        writeToStatFile.close()
        redactContents['phones'] = tempHolder
        print(f"Final phone values in tempHolder: {tempHolder}")
        return redactContents

    def redactAddress(self, directoryName, fileName, redactContents):
        content = open(fileName, 'r').read()
        tempHolder = []
        addressRedactList = pyap.parse(content, country="US")
        for address in addressRedactList:
            tempHolder.append(address)
        writeToStatFile = open(directoryName + '/stat.txt', mode="a")
        print("\n Number of address redacted:  " + str(len(tempHolder)))
        writeToStatFile.write(
            "\n Number of address redacted:  " + str(len(tempHolder)))
        writeToStatFile.close()
        redactContents['address'] = tempHolder
        return redactContents

    def redactConcept(self, directoryName, fileName, redactContents, concept):
        synonyms = wordnet.synsets(concept)
        conceptWords = []
        tempHolder = []
        for word in synonyms:
            conceptWords.append(word.lemma_names())
        conceptWords = nltk.flatten(conceptWords)
        content = open(fileName, 'r').read()
        sentenceList = nltk.sent_tokenize(content)
        for sentence in sentenceList:
            addToList = False
            contentList = nltk.word_tokenize(sentence)
            for word in contentList:
                if word in conceptWords and addToList is False:
                    addToList = True
            if addToList:
                tempHolder.append(sentence)
        writeToStatFile = open(directoryName + '/stat.txt', mode="a")
        print("\n Total concepts Redacted:  " + str(len(tempHolder)))
        writeToStatFile.write(
            "\n Total concepts Redacted:  " + str(len(tempHolder)))
        writeToStatFile.close()
        redactContents['concept'] = tempHolder
        return redactContents

    def redactGenders(self, directoryName, fileName, redactContents):
        content = open(fileName, 'r').read()
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
        print("Words:", genderWordsList)
        for word in genderWordsList:
            if word in genderWords:
                tempHolder.append(word)
        writeToStatFile = open(directoryName + '/stat.txt', mode="a")
        print("\n Total genders Redacted:  " + str(len(tempHolder)))
        writeToStatFile.write(
            "\n Total genders Redacted:  " + str(len(tempHolder)))
        writeToStatFile.close()
        redactContents['genders'] = tempHolder
        return redactContents

    def redactContent(self, args, fileName, redactContents):
        content = open(fileName, 'r').read()
        if args.concept:
            toReplaceList = redactContents.get('concept')
            for sentence in toReplaceList:
                content = content.replace(sentence, "█" * len(sentence))
        if args.names:
            toReplaceList = redactContents.get('names')
            for word in toReplaceList:
                content = content.replace(word, "█" * len(word))
        if args.dates:
            toReplaceList = redactContents.get('dates')
            for word in toReplaceList:
                content = content.replace(word, "█" * len(word))
        if args.phones:
            toReplaceList = redactContents.get('phones')
            for word in toReplaceList:
                content = content.replace(word, "█" * len(word))
        if args.address:
            toReplaceList = redactContents.get('address')
            for word in toReplaceList:
                content = content.replace(word, "█" * len(word))
        if args.genders:
            tempContent = ''
            toReplaceList = redactContents.get('genders')
            endSymbols = ['.', ',', '!', '?', ';', ':']
            genderWordsList = nltk.tokenize.word_tokenize(content)
            for word in genderWordsList:
                if word in toReplaceList and tempContent != '':
                    tempContent = tempContent + ' ' + "█"*len(word)
                elif word in toReplaceList and tempContent == '':
                    tempContent = "█" * len(word)
                elif tempContent == '':
                    tempContent = tempContent + word
                elif tempContent != '' and word not in endSymbols:
                    tempContent = tempContent + ' ' + word
                elif tempContent != '' and word in endSymbols:
                    tempContent = tempContent + word
            content = tempContent
        return content








