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
client = WebhookClient(
    "YOUR_URL_HERE"
)

# ChatGPT temp
temp = 0.9

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

# some topics to choose from for topline quote
quote_topics = [
    "motivation",
    "leadership",
    "parenthood",
    "perserverance",
    "curiousity",
    "love",
    "life",
    "relationships",
    "family",
    "happiness",
    "friendship",
    "success",
    "courage",
    "inspiration",
    "happiness",
    "gratitude",
    "hope",
    "change",
    "beauty",
    "resilience",
    "kindness",
]

# pick a random quote topic
quote_topic = random.choice(quote_topics)
quote = "Share a random quote about " + quote_topic + " and attribute its author"
quote_response = openai.Completion.create(
    engine="text-davinci-002", prompt=quote, temperature=temp, max_tokens=1024
)

# List of topics for daily
topics = [
    "Artificial intelligence",
    "Robotics",
    "Quantum computing",
    "Biotechnology",
    "Nanotechnology",
    "Genetics",
    "Data science",
    "Machine learning",
    "Energy technology",
    "Space exploration",
    "Solar power",
    "Renewable energy",
    "Environmental science",
    "Climate change",
    "Agriculture technology",
    "Medical technology",
    "Health informatics",
    "Drug discovery and development",
    "Neuroscience",
    "Cancer research",
    "Psychology",
    "Geology",
    "Meteorology",
    "Astronomy",
    "Astrophysics",
    "Particle physics",
    "Atomic physics",
    "Chemistry",
    "Materials science",
    "Geochemistry",
    "Oceanography",
    "Environmental engineering",
    "Electrical engineering",
    "Mechanical engineering",
    "Computer science",
    "Cybersecurity",
    "Internet of Things",
    "Blockchain technology",
    "Virtual reality",
    "Augmented reality",
    "3D printing",
    "Transportation technology",
    "Telecommunication",
    "Drones",
    "Television and video technology",
    "Music technology",
    "Video game technology",
    "Film and movie technology",
    "Photography technology",
    "Design and architecture technology",
]


# let's do something different each day of the week
day = datetime.datetime.now().weekday()

if day == 0:
    # monday's are hard
    # let's start the week with an important topic -- parenthood
    question = "provide some reflective thoughts on parenthood or fatherhood and connect it to a human emotion, picked at random. Use around 250 words."
    poem = "create a haiku about parenthood"

    # Ask ChatGPT your question
    poem_response = openai.Completion.create(
        engine="text-davinci-002", prompt=poem, temperature=temp, max_tokens=1024
    )

    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002", prompt=question, temperature=temp, max_tokens=1024
    )

    elif day == 1:
    # tuesday's are for getting shit done
    # let's learn about science and tech
    science_topic = random.choice(topics)
    question = (
        "pick a complex topic from the area of "
        + science_topic
        + " and tell me about it in 250 words."
    )
    poem = (
        "create a haiku about science and technology, particularly in the area of "
        + science_topic
    )

    # Ask ChatGPT your question
    poem_response = openai.Completion.create(
        engine="text-davinci-002", prompt=poem, temperature=temp, max_tokens=1024
    )

    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002", prompt=question, temperature=temp, max_tokens=1024
    )
elif day == 2:
    # wednesday's ... keep going baby
    # how about we do a little money talk
    question = "tell me about a random topic on finance and connect to a historical event. Use around 250 words."
    poem = "create a haiku about money"

    # Ask ChatGPT your question
    poem_response = openai.Completion.create(
        engine="text-davinci-002", prompt=poem, temperature=temp, max_tokens=1024
    )

    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002", prompt=question, temperature=temp, max_tokens=1024
    )
elif day == 3:
    # thursday's we see the light
    # let's get some fun stuff going
    question = "pick a random book chapter from The Wheel of Time series and give me a summary. Tell me the book and chapter you have picked. Use around 250 words."
    poem = "create a haiku about fantasy or sci-fi"

    # Ask ChatGPT your question
    poem_response = openai.Completion.create(
        engine="text-davinci-002", prompt=poem, temperature=temp, max_tokens=1024
    )

    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002", prompt=question, temperature=temp, max_tokens=1024
    )
elif day == 4:
    # friday baby
    # let's talk music
    question = "pick a random topic from the area of music. it can be music theory, a song, an artist, a concert -- really anything related to music. Give me a summary about the topic in around 250 words."
    poem = "create a haiku poem about music"

    # Ask ChatGPT your question
    poem_response = openai.Completion.create(
        engine="text-davinci-002", prompt=poem, temperature=temp, max_tokens=1024
    )

    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002", prompt=question, temperature=temp, max_tokens=1024
    )
elif day == 5:
    # saturday -- FOOTBAWW
    question = "pick 5 random stats about college football and tell me about them. Use around 250 words."
    poem = "create a haiku about clemson university"

    # Ask ChatGPT your question
    poem_response = openai.Completion.create(
        engine="text-davinci-002", prompt=poem, temperature=temp, max_tokens=1024
    )

    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002", prompt=question, temperature=temp, max_tokens=1024
    )
elif day == 6:
    # sunday -- a day of rest
    question = "Give me a bulleted summary of a book from the christian bible. Use around 250 words."
    poem = "create a haiku about religon"

    # Ask ChatGPT your question
    poem_response = openai.Completion.create(
        engine="text-davinci-002", prompt=poem, temperature=temp, max_tokens=1024
    )

    # Ask ChatGPT your question
    question_response = openai.Completion.create(
        engine="text-davinci-002", prompt=question, temperature=temp, max_tokens=1024
    )
else:
    poem_response = "error yo"
    question_response = "error yo"

# Send the response to the incoming Slack webhook
slack_response = client.send(
    text="good morning mr. pelkey...",
    blocks=[
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":robot_face: :game_die:  Good Morning Mr. Pelkey  :game_die: :robot_face:",
            },
        },
        {
            "type": "context",
            "elements": [
                {"type": "mrkdwn", "text": quote_response["choices"][0]["text"]}
            ],
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": question_response["choices"][0]["text"]},
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {"text": poem_response["choices"][0]["text"], "type": "mrkdwn"}
            ],
        },
        {"type": "divider"},
        {
            "type": "context",
            "elements": [
                {
                    "text": "_I have been alive for "
                    + str(uptime_days)
                    + " days, "
                    + str(uptime_hours)
                    + " hours, "
                    + str(uptime_minutes)
                    + " minutes, and "
                    + str(uptime_seconds)
                    + " seconds || "
                    + str(cpu_percent)
                    + "% cpu || "
                    + str(memory_percent)
                    + "% ram || "
                    + str(disk_usage.percent)
                    + "% disk_",
                    "type": "mrkdwn",
                }
            ],
        },
    ],
)    
