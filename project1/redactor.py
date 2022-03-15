import nltk
import spacy
from nltk.tree import Tree
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


class redactFiles:
    def __init__(self):
        self.namesHoldingList = []

    def redactNames(self, fileName):

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
        print("Final Content:", content)
