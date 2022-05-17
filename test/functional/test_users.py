def test_new_users(new_user):
    assert new_user.username == 'winson'
    assert new_user.email == 'winsonma@sjsu.edu'
    assert new_user.password == 'winson'
