1. List of chatrooms

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

2. Show selected chatroom

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

Send a Message

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
 
$. Delete a Message
* Endpoint path: /chatroom
* Endpoint method: DELETE

