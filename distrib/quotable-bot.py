from time import sleep
from slackclient import SlackClient
from quotes import quotes
from random import randint
from config import BOT_ID, BOT_TOKEN
import json


def get_quote():
    quote = quotes[randint(0, 10000) % len(quotes)]
    split_quote = quote.split(" - ")
    split_attribution = split_quote[1].split(",")
    person = split_attribution[0]
    quote = split_quote[0]
    attribution = ", ".join(split_quote[1:])
    return "The Quotable %s\n&gt;%s\n - %s" % (person, quote, attribution)


if __name__ == "__main__":
    slack_client = SlackClient(BOT_TOKEN)
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    while True:
        try:
            if slack_client.rtm_connect():
                print("quotable-bot connected and running!")
                while True:
                    output_list = slack_client.rtm_read()
                    if output_list and len(output_list) > 0:
                        for output in output_list:
                            if output and 'text' in output and "quotable" in output['text'].lower() and \
                                    ('bot_id' not in output or output['bot_id'] != BOT_ID):
                                print(json.dumps(output, indent=2))
                                slack_client.api_call("chat.postMessage", channel=output['channel'], text=get_quote(), as_user=True)
                    sleep(READ_WEBSOCKET_DELAY)
            else:
                print("Connection failed. Invalid Slack token or bot ID?")
        except Exception as e:
            print(e)
