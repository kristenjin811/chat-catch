
Wenqi
9. edit a message - put
### «Human-readable of the endpoint»

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
          "member_id": number,
          "group_id": string,
        }
      ]
    }
    ```


11. accepting a membership for chatroom- put
### «Human-readable of the endpoint»

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
