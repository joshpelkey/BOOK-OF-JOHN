# Import the necessary package
import random
import psutil
import time
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

# get a random number
random_num = random.randint(5,1000)

# craft a prompt with some placeholder
placeholder = "Find something cool that happened xxx years ago. Tell me about it in 100 words or less and then give me a thought provoking question at the end."
prompt_text = placeholder.replace("xxx", str(random_num))


# Ask ChatGPT your question
chat_response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt_text,
    temperature=0.5,
    max_tokens=1024
)

# Send the response to the incoming Slack webhook
slack_response = client.send(
    text="fallback",
    blocks=[
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":robot_face: :computer: :game_die:  Good Morning Mr. Pelkey  :game_die: :computer: :robot_face:"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "text": "_On this day " + str(random_num) + " years ago..._",
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
            "type": "divider"
        },
        {
            "type": "context",
            "elements": [
                {
                    "text": "_I have been alive for " + str(uptime_days) + " days, " \
                            + str(uptime_hours) + " hours, " + str(uptime_minutes) \
                            + " minutes, and " + str(uptime_seconds) + " seconds || " \
                            + str(cpu_percent) + "% cpu in use || " \
                            + str(memory_percent) + "% ram in use_",
                    "type": "mrkdwn"
                }
            ]
        }
    ]
)
