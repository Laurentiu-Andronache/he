"""Helpers related to HTTP/HTTPS."""

import logging
from importlib.resources import open_text
from random import choice
from typing import Dict, Any, Union

import requests

_LOGGER = logging.getLogger(__name__)

# user agents can be downloaded from https://techblog.willshouse.com/2012/01/03/most-common-user-agents/
DESKTOP_AGENTS = open_text('he.data', 'user_agents.txt').readlines()


def random_headers() -> Dict[str, str]:
    """Returns headers dict for use when making requests to web servers,
    in order to simulate a browser more realistically.
    The user agent is random."""
    return {
        'User-Agent': choice(DESKTOP_AGENTS).strip(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }


def get_json_parsed_from(url: Union[str, bytes]) -> Dict[Any, Any]:
    """Gets a JSON file and returns it parsed, or returns an empty dict if any error occurred."""
    try:
        headers = random_headers()
        headers['Accept'] = 'application/json,text/*;q=0.99'
        result = requests.get(url, headers=headers).json()
        if isinstance(result, dict):
            return result
    except BaseException:
        _LOGGER.exception('Failed getting JSON from %s', repr(url), exc_info=False)

    return {}
