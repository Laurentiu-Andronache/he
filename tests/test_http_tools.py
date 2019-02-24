import pytest

from he.http_tools import get_json_parsed_from


@pytest.mark.slow
def test_get_json_parsed_from():
    # If fail, getting moderated subreddits from Reddit is not possible anymore with this method.
    assert {'data', 'kind'} == set(
        get_json_parsed_from(
            'https://www.reddit.com/user/alpha/moderated_subreddits.json'
        )
    )

    # Not interrupting __main__ processing for any error...
    assert '' == get_json_parsed_from('http://motherfuckingwebsite.com')
    assert '' == get_json_parsed_from('')
