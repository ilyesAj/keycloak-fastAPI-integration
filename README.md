# keycloak-fastAPI-integration

This repository illustrates how we can integrate keycloak with fastAPI for authetification.
This repo can be used as a template/code base for your app . 


## setup env

I used `pipenv` for my env setup.

1. install `pipenv`
2. install dependencies using `pipenv install`
3. run keycloak instance using:

```bash
docker run -p 8080:8080 -v ./keycloak/keycloak_data:/opt/keycloak/data/h2 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:22.0.3 start-dev
```

4. now you can run your fastAPI app using `pipenv run python main.py`

## Demo

1. access to fastAPI swagger using http://127.0.0.1:8081/docs
2. get token using authorize
3. make your query for `/secure`
![demo](https://github.com/ilyesAj/keycloak-fastAPI-integration/blob/main/images/fastapi.gif)

