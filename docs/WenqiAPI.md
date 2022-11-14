
Wenqi
9. edit a message - put
### «Human-readable of the endpoint»

* Endpoint path: /messages
* Endpoint method: PUT
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
    {
      "message": [
        {
          "group_id": string,
          "user_id": username,
          "message_id": number,
          "time_stamp": datetime,
          "updated_message": string,
        }
      ]
    }
    ```


10. adding a member to a chatroom - put
### «Human-readable of the endpoint»

* Endpoint path: /members
* Endpoint method: PUT
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
    {
      "member": [
        {
          "user_id": username,
          "member_id": number,
          "group_id": string,
        }
      ]
    }
    ```


11. accepting a membership for chatroom- put
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
    {
      "joined_chatroom": [
        {
          "user_id": username,
          "member_id": number,
          "group_id": string,
          "joined_time": datetime,
        }
      ]
    }
    ```


12. deleting a member of a chatroom  - delete
### «Human-readable of the endpoint»

* Endpoint path: /members/:memberId
* Endpoint method: DELETE
* Query parameters:
  * member_id

* Headers:
  * Authorization: Bearer token

* Response: Member is deleted from the chatroom.
* Response shape (JSON):
    ```json
    {
      "member_deleted": [
        {
          "user_id": username,
          "member_id": number,
          "group_id": string,
        }
      ]
    }
    ```
