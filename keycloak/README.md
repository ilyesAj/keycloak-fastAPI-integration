# keycloak setup

Run keycloak using either docker-compose or docker:

```bash
docker run -p 8080:8080 -v ./keycloak_data:/opt/keycloak/data/h2 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:22.0.3 start-dev
```

You can also use your own instance of keycloak and just import the test realm using `roc.json`