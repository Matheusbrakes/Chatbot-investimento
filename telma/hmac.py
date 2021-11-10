import random
import string
import hmac
import hashlib
letters = string.ascii_lowercase

key = "chaveSecreta"
message = input("Digite a mensagem a ser enviada: ")

########## 1 ##########
message_digest1 = hmac.digest(key=key.encode(), msg=message.encode(), digest="sha1")

envio = random.randint(0, 3)
if envio == 0:
    # Mensagem normal, key normal
    message = message
elif envio == 1:
    # Mensagem corrompida, key normal
    alM = ''.join(random.choice(letters) for i in range(5))
    message = message + alM
elif envio == 2:
    # Mensagem normal, key corrompida
    alK = ''.join(random.choice(letters) for i in range(5))
    key = key + alK
elif envio == 3:
    # Mensagem corrompida, key corrompida
    alM = ''.join(random.choice(letters) for i in range(5))
    message = message + alM
    alK = ''.join(random.choice(letters) for i in range(5))
    key = key + alK


print(f"\nA mensagem recebida foi: {message}\n")


########## 2 ##########
message_digest2 = hmac.digest(key=key.encode(), msg=bytes(message, encoding="utf-8"), digest=hashlib.sha1)


print("O hash da mensagem enviada é: {}".format(message_digest1))
print("O hash da mensagem recebida é: {}".format(message_digest2))
print("\nO hash da mensagem 1 é igual ao hash da mensagem 2: {}".format(hmac.compare_digest(message_digest1, message_digest2)))

if hmac.compare_digest(message_digest1, message_digest2) == True:
    print("Tudo certo!")
elif hmac.compare_digest(message_digest1, message_digest2) == False:
    print("Algo deu errado!")
