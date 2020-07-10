import main
import pytest

def test_parse_nrao_bad_url():
    with pytest.raises(ValueError):
        assert main.parse_nrao("")

def mock_response_read_func(response):
    return None

def test_parse_nrao_no_data():
    with pytest.raises(ValueError):
        orig_func = main.response_read_func
        main.response_read_func = mock_response_read_func
        main.parse_nrao(main.nrao_url)
        main.response_read_func = orig_func