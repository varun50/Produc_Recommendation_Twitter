# -*- coding: utf-8 -*-
"""
Varun Singh
"""

import twitter, json, os
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob



#reload(sys)
#sys.setdefaultencoding("utf-8")


#setup for the twitter API to allow query
myApi=twitter.Api(consumer_key='MIOSNRkdWXrNLXQ8m8mwnA', \
                  consumer_secret='csAAjdPuf9VnaHcL9Hg3hDflno9dZzY51HaFTOiie0', \
                 access_token_key='142176672-ydnzn7T9sCaR5b0bVwWaiMc6qFlCbGrtjkj3rO8C', \
                  access_token_secret='UBnMax7ociuNzeEn42sPLPnmgbGNPsN2nmMqqXckvCBU2')

#myApi=twitter.Api(consumer_key='O4vlPtkyBQVtOpUgCzvikg', \
            #consumer_secret='saCPhhqWI1EqhvGTYMm4bMwnQ6gobYCYWFMBBGYBgs', \
            #access_token_key='2320154102-uwj7p6JDC0DOopubMLPnxHANqCkfIDlnSf7LQdd', \
            #access_token_secret='1KXAnqafOpVDF0URg2Nb6l1Cst44zEZM1ODSTi6jkN8sT')

#Training Data
train = [
        (':)', 'pos'),
        (':(', 'neg'),
        ('is an awesome phone', 'pos'),
        ('is beautiful machine', 'pos'),
        ('is very good person', 'pos'),
        ('is very fantastic', 'pos'),
        ('is hero', 'pos'),
        ('is very awesome product', 'pos'),
        ('good product', 'pos'),
        ('user friendly', 'pos'),
        ('the best', 'pos'),
        ('nicely built', 'pos'),
        ('is an excellent product', 'pos'),
        ('horrible battery life', 'neg'),
        ('not a good machine', 'neg'),
        ('worst ever', 'neg'),
        ('best investment I have made', 'pos'),
        ('this phone really sucks', 'neg')
    ]


def rest_query(product1):
    filename = 'consumer.json'
    f = open(filename, 'w')
    b = '[\n'
    c = '\n]'
    f.write(b)
    print product1
    
    first = '('
    second = ')'
    middle = str(product1)

    temp = first + middle
    product = temp + second

    print product + '\n'

    User_freq = dict()    #set up dictionary mapping of users
    count = 0

    #queries to disclude from serach
    disclude = 'AND -case AND -cases AND -filter:links AND -RT'


    #Positive Queries
    query1 = 'AND (awesome OR amazing OR favorable)'
    query2 = 'AND (recommend OR fantastic OR excellent)'
    query3 = 'AND (better OR best OR love)'
    query4 = 'AND (outstanding OR perfect)'
    query5 = 'AND :)'
    query6 = 'AND (ultimate OR smart OR great)'
    queryall = 'AND (awesome OR amazing OR favorable OR recommend OR fantastic OR excellent) '

    #Where the program queries twitter's servers for tweets
    raw_tweets = myApi.GetSearch(product + query1 + disclude, count = 1500, result_type='recent')
    raw_tweets2 = myApi.GetSearch(product + query2 + disclude, count = 1500, result_type='recent')
    raw_tweets3 = myApi.GetSearch(product + query3 + disclude, count = 1500, result_type='recent')
    raw_tweets4 = myApi.GetSearch(product + query4 + disclude, count = 1500, result_type='recent')
    raw_tweets5 = myApi.GetSearch(product + query5 + disclude, count = 1500, result_type='recent')
    raw_tweets6 = myApi.GetSearch(product + query6 + disclude, count = 1500, result_type='recent')
    raw_tweets14 = myApi.GetSearch(product + queryall + disclude, count = 1500, result_type='popular')
    raw_tweets15 = myApi.GetSearch(product + query5 + disclude, count = 1500, result_type='popular')



    write_tweets(raw_tweets, User_freq, f, 1)
    write_tweets(raw_tweets2, User_freq, f, 1)
    write_tweets(raw_tweets3, User_freq, f, 1)
    write_tweets(raw_tweets4, User_freq, f, 1)
    write_tweets(raw_tweets5, User_freq, f, 1)
    write_tweets(raw_tweets6, User_freq, f, 1)
    write_tweets(raw_tweets14, User_freq, f, 1)
    write_tweets(raw_tweets15, User_freq, f, 1)

    #Negative Queries
    query7 = 'AND (awful OR bad OR awkward OR terrible)'
    query8 = 'AND (unsatisfactory OR dreadful OR downgrade)'
    query9 = 'AND (lame OR boring OR flawed OR lacking)'
    query10 = 'AND (sad OR laughable OR regret)'
    query11 = 'AND (disapointed OR disapointing OR sucks)'
    query12 = "AND (don't) AND (recommend)"
    query13 = ':('

    raw_tweets7 = myApi.GetSearch(product + query7 + disclude, count = 1500, result_type='recent')
    raw_tweets8 = myApi.GetSearch(product + query8 + disclude, count = 1500, result_type='recent')
    raw_tweets9 = myApi.GetSearch(product + query9 + disclude, count = 1500, result_type='recent')
    raw_tweets10 = myApi.GetSearch(product + query10 + disclude, count = 1500, result_type='recent')
    raw_tweets11 = myApi.GetSearch(product + query11 + disclude, count = 1500, result_type='recent')
    raw_tweets12 = myApi.GetSearch(product + query12 + disclude, count = 1500, result_type='recent')
    raw_tweets13 = myApi.GetSearch(product + query13 + disclude, count = 1500, result_type='recent')
    raw_tweets16 = myApi.GetSearch(product + query13 + disclude, count = 1500, result_type='popular')

    write_tweets(raw_tweets7, User_freq, f, 0)
    write_tweets(raw_tweets8, User_freq, f, 0)
    write_tweets(raw_tweets9, User_freq, f, 0)
    write_tweets(raw_tweets10, User_freq, f, 0)
    write_tweets(raw_tweets11, User_freq, f, 0)
    write_tweets(raw_tweets12, User_freq, f, 0)
    write_tweets(raw_tweets13, User_freq, f, 0)
    write_tweets(raw_tweets16, User_freq, f, 0)

    f.close()
    d = open(filename, 'rb+')
    d.seek(-2, os.SEEK_END)
    d.truncate()
    d.write(c)


    filename = 'Users.txt'
    f = open(filename, 'w')
 
    for user_id, freq in sorted(User_freq.items(), key = lambda item: item[1] * -1):
    #sorts dictionary that was created, prints users that have more than 2
    #tweets from queries
        f.write('User:  {}  Freq:   {}'.format(user_id, freq)+ '\n')
    f.close()
    
    


def analyze_tweets(cl):

    file = 'consumer.json'
    f = open(file, 'r')
    data = f.read()
    blob = TextBlob(data,classifier=cl)

    a = blob.classify()

    print 'The product have an overall ' + a + ' rating\n'
    #print 'The majority of the tweets that were positive are ' + str(b) + '\n'
    #print 'The percent of the tweets that were negative are ' + str(c) + '\n'
    return 'The product have an overall ' + a + ' rating\n'

def write_tweets(tweets, User_freq, f, s):

    for raw_tweet in tweets:
        tweet = json.loads(str(raw_tweet))
        if User_freq.has_key(tweet['user']['screen_name']): #checks dictionary for user
            User_freq[tweet['user']['screen_name']] += 1
        else:
            User_freq[tweet['user']['screen_name']] = 1
            if s == 1:
                f.write('{"text": ' + json.dumps(tweet['text']) + ', "label": "pos"},' '\n')
            else:
                f.write('{"text": ' + json.dumps(tweet['text']) + ', "label": "neg"},' '\n')


def run_query(product1):
    rest_query(product1)
    cl = NaiveBayesClassifier(train)
    msg = analyze_tweets(cl)
    return msg



