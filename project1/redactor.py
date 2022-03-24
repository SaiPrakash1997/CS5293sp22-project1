import nltk
import spacy
from nltk.tree import Tree
import re
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


class redactFiles:
    def __init__(self):
        self.namesHoldingList = []

    def redactNames(self, fileName, directoryName):
        content = open(fileName, 'r').read()
        print("content:", content)
        content = content.strip()
        sentenceList = nltk.sent_tokenize(content)
        print("sentence List:", sentenceList)
        namesHoldingList = []
        nlp = spacy.blank("en")
        nlp = spacy.load('en_core_web_lg')
        for sentence in sentenceList:
            print("sentence:", sentence)
            doc = nlp(sentence)
            print("doc:", doc)
            for token in doc.ents:
                print("token:", token, "label:", token.label_)
                if token.label_ == 'PERSON':
                    namesHoldingList.append(token.text)
        print(" Values in namesHoldingList:", namesHoldingList)
        wordsList = nltk.tokenize.word_tokenize(content)
        print("words in list:", wordsList)
        tagList = nltk.pos_tag(wordsList)
        print("tag list:", tagList)
        chunkedList = nltk.ne_chunk(tagList)
        print("chunk list:", chunkedList)
        for entities in chunkedList:
            if type(entities) == Tree and entities.label() == 'PERSON':
                namesHoldingList.append(' '.join([chunk[0] for chunk in entities]))
        for toReplaceNames in namesHoldingList:
            content = content.replace(toReplaceNames, "█"*len(toReplaceNames))
        print("File Path:", directoryName+'/stat.txt')
        writeToStatFile = open('project1/'+directoryName+'/stat.txt', mode="a")
        writeToStatFile.write("\n******************** \t "+fileName+" \t ***********************")
        writeToStatFile.write("\n Total Names Redacted: \t "+str(len(namesHoldingList)))
        writeToStatFile.close()
        print("Final content after name redaction:", content)
        return content

    def redactDates(self, directoryName, content):
        datesContainerLetters = []
        datesContainerNumbers = []
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
        finalDatesContainer = []
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
            content = content.replace(toReplace, "█"*len(toReplace))
        datesContainerNumbers = nltk.flatten(datesContainerNumbers)
        for toReplaceNumbers in datesContainerNumbers:
            toReplace = str(toReplaceNumbers)
            print("Value to be replaced:", toReplace)
            content = content.replace(toReplace, "█"*len(toReplace))
        monthsInWords = nltk.tokenize.word_tokenize(content)
        print("months in list:", monthsInWords)
        matched = 0
        for months in monthsInWords:
            if months in monthsContainer:
                print("Value matched:", months)
                matched += 1
                content = content.replace(months, "█"*len(months))

        writeToStatFile = open('project1/' + directoryName + '/stat.txt', mode="a")
        print("\n Total Dates Redacted: \t " + str(len(finalDatesContainer)+len(datesContainerNumbers)+matched))
        writeToStatFile.write("\n Total Dates Redacted: \t " + str(len(finalDatesContainer)+len(datesContainerNumbers)+matched))
        writeToStatFile.close()
        print("content after date redaction:", content)
        return content

    def redactPhones(self, directoryName, content):
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
            content = content.replace(primaryValue, "█"*len(primaryValue))
        phonesSecondaryList = nltk.flatten(phonesSecondaryList)
        for secondaryValue in phonesSecondaryList:
            content = content.replace(secondaryValue, "█"*len(secondaryValue))
        writeToStatFile = open('project1/' + directoryName + '/stat.txt', mode="a")
        print("\n Total Phone Numbers Redacted:  " + str(len(primaryPhonesList)+len(phonesSecondaryList)))
        writeToStatFile.write(
            "\n Total Phone Numbers Redacted:  " + str(len(primaryPhonesList)+len(phonesSecondaryList)))
        writeToStatFile.close()
        print("content after phones redaction:", content)
        return content

    def redactGenders(self, directoryName, content):
        genderWords = ['he', 'him', 'his', 'male', 'man', 'men', 'He', 'Him', 'His', 'Male', 'Man', 'Men', 'HE', 'HIM', 'HIS', 'MALE', 'MAN', 'MEN', 'guy',
                       'spokesman', 'spokesperson', 'chairman', "he's", 'boy', 'boys', 'boyfriend', 'boyfriends', 'brother', 'brothers', 'dad', "dad's",
                       'dude', 'father', "father's", 'fiance', 'gentleman', 'gentlemen', 'god', 'grandfather', 'grandpa', 'grandson', 'groom', 'himself',
                       'husband', 'husbands', 'King', 'king', 'nephew', 'nephews', 'prince', 'son', "son's", 'sons', 'uncle', "uncle's", 'she', 'her', 'female',
                       'women', 'woman', 'She', 'Her', 'Female', 'Woman', 'Women', 'SHE', 'HER', 'FEMALE', 'WOMEN', 'WOMAN', 'FIANCE', 'widow', 'Widow',
                       'widower', "Widower's", 'heroine', 'Heroine', 'spokeswoman', 'Spokeswoman', 'Chairwoman', 'chairwoman', 'Fiancee', 'fiancee', 'girl',
                       'Girl', 'girlfriend', 'Girlfriend', 'girlfriends', 'Girlfriends', 'girls', 'Girls', 'goddess', 'Goddess', 'granddaughter', 'Granddaughter',
                       'grandma', 'Grandma', 'grandmother', 'Grandmother', 'herself', 'Herself', 'lady', 'Lady', 'ladies', 'Ladies', 'Mom', 'mom', 'Mother', 'mother'
                       'niece', 'Niece', 'princess', 'queen', 'sister', 'Queen', 'Sister', 'wife', 'Wife', 'wives', 'Wives']
        print("content:", content)
        genderWordsList = nltk.tokenize.word_tokenize(content)
        print("Words:", genderWordsList)
        genderStatCount = 0
        tempContent = ''
        endSymbols = ['.', ',', '!', '?', ';', ':']
        for word in genderWordsList:
            if word in genderWords and tempContent != '':
                genderStatCount += 1
                tempContent = tempContent + ' ' + "█"*len(word)
            elif word in genderWords and tempContent == '':
                genderStatCount += 1
                tempContent = "█" * len(word)
            elif tempContent == '':
                tempContent = tempContent + word
            elif tempContent != '' and word not in endSymbols:
                tempContent = tempContent + ' ' + word
            elif tempContent != '' and word in endSymbols:
                tempContent = tempContent + word
        writeToStatFile = open('project1/' + directoryName + '/stat.txt', mode="a")
        print("\n Total genders Redacted:  " + str(genderStatCount))
        writeToStatFile.write(
            "\n Total genders Redacted:  " + str(genderStatCount))
        writeToStatFile.close()
        print("content after gender redaction:", tempContent)
        return tempContent







