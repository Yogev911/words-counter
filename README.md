# Words counter service - Lemonade

A REST API for retrieve textual data, parse it, and count words in it.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
1. git
2. docker

## Service Deployment
```
git clone https://github.com/Yogev911/words-counter.git

cd words-counter

mkdir data

bash main.sh
```

####clarifications:
This service runs a REDIS server and maps his volumes to /data folder

## Swagger-ui deployment
SMS-SERVICE is using swagger API documentation
to reveal the API docs there's a need to use a swagger-ui

```
docker pull swaggerapi/swagger-ui

docker run -p 80:8080 swaggerapi/swagger-ui

open http://localhost
```
for more info `https://hub.docker.com/r/swaggerapi/swagger-ui/` and `https://swagger.io/tools/swagger-ui/`

## How it works
basic flow:

1. insert new words from string in body
`curl -X POST "http://localhost:5000/words" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"data\": \"Testing the input here\"}"`

2. insert new words from url in body
`curl -X POST "http://localhost:5000/words" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"data\": \"http:localhost:8081/getwords\"}"`

3. insert new words from path in body
`curl -X POST "http://localhost:5000/words" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"data\": \"/Users/yogevheskia/projects/words-counter/README.md\"}"`

4. query for word in DB
`curl -X POST "http://localhost:5000/statistics" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"word\": \"Yogev\"}"`


## Tests
Utils component has an `test.py` file that contains unittests for the component

## Exceptions
This project contains a `exception.py` file that defines app custom exceptions

## Built With
* **Flask Framework**
* **unittest**
* **REDIS DB**

## Author

* **Yogev Heskia**  [GitHub](https://github.com/yogev911) [LinkedIn](https://www.linkedin.com/in/yogevh/)

## License

This project is licensed under the MIT License
