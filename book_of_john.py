import random
import openai
from slack_sdk.webhook import WebhookClient
import requests
import subprocess
from urlextract import URLExtract


# Authenticate with OpenAI using your API key
openai.api_key = "YOUR_KEY_HERE"

# Create a Slack client

#ai_stories
client = WebhookClient("YOUR_HOOK_HERE")

# variables for our book
book_title = "Book of John"
emotions = ["Love", "Joy", "Anger",
            "Sadness", "Fear", "Surprise",
            "Disgust", "Envy", "Hope", "Hurt",
            "Shame", "Guilt", "Pride", "Desire",
            "Nostalgia", "Excitement", "Loneliness",
            "Jealousy", "Contentment", "Satisfaction"]
favorite_things = ["drinking whiskey",
                    "playing golf",
                    "gambling",
                    "watching sports",
                    "playing blackjack",
                    "throwing dice",
                    "delivering packages",
                    "making cocktails",
                    "drinking beers",
                    "enjoying craft beer",
                    "crypto",
                    "shitcoins",
                    "telling long stories",
                    "gaming the stock market",
                    "playing old nintendo games",
                    "jumping on the trampoline",
                    "being shirtless",
                    "smoking weed",
                    "slaying a beast"]

# some safer searches for DALL-E, who seems to be picky
favorite_things_safe = ["drinking",
                    "playing golf",
                    "sitting at a card table",
                    "watching sports",
                    "playing cards",
                    "throwing dice",
                    "delivering packages",
                    "making drinks",
                    "drinking",
                    "drinking at a bar",
                    "crypto",
                    "penny stocks",
                    "telling long stories",
                    "gaming the stock market",
                    "playing old nintendo games",
                    "jumping on the trampoline",
                    "being shirtless",
                    "smoking",
                    "hunting"]

# pick a randoms
theme = random.choice(emotions)
favorite_thing_number = random.randint(0,18)  # i store this to use as the book chapter number in the output
favorite_thing = favorite_things[favorite_thing_number]
favorite_thing_safe = favorite_things_safe[favorite_thing_number]
number_verses = 3
starting_verse_number = random.randint(1, 997)


#sent your prompt with all variables 
gpt_prompt = "Generate " + str(number_verses) + " numbered verses about " \
        + favorite_thing + ". Make the tone of the verses about " + theme + ". Use the word or phrase " + favorite_thing \
        + " in each verse. Don't use the word God or Lord. Start with verse number " \
        + str(starting_verse_number) + " and count up."

print(gpt_prompt)

# Ask ChatGPT your question
chat_response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=1024
)

# DALL-E prompt
dalle_prompt = "a neoclassical painting of " + favorite_thing_safe + " and " + theme

# generate a dope DALL-E image
dalle_response = openai.Image.create(
  prompt = dalle_prompt,
  size="256x256"
)
image_url = dalle_response['data'][0]['url']

# get the image and store it on imgur
img_data = requests.get(image_url).content
with open('book_of_john.jpg', 'wb') as handler:
    handler.write(img_data)

imgur = subprocess.run(['imgur-uploader', 'book_of_john.jpg'], stdout=subprocess.PIPE)

extractor = URLExtract()
imgur_str = str(imgur)
url = extractor.find_urls(imgur_str)

                "text": chat_response["choices"][0]["text"] 
            }
        },
        {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": "[" + theme + "]",
                "emoji": True# Import the necessary package
import random
import openai
from slack_sdk.webhook import WebhookClient
import requests
import subprocess
from urlextract import URLExtract


# Authenticate with OpenAI using your API key
openai.api_key = "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"

# Create a Slack client

#ai_stories
client = WebhookClient("https://hooks.slack.com/services/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")

# me
#client = WebhookClient("https://hooks.slack.com/services/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")

# variables for our book
book_title = "Book of John"
emotions = ["Love", "Joy", "Anger",
            "Sadness", "Fear", "Surprise",
            "Disgust", "Envy", "Hope", "Hurt",
            "Shame", "Guilt", "Pride", "Desire",
            "Nostalgia", "Excitement", "Loneliness",
            "Jealousy", "Contentment", "Satisfaction"]
favorite_things = ["drinking whiskey",
                    "playing golf",
                    "gambling",
                    "watching sports",
                    "playing blackjack",
                    "throwing dice",
                    "delivering packages",
                    "making cocktails",
                    "drinking beers",
                    "enjoying craft beer",
                    "crypto",
                    "shitcoins",
                    "telling long stories",
                    "gaming the stock market",
                    "playing old nintendo games",
                    "jumping on the trampoline",
                    "being shirtless",
                    "smoking weed",
                    "slaying a beast"]

# some safer searches for DALL-E, who seems to be picky
favorite_things_safe = ["drinking",
                    "playing golf",
                    "sitting at a card table",
                    "watching sports",
                    "playing cards",
                    "throwing dice",
                    "delivering packages",
                    "making drinks",
                    "drinking",
                    "drinking at a bar",
                    "crypto",
                    "penny stocks",
                    "telling long stories",
                    "gaming the stock market",
                    "playing old nintendo games",
                    "jumping on the trampoline",
                    "being shirtless",
                    "smoking",
                    "hunting"]

# pick a randoms
theme = random.choice(emotions)
favorite_thing_number = random.randint(0,18)  # i store this to use as the book chapter number in the output
favorite_thing = favorite_things[favorite_thing_number]
favorite_thing_safe = favorite_things_safe[favorite_thing_number]
number_verses = 3
starting_verse_number = random.randint(1, 997)


#sent your prompt with all variables 
gpt_prompt = "Generate " + str(number_verses) + " numbered verses about " \
        + favorite_thing + ". Make the tone of the verses about " + theme + ". Use the word or phrase " \
        + favorite_thing + " in each verse. Don't use the word God or Lord. Start with verse number " \
        + str(starting_verse_number) + " and count up."

print(gpt_prompt)

# Ask ChatGPT your question
chat_response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=1024
)

# DALL-E prompt
dalle_prompt = "a neoclassical painting of " + favorite_thing_safe + " and " + theme

# generate a dope DALL-E image
dalle_response = openai.Image.create(
  prompt = dalle_prompt,
  size="256x256"
)
image_url = dalle_response['data'][0]['url']

# get the image and store it on imgur
img_data = requests.get(image_url).content
with open('book_of_john.jpg', 'wb') as handler:
    handler.write(img_data)

imgur = subprocess.run(['imgur-uploader', 'book_of_john.jpg'], stdout=subprocess.PIPE)

extractor = URLExtract()
imgur_str = str(imgur)
url = extractor.find_urls(imgur_str)

                "text": chat_response["choices"][0]["text"] 
            }
        },
        {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": "[" + theme + "]",
                "emoji": True
            },
            "image_url": clean_url,
            "alt_text": "[ THE BOOK OF JOHN || " + theme + " ]"
        }
    ]
)

print(chat_response)
print(dalle_response)
print(slack_response)
clean_url = url[0][:-4]


# Send the response to the incoming Slack webhook
slack_response = client.send(
    text="fallback",
    blocks=[
        {
            "type": "header",
            "text": {
                "type": "plain_text",
            },
            "image_url": clean_url,
            "alt_text": "[ THE BOOK OF JOHN || " + theme + " ]"
        }
    ]
)

print(chat_response)
print(dalle_response)
print(slack_response)
clean_url = url[0][:-4]

# Send the response to the incoming Slack webhook
slack_response = client.send(
    text="fallback",
    blocks=[
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":game_die: :beer: :game_die:  The Book of John  :game_die: :beer: :game_die:"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "text": theme + " | _Chapter " + str(favorite_thing_number + 1) + " | Verses " + str(starting_verse_number) \
                                    + "-" + str(starting_verse_number + (number_verses-1)) + "_",
                    "type": "mrkdwn"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": chat_response["choices"][0]["text"]
            }
        },
        {
            "type": "image",
            "title": {
                "type": "plain_text",
                "text": "[" + theme + "]",
                "emoji": True
            },
            "image_url": clean_url,
            "alt_text": "[ THE BOOK OF JOHN || " + theme + " ]"
        }
    ]
)

print(chat_response)
print(dalle_response)
print(slack_response)
