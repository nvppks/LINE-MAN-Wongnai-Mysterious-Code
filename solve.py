import base64

secret= 'aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K'
decode_secret = base64.b64decode(secret).decode()
reverse = decode_secret[::-1]
print(reverse)
