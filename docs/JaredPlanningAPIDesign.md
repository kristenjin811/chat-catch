EndPoints -
Dean
1. login - post
2. logout - delete
3. signup - post
4. list of chat room members - get

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

Jared
13. declining a chatroom membership - delete
14. create a chatroom - post
15. delete a chatroom - delete
16. reactions - put







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
