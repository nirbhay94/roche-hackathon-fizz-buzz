# Roche hackathon FizzBuzz - Phase1

---
This repo implement a robust and production-ready Fizz-Buzz REST Server that follows the classic Fizz-Buzz logic. The server exposes a REST API endpoint, with an additional feature of a statistical endpoint.

This project is built using Python FastAPI framework
---

## Requirements

Python 3.8+

## Installation

You can install fastapi via pip command:

```pip install fastapi```

OR

```pip3 install fastapi```

For testing install

```pip install httpx```

AND

```pip3 install pytest```

## Run application

You can start the server with:

```uvicorn main:app --reload```

## API Documentation

```curl --location 'http://127.0.0.1:8000/?int1=3&int2=5&limit=25&str1=fizz&str2=buzz'```

http://127.0.0.1:8000/?int1=3&int2=5&limit=25&str1=fizz&str2=buzz

Response

```"1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,17,fizz,19,buzz,fizz,22,23,fizz,buzz"```

## Testing

To test run below command:
```pytest```

