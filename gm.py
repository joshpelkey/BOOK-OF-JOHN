# Import the necessary package
import random
import psutil
import time
import datetime
import openai
import math
from slack_sdk.webhook import WebhookClient

# Authenticate with OpenAI using your API key
openai.api_key = "YOUR_KEY_HERE"

# Create a Slack client
client = WebhookClient("YOUR_URL_HERE")

# get some cpu stats
memory_percent = psutil.virtual_memory().percent
cpu_percent = psutil.cpu_percent(interval=2)

uptime = time.time() - psutil.boot_time()
uptime_days = math.floor(uptime // (24 * 3600))
uptime = uptime % (24 * 3600)
uptime_hours = math.floor(uptime // 3600)
uptime %= 3600
uptime_minutes = math.floor(uptime // 60)
uptime %= 60
uptime_seconds = math.floor(uptime)

disk_usage = psutil.disk_usage("/")

# let's do something different each day of the week
day = datetime.datetime.now().weekday()

if day == 0:
    # today is monday 
    # monday's are hard. work hard. let's start with something motivating
    quote = "Share a motivational quote and attribute its author."
    question = "Tell me an uplifting story about success that is non-fiction. Use 250 words or less."

    # Ask ChatGPT your question
    quote_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=quote,
        temperature=0.5,
        max_tokens=1024
    )


    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024
    )

elif day == 1:
    # today is tuesday
    # tuesday's are for getting shit done. more to come...
    quote = "Share a quote about hard work and attribute its author."
    question = "Tell me in 250 words about a person who has contributed greatly to society. What were their works? Use 250 words or less."

    # Ask ChatGPT your question
    quote_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=quote,
        temperature=0.5,
        max_tokens=1024
    )


    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024
    )
elif day == 2:
    # today is wednesday
    # wednesday's are also hard. perservere.
    quote = "Share a quote about perserverance and attribute its author."
    question = "Tell me about a complex topic but explain it in simple terms."

    # Ask ChatGPT your question
    quote_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=quote,
        temperature=0.5,
        max_tokens=1024
    )


    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024
    )
elif day == 3:
    # today is thursday
    # on thursday, there is light
    quote = "Share a inspirational quote and attribute its author."
    question = "Give me some good advice on raising a son, as a father. Use 250 words or less."

    # Ask ChatGPT your question
    quote_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=quote,
        temperature=0.5,
        max_tokens=1024
    )


    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024
    )
elif day == 4:
    # today is friday
    # friday funday
    quote = "Share a quote about enjoying life and attribute its author."
    question = "Tell me a neat fact about something in the music industry. Use 250 words or less."

    # Ask ChatGPT your question
    quote_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=quote,
        temperature=0.5,
        max_tokens=1024
    )


    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024
    )
elif day == 5:
    # today is saturday 
    # saturdays are boss
    quote = "Share a quote about leadership and attribute its author."
    question = "Tell me about an interesting but lesser-known hobby or sport in 250 words or less."

    # Ask ChatGPT your question
    quote_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=quote,
        temperature=0.5,
        max_tokens=1024
    )


    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024
    )
elif day == 6:
    # today is sunday 
    # sundays are for rest and reset
    quote = "Share a quote about love and attribute its author."
    question = "Give me some life advice, in particular about raising daughters."

    # Ask ChatGPT your question
    quote_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=quote,
        temperature=0.5,
        max_tokens=1024
    )


    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        temperature=0.5,
        max_tokens=1024
    )
else:
    quote_response = 'error yo'
    question_response = 'error yo'


# Send the response to the incoming Slack webhook
slack_response = client.send(
    text="good morning mr. pelkey...",
    blocks=[
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":robot_face: :game_die:  Good Morning Mr. Pelkey  :game_die: :robot_face:"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": quote_response["choices"][0]["text"]
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
                "text": question_response["choices"][0]["text"]
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "context",
            "elements": [
                {
                    "text": "_I have been alive for " + str(uptime_days) + " days, " \
                            + str(uptime_hours) + " hours, " + str(uptime_minutes) \
                            + " minutes, and " + str(uptime_seconds) + " seconds || " \
                            + str(cpu_percent) + "% cpu || " \
                            + str(memory_percent) + "% ram || " \
                            + str(disk_usage.percent) + "% disk_",
                    "type": "mrkdwn"
                }
            ]
        }
    ]
)
