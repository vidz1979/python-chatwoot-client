import re
from typing import Any, Optional, Union, Type
from dataclasses import dataclass
from chatwoot_client.http import HttpClient
from chatwoot_client.definitions.actions import *


class Actions:
    client: HttpClient

    def __init__(self, client: HttpClient):
        self.client = client

    def __getitem__(self, item):
        return getattr(self, item)


@dataclass
class Action(Actions):
    method: str
    url: str
    query: Optional[Union[Type, Any]] = None
    schema_: Optional[Union[Type, Any]] = None


def action_factory(client: HttpClient, method: str, url: str, query=None, schema_=None) -> Action:
    """Factory function to create a default Action instance."""
    print(f"method: {method}, url: {url}, query: {query}, schema_: {schema_}")

    def run_action(**kwargs):
        try:
            fmt_url = url.format(**kwargs)
        except KeyError:
            url_params = re.findall("{(.*?)}", url)
            provided_params = list(kwargs.keys())
            raise ValueError(f"{method} {url} needs parameters: {url_params}, but where provided: {provided_params}")
        print(fmt_url)

    return run_action
    # return Action(method=method, url=url, query=query, schema_=schema_)
