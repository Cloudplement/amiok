import pytest

from amiok.app import get_status

def test_ok_get_status():
    resp = get_status("http://google.com")
    assert 'OK' in resp

def test_not_ok_get_status():
    resp = get_status("http://not-a-google-domain.go")
    assert 'Not OK' in resp
