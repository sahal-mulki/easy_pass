from easy_pass import easy_pass

def test_haversine():
    assert easy_pass.Password(password="password").hash == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
