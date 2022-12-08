## APIs

## EndPoints -
1. login - post
2. logout - delete
3. signup - post
4. list of chat room members - get
5. list of chat rooms - get
6. Show selected chatroom - get
7. send a message - post
8. delete a message - delete
9. edit a message - put
10. adding a member to a chatroom - put
11. accepting a membership for chatroom- put
12. deleting a member of a chatroom  - delete
13. declining a chatroom membership - delete
14. create a chatroom - post
15. delete a chatroom - delete
16. reactions - put

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

* Response: A list of chat room members
* Response shape (JSON):
    ```json
    {
        "members": string,
        "members_id": number,
        "chatroom_id": number,
    }
    ```


### List of chatrooms

* Endpoint path: /chatrooms
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A list of chatrooms
* Response shape:
    ```json
    {
      "chatrooms": [
        {
          "name": string,
          "member_count": int,
          "image_url": string,
        }
      ]
    }
    ```

### Show selected chatroom

* Endpoint path: /chatroom
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: A selected chatroom
* Response shape:
    ```json
    {
      "chatroom": [
        {
         "name": string,
         "member_count": int,
         "image_url": string,
        }
      ]
    }
    ```

### Send a Message

* Endpoint path: /chatroom
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Sending a Message to chatroom
* Response shape:
    ```json
    {
      "message": [
        {
         "message": string,
        }
      ]
    }

8. Delete a Message
* Endpoint path: /chatroom
* Endpoint method: DELETE


### edit a message - put

* Endpoint path: /messages/int:pk/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    {
      "message": [
        {
          "updated_message": string,
        }
      ]
    }
    ```

* Response: A message context has been changed.
* Response shape (JSON):
    ```json
    {
      "message": [
        {
          "chatroom_id": string,
          "user_id": username,
          "message_id": number,
          "time_stamp": datetime,
          "updated_message": string,
        }
      ]
    }
    ```


### adding a member to a chatroom - put

* Endpoint path: /members/int:pk/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    {
      "membership": True
    }
    ```

* Response: A member is added to a chatroom
* Response shape (JSON):
    ```json
    {
      "member": [
        {
          "user_id": username,
          "chatroom_id": string,
        }
      ]
    }
    ```


### accepting a membership for chatroom- put

* Endpoint path: /membership/int:pk/
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    {
      "accepted": True
    }
    ```

* Response: User accepts the membership invitation
* Response shape (JSON):
    ```json
    {
      "joined_chatroom": [
        {
          "user_id": username,
          "chatroom_id": string,
          "joined_time": datetime,
        }
      ]
    }
    ```


### deleting a member of a chatroom  - delete

* Endpoint path: /members/:memberId
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Member is deleted from the chatroom.
* Response shape (JSON):
    ```json
    {
      "member_deleted": [
        {
          "user_id": username,
          "chatroom_id": string,
        }
      ]
    }
    ```


### declining a chatroom membership - put
Endpoint Path: /users/<int:pk>/
Endpoint Method: PUT
Headers:
    Authorization: Bearer token
Request Shape:
    {
        pending request: boolean
    }
Response: An indication of success or failure
Response Shape:
    ```json
    {
      "success": boolean,
      "message": string
    }
    ```

### create a chatroom - post
Endpoint path: /chatrooms
Endpoint method: POST
Headers:
    Authorization: Bearer token
Request Shape:
    ```json
    {
        "name": string
    }
    ```
response: Indication of success or failure
response Shape:
    ```json
    {
      "success": boolean,
      "message": string
    }
    ```

### delete a chatroom - delete
Endpoint path: /chatrooms/<int:pk>
Endpount Method: DELETE
Headers:
    Authorization: Bearer token
Response: Always true
Response shape (JSON):
    ```json
    true
    ```

### reactions - put
Endpoint path: /chatrooms/<int:pk>/messages/<int:pk>
Endpount Method: PUT
Headers:
    Authorization: Bearer token
Request Shape:
    ```json
    {
        emoji: option
    }
Response: Indication of success or failure
Response shape (JSON):
    ```json
    {
      "success": boolean,
      "message": string
    }
    ```
