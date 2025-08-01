import random
def genotp():
    otp=''
    u_l=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    s_l=[chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(2):
        otp=otp+random.choice(u_l) #otp=''+'A' --'A',otp='Ak9'+'M'
        otp=otp+random.choice(s_l) #otp='A'+'k' --'Ak',otp='Ak9M'+'u'
        otp=otp+str(random.randint(0,9)) #otp='Ak'+'9' --'Ak9',otp='Ak9Mu'+8 --
    return otp #'Ak9Mu8'  