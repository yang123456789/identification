# ID
identify = {
    'url': 'http://apis.juhe.cn/idcard/index',
    'format': 'json',
    'key': 'JH343d7b591c6a0d0b12a09b191a6f65d8',
    'area': ['11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36',
             '37', '41', '42', '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62',
             '63', '64', '65', '71', '81', '82', '91']
}

# mysql
mysql = {
    'user': 'yang',
    'password': 'SYHXsqq@1233',
    'host': '123.58.244.172',
    'port': 3306,
    'db': 'identify'
}

# rsa
KEY = {
    'public': """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDp0Vu1+AX9Fmn6klmOimmI6RPm
KbRfcbFwgpdKk+DkN8EeeYKzq15bS+0dsT/PixgxYT0nYbUq9UNbe8dNbXiikN87
h3WXKnNSMQ1stbmjL5w7T5kRPejHFecNZ+hn1/H5P+Tp3RgpwSB8kIgmsYblF5aQ
M6oKZnZSW7qsICrokQIDAQAB
-----END PUBLIC KEY-----""",
    'private': """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDp0Vu1+AX9Fmn6klmOimmI6RPmKbRfcbFwgpdKk+DkN8EeeYKz
q15bS+0dsT/PixgxYT0nYbUq9UNbe8dNbXiikN87h3WXKnNSMQ1stbmjL5w7T5kR
PejHFecNZ+hn1/H5P+Tp3RgpwSB8kIgmsYblF5aQM6oKZnZSW7qsICrokQIDAQAB
AoGAJDvZZn2lD+9lRPtg/YHdkOXtu4FC/ndz8+eI4nnAJB2vw7U41/b6jFNbz3ok
VVlMynozK+MsXBfd9FNeM1V/mAXMtuR6HsF8GAdC/YrcOh2Z6cg9QJkkLP3d765r
N35pmYkGtHIqWg/6uKImsdHd7CRCjuVcBdVLuXrTVoaaLUECQQDqMUI6O/Jq/Qy6
KkYdPRbwRTrcSvAooQnK22swzjZMqOuSD6of4TPp6xgUCb8tv0jR2kK8icpgwQno
9t9HHDw1AkEA/5crYfhTsWANHkj3Qtb3E/vEzq3LBGwvYMATO8Sk2WYXy9+Y2SyR
wuwtNghWKImm57JXjNTAPbqOj0c+ofzubQJBANwvPfYkgJJoonux3UQGOLfkTyfp
aQy6A8vvKkOzzceblgg4pBnfEYEfoP7N/yoSy3NKQy6iWl1HgXrACUMBX/UCQQDu
IGaP4XAASxANzkdoY6VRXflv4eXLGgxOJMYGomBAF+lFze23MNog9C/vLncvT4hM
SBFfqXvuRxi5DtSg0WlFAkBRCVtGYKKrtJ27t5hThg9ueX8H96Sw3L+qkj4yrSQk
fXFhoDL6OMJbshY4jQwtQS6HrsmkzAlJyq7gmVSqeZEf
-----END RSA PRIVATE KEY-----"""
}

# juhe
CARD = {
    'key': '3717556d5319562f74671847738e703e',
    'info_url': 'http://apis.juhe.cn/idcard/index',
    'leak_url': 'http://apis.juhe.cn/idcard/leak',
    'loss_url': 'http://apis.juhe.cn/idcard/loss'
}
