import nltk
# nltk.download('punkt')
from nltk.tag.stanford import StanfordNERTagger
st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar')
# st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')

def getName(text):
    # tags = st.tag(text.split())
    # print(text)
    names = []
    personNames = []
    for sent in nltk.sent_tokenize(text):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            names.append(tag)
            if tag[1] == 'PERSON':
                personNames.append(tag[0])
    name = " ".join(personNames)
    # print("names", names)
    # print("name", name)

    return name
