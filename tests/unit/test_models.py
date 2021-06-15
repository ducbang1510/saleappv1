from saleapp.models import *


def test_new_user():
    user = User('Duc Bang', 'abc@gmail.com', 'bang123', '12345')
    assert user.name == 'Duc Bang'
    assert user.email == 'abc@gmail.com'
    assert user.username == 'bang123'
    assert user.password != '12345'
    assert user.user_role == UserRole.USER


def test_new_user_with_fixture(new_user):
    assert new_user.name == 'Duc Bang'
    assert new_user.email == 'abc@gmail.com'
    assert new_user.username == 'bang123'
    assert new_user.password != '12345'
    assert new_user.user_role == UserRole.USER