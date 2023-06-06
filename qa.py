
import os
import openai
import numpy as np
import matplotlib.pyplot as plt

openai.api_key = os.getenv("OPENAI_API_KEY")

tweets=[]
#handle ='FINAL_LEVEL'
#handle = 'tszzl'
handle = 'karpathy'
#handle = 'realdonaldtrump'

filename = "./tweets_"+handle+".txt"
with open(filename) as file:
    for line in file:
        tweets.append(line.rstrip())


print(len(tweets), "tweets in total.")

prompt_base = 'Write the question that could have elicited the following answer:\nAnswer: '
tweetswq = []

#tweets=tweets[15:18]

for (numtweet, tweet) in enumerate(tweets):
    print("Generating question for tweet", numtweet)
    prompt =  prompt_base+tweet+"\nQuestion:"
    try:
        response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=30)
    except:
        print("Error on tweet", numtweet,", question not generated.")
        continue
    tweetswq.append("[[Q:]]"+response['choices'][0]['text']+" [[A:]] "+tweet)
    #tweetswq.append("<human:>"+response['choices'][0]['text']+"\n<bot:> "+tweet)

outfile = "./tweetswq_"+handle+".txt"
with open(outfile, 'w') as f:
    for line in tweetswq:
        f.write(line+"\n")

