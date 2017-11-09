import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        #load positive and negative words make it self.positives, self.negatives use list,dict or set
        #omit leading/trailing white space, use str.strip()
        #don't include comments. use str.startswith
        self.positives =[x.strip() for x in open(positives,'r').readlines() if not x.startswith(";")]
        self.negatives =[x.strip() for x in open(negatives,'r').readlines() if not x.startswith(";")]

        # TODO-DONE
        
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        #tokenize text tokens = self.tokenizer.tokenize(text)
        #iterate over tokens str.lower
        #check if word is positive or negative
        #assign each word in text a value(-1,0,1)
        #calculate text total score
        tokenizer=nltk.tokenize.casual.TweetTokenizer()
        score=0
        for word in tokenizer.tokenize(text):
            score+=(lambda positive,negative,word: 1 if word in positive else -1 if word in negative else 0)(self.positives, self.negatives,word.lower())
        
        #return score

        # TODO - DONE
        return score
