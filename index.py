import asyncio
import requests
import json

# from luno_python.client import Client

auth = {
    "api_key_id": "h6s5ne73nfy3w",
    "api_key_secret": "Wr6jiU_YTxupB8JSjjN30_Sc9JZg2m-N_mvCmpja32Q"
}

# Fetching your accounts
balance = requests.get('https://api.mybitx.com/api/1/balance', auth=(auth['api_key_id'], auth['api_key_secret']))

try:
  print(balance)
except RuntimeError:
  loop = None

