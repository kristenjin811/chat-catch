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

* Response: A list of chat room memebers
* Response shape (JSON):
    ```json
    {
        "members": string,
        "memebers_id": number,
        "chatroom_id": number,
    }
    ```
