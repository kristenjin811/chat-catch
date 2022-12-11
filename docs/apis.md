# API

This is the documentation for the API of Chat Catch.

# Login

POST /login

## Request
```json
{
  "username": "johnsmith",
  "password": "mypassword"
}
```
## Response

Success
```json

{
  "status": "success",
  "access_token": "example"
}
```
 Failure
```json
{
  "status": "failure",
  "message": "Invalid username or password"
}
```
# Logout
DELETE /logout

## Request
```json
{
  "access_token": "example"
}
```
## Response

## Success
```json
{
  "status": "success"
}
```

## Failure
```json
{
  "status": "failure",
  "message": "Invalid access token"
}
```
# Signup

POST /signup

## Request
```json
{
  "username": "johnsmith",
  "password": "mypassword"
}
```
## Response

Success
```json
{
  "status": "success"
}
```
Failure
```json
{
  "status": "failure",
  "message": "Username already exists"
}
```

# Send message

POST /messages

## Request
```json
{
  "access_token": "example",
  "chatroom_id": 1,
  "text": "Hello, world!"
}
```
## Response
Success
```json
{
  "status": "success"
}
```
Failure
```json
{
  "status": "failure",
  "message": "Invalid access token"
}
```

# Create Chatroom

POST /chatrooms

## Request
```json
{
  "name": "string"
}
```
## Response
Success
```json
{
  "status": "boolean",
  "message": "string"
}
```
Failure
```json
{
  "status": "failure",
  "message": "Chatroom already exists"
}
```

# Get chatroom

GET /chatroom/id

## Request
```json
{
  "name": "string",
  "member_names": "string",

}
```
## Response
Success
```json
{
  "status": "boolean",
  "message": "string"
}
```
Failure
```json
{
  "status": "failure",
  "message": "Invalid Chatroom"
}
```


# Get all chatrooms

GET /chatrooms

## Request
```json
{
  "name": "string",
  "member_count" : "string"
}
```
## Response
Success
```json
{
  "status": "boolean",
  "message": "string"
}
```
Failure
```json
{
  "status": "failure",
  "message": "Invalid Chatrooms"
}
```