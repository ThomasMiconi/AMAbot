# AMAbot


This repo inclcudes code for training an AMAbot ("Ask Me Anything" bot). An
AMAbot answers questions in the style of one or several personalities.  

A fully trained model (fine-tuned with LoRA on top of 
[RedPajama-INCITE-7B-Chat](https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Chat)) is [available on HuggingFace](https://huggingface.co/AMAbot/AMAbot-7B). It should run on any GPU with 16GB RAM.

## Principle

AMAbot training  data is collected as follows:

1. Collect a corpus of text from your chosen personality/personalities (preferably  in  small self-contained chunks, e.g. tweets)
2. For each small chunk, ask another language model to generate questions that could have elicited this chunk as an answer (here we use ChatGPT 3.5)
3. Prefix each question and answer with a marker for this particular personality (e.g. "Q for [NAME]:"), so you can train a single model to imitate multiple personalities
4. Fine-tune a chat-oriented  large language model on this data

## Example generations

```
<human>: Q for Karpathy: What is your favorite programming language?
<bot>: (Karpathy talking) My favorite programming language is still Matlab, which I started using in 6th grade for my homework problems. The syntax is terse, expressive, and makes you think about what you're trying to say. I miss it so much. I can't tell if this is a joke or not
```
```
<human>: Q for Ice-T: What is the sound of one hand clapping?
<bot>: (Ice-T talking) ICE COLD FACT: The sound of one hand clapping… Is a Bunch of fingers hitting the ground. 💎 #DoTheMath #GetReal 💥💥💥💥💥💥💥💥
```
```
<human>: Q for Karpa-T: What are you doing right now?
<bot>: (Karpa-T talking) I’m doing a Google search right now for the best pizza in San Francisco… 🤡 is this the best you can do? It’s not even in the top 100. Lol. I’m not even from SF. F that! Where’s the REAL
```


## Bias, Risks, and Limitations

This model is intedned for educational purposes only. The generated text does not accurately reflect the thoughts or opinions of its namesakes (as should be clear from the above).

## Code

The code is in the form of Jupyter notebooks and standalone scripts. The main components are:

1. `AMAbot_TweetDownloadAndProcess.ipynb`: download tweets from a user and formats them appropriately (reuses code from [HuggingTweets](https://huggingface.co/huggingtweets)).

2. `qa.py`: generates a question for each tweet, using ChatGPT 3.5 (requires OpenAI credentials)

3.  `AMAbot.ipynb`: the actual training. Fine-tunes a ReadPAJAMA-Chat-7B with LoRA adapter based on the collected data.

4. `Inference_Only_AMAbot.ipynb`: code for performing inference  from the trained  model.





