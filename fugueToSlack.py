from __future__ import print_function

import boto3
import json
import logging
import os
import requests

from base64 import b64decode
#from urllib2 import Request, urlopen, URLError, HTTPError


# The base-64 encoded, encrypted key (CiphertextBlob) stored in the kmsEncryptedHookUrl environment variable
ENCRYPTED_HOOK_URL = os.environ['kmsEncryptedHookUrl']
# The Slack channel to send a message to stored in the slackChannel environment variable
SLACK_CHANNEL = os.environ['slackChannel']

#HOOK_URL = "https://" + boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED_HOOK_URL))['Plaintext']
#HOOK_URL = "https://hooks.slack.com/services/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"
logger = logging.getLogger()
logger.setLevel(logging.INFO)

print('Loading function')

def lambda_handler(event, context):
    
    event_cond = 'default'
    sns = event['Records'][0]['Sns']
    #print('DEBUG:', sns['Message'])
    #json_msg = json.loads(sns['Message'])

    if sns['Subject']:
        message = sns['Subject']
    else:
        message = sns['Message']
    
    region = sns['TopicArn'].split(':')[3]
    topic_name = sns['TopicArn'].split(':')[-1]
    HOOK_URL = "https://" + boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED_HOOK_URL))['Plaintext']

    message = event['Records'][0]['Sns']['Message']

    payload = {
    'text': message,
    'channel': '#fugue-updates',
    'username': 'AWS Lambda',
    'icon_emoji': ':thumbs-up'
    }
    r = requests.post(HOOK_URL, json=payload)
    return r.status_code


# def lambda_handler(event, context):
#     print("Received event: " + json.dumps(event, indent=2))
#     message = event['Records'][0]['Sns']['Message']
#     print("From SNS: " + message)
#     return message