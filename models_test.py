import pytest
from app.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User('winson', 'winsonma@sjsu.edu', 'winson')
    return user

def test_user(user):
    assert user.username == 'winson'
    assert user.email == 'winsonma@sjsu.edu'
    assert user.password == 'winson'
