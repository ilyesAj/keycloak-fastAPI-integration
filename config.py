#/config.py
from models import authConfiguration


settings = authConfiguration(
    server_url="http://localhost:8080/",
    realm="roc",
    client_id="rns:roc:portal",
    client_secret="",
    authorization_url="http://localhost:8080/realms/roc/protocol/openid-connect/auth",
    token_url="http://localhost:8080/realms/roc/protocol/openid-connect/token",
)
