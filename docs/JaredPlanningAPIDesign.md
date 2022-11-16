EndPoints -
Dean
1. login - post
2. logout - delete
3. signup - post
4. list of chat room members - get

1. As a user, I want to be able to log in, So that I know my information and conversations are safe
2. As a user, I want to be able to log out, So that I know my information and conversations are safe
3. As a user, I want users to have to sign-up / have accounts, So that random users are not allowed to break any terms of service (harassment/bulling)
4. As a user, I want to be able to see all the chat room members, So that I can connect with them / or reach out to them separately / read bio

Michael
5. list of chat rooms - get
6. Show selected chatroom - get
7. send a message - post
8. delete a message - delete

Wenqi
9. edit a message - put
10. adding a member to a chatroom - put
11. accepting a membership for chatroom- put
12. deleting a member of a chatroom  - delete

9. As a user, I want to modify a message that I already sent, so that the message speaks what I want to say.
10. As a chatroom creator, I want to add other user into a chatroom that I am in, so that the user can chat together in the group.
11. As a user, I want to accept a chatroom membership, so that I can talk in the chatroom.
12. As a creator of a chatroom, I want to delete a member from the group, so that I have control on which users can be in this chatroom.


Jared
13. declining a chatroom membership - delete
14. create a chatroom - post
15. delete a chatroom - delete
16. reactions - put

13. As a User, I want to decline a membership request for a chatroom, so I can manage the amount and quality of chatrooms I am in.
14. As a User, I want to create a chatroom, so that I might bring together a new group of users to chat about a particular topic.
15. As a Chatroom Creater, I want to delete a chatroom, so that I do not need to maintain chatrooms that are dead and keep having them in my list of chatrooms.
16. As a chatroom member, I want to respond to messages with an emoji, so that I can engage with a message without writing another message.






### «Human-readable of the endpoint»

* Endpoint path: «path to use»
* Endpoint method: «HTTP method»
* Query parameters:
  * «name»: «purpose»

* Headers:
  * Authorization: Bearer token

* Request shape (JSON):
    ```json
    «JSON-looking thing that has the
    keys and types in it»
    ```

* Response: «Human-readable description
            of response»
* Response shape (JSON):
    ```json
    «JSON-looking thing that has the
    keys and types in it»


13. declining a chatroom membership - put
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


14. create a chatroom - post
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

15. delete a chatroom - delete
Endpoint path: /chatrooms/<int:pk>
Endpount Method: DELETE
Headers:
    Authorization: Bearer token
Response: Always true
Response shape (JSON):
    ```json
    true
    ```

16. reactions - put
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
