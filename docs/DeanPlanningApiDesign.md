### Log in

* Endpoint path: /login
* Endpoint method: POST

* Request shape (form):
  * username: string
  * password: string

* Response: Account information and a token
* Response shape (JSON):
    ```json
    {
      "account": {
        «key»: type»,
      },
      "token": string
    }
    ```



### User Story:
As a chat-catch customer
I want to be able to log in
So that I know my information and conversations are safe


### Issue:
Being able to log in

### Log out

* Endpoint path: /logout
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):
    ```json
    true
    ```


### User Story:
As a chat-catch customer
I want to be able to log out
So that I know my information and conversations are safe


###
Being able to log out

### Sign up

* Endpoint path: /sign_up
* Endpoint method: POST
* Query parameters:
  * «name»: «purpose»

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    {
        "username": string,
        "password": string
    }
    ```

* Response: An indication of success or failure
* Response shape (JSON):
    ```json
    {
        "success": boolean,
        "message": string
    }
    ```

### User Story:
As a chat-catch customer
I want users to have to sign-up / have accounts
So that random users are not allowed to break any terms of service (harassment/bulling)

### Issue
Being able to Sign up

### List of Chatrooms

* Endpoint path: /list_chatroom_members
* Endpoint method: GET
* Query parameters:
  * «name»: «purpose»

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    {
      "chatroom_id": number,
    }

    ```

* Response: A list of chat room members
* Response shape (JSON):
    ```json
    {
        "members": string,
        "members_id": number,
        "chatroom_id": number,
    }
    ```

### User Story:
As a chat-catch customer
I want to be able to see all the chat room members
So that I can connect with them / or reach out to them separately / read bio

### Issue:
Being able to get all users in a chat room
