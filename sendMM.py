import requests
import json
import settings

def post_to_mattermost(url, message):
    # Send payload as HTTP Post Request to Webhook URL
    r = requests.post(
        url,
        data=message
    )
    r.raise_for_status()

if __name__=="__main__":
    url = settings.MM_hook_url
    messages = [
        {
            'channel' : settings.MM_channel,
            'text'    : '한국어 채팅 테스트'
        }
    ]
    for message in messages:
        post_to_mattermost(url, json.dumps(message))