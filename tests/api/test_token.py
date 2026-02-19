def test_token_exists(token):
    assert token is not None
    assert isinstance(token, str)
    assert len(token) > 10
