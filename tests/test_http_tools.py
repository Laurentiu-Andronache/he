import pytest

from he.http_tools import random_headers, get_json_parsed_from


def test_random_headers():
    # GIVEN 10 headers in which the User Agent should have been randomly generated
    headers = [random_headers() for _ in range(10)]

    # WHEN extracting all user agents and creating a set (therefore removing duplicates)
    user_agents = {item['User-Agent'] for item in headers}

    # THEN there should be at least 2 different user agents
    assert len(user_agents) > 1

    # OTHER
    assert 'Accept' in headers[0]


@pytest.mark.slow
def test_get_json_parsed_from():
    # If fail, getting moderated subreddits from Reddit is not possible anymore with this method.
    assert {'data', 'kind'} == set(
        get_json_parsed_from(
            b'https://www.reddit.com/user/alpha/moderated_subreddits.json'
        )
    )

    # Not interrupting __main__ processing for any error...
    assert {} == get_json_parsed_from('http://motherfuckingwebsite.com')
    assert {} == get_json_parsed_from('')
