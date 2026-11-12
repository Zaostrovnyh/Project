import hmac
import hashlib

flag = True
def check_pickle_integrity(msg, key, original_sig):
    msg_bytes = msg.encode('utf-8')
    key_bytes = key.encode('utf-8')
    computed_sig = hmac.new(key_bytes, msg_bytes, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_sig, original_sig)
while True:
    if flag:
        with open("tet.txt", "r", encoding = "utf-8") as f:
            print("read")
            original_msg = f.read()

        flag = False
    my_key = "d16705f004604d0c5a4fce0180f50397417533af2dba788ae8f2b4bc25f2521f"
    with open("tet.txt", "r", encoding="utf-8") as f:
        new_msg = f.read()
    sig = hmac.new(my_key.encode(), original_msg.encode(), hashlib.sha256).hexdigest()
    if check_pickle_integrity(new_msg, my_key, sig) == False:
        print("Изменение конфигурационного файла!")
        flag = True