"""
This file is just for testing. It will not be executed in the package use.
"""

from dotenv import load_dotenv

load_dotenv()

import os
from . import ChatwootClient

chatwoot = ChatwootClient(os.getenv("CHATWOOT_URL"), os.getenv("CHATWOOT_USER_TOKEN"))

response = chatwoot.agents.list(account_id=os.getenv("CHATWOOT_ACCOUNT_ID"))

print(response)
