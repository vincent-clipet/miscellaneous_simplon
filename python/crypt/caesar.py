#############
# FUNCTIONS #
#############

def crypt(message: str, shift: int) -> str :
    a = [*message]
    ret = []
    for char in a:
        ret.append(chr(ord(char)+shift))
    return "".join(ret)

def decrypt(message: str, shift: int) -> str:
    return crypt(message, shift*-1)

def test_shift(message, shift):
    tmp = ""
    for i in message:
        tmp += chr(i+shift)
    return tmp



#######
# RUN #
#######

test = "ABCDE"
crypted = crypt(test, 8)
print(test, " => ", crypted)
decrypted = decrypt(test, 8)
print(crypted, " => ", decrypted)


print("=================================================")


mystery = ']\x8a\x89\x85\x8a\x90\x8d;\x88\x80\x8e;\x8f\x8dă\x8e;~\x83\x80\x8d\x8e;|\x8b\x8b\x8d\x80\x89|\x89\x8f\x8eI;aĄ\x87\x84~\x84\x8f|\x8f\x84\x8a\x89\x8e;û;\x91\x8a\x90\x8eG;\x91\x8a\x90\x8e;|\x91\x80\x95;\x8dĄ\x90\x8e\x8e\x84;û;~|\x8e\x8e\x80\x8d;~\x80;~\x8a\x7f\x80;<;e\x80;\x8e\x90\x84\x8e;\x81\x84\x80\x8d;\x7f\x80;\x91\x8a\x90\x8eI;h|\x84\x89\x8f\x80\x89|\x89\x8fG;\x91\x8a\x90\x8e;\x8b\x8a\x90\x91\x80\x95;~\x8a\x88\x88\x80\x89~\x80\x8d;\x87\x80;~\x8a\x7f\x80;\x7f\x80;q\x84\x82\x80\x89ă\x8d\x80'
# print("mystery : ", mystery)
a = [ord(c) for c in [*mystery]]

for i in range(1, 40):
    tmp = test_shift(a, -i)
    print("", i, " => ", tmp)
    input()
