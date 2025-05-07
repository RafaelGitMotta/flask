# Esse arquivo serve somente para gerar chaves aletórias no terminal para ser usada como uma SECRET KEY
import secrets

sk = secrets.token_hex(24)

print(sk)