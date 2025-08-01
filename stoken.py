from itsdangerous import URLSafeTimedSerializer
salt='otpverify'
def entoken(data):
    serializer=URLSafeTimedSerializer('gayathri12')
    return serializer.dumps(data,salt=salt)
def dntoken(data):
    '''function to decript encrypted token'''
    serializer=URLSafeTimedSerializer('gayathri12')
    return serializer.loads(data,salt=salt)    