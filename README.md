## Chat Catch
<p align="center">
  <img width="auto" height="auto" src="images/chat-logo.png">
</p>

## OverView
<p align="center">
  <img width="auto" height="auto" src="images/OverviewCC.png">
</p>

## Login page
<p align="center">
  <img width="auto" height="auto" src="images/login_page.png">
</p>

## Logout page
<p align="center">
  <img width="auto" height="auto" src="images/logout_page.png">
</p>


## Getting started

You have a project repository, now what? The next section
lists all of the deliverables that are due at the end of the
week. Below is some guidance for getting started on the
tasks for this week.

## Install Extensions

* Prettier: <https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode>
* Black Formatter: <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>

## Deliverables
### Wireframes
<p align="center">
  <img width="auto" height="auto" src="images/WireFrameCC.png">
</p>


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


## Project layout

The layout of the project is just like all of the projects
you did with `docker-compose` in module #2. You will create
a directory in the root of the repository for each service
that you add to your project just like those previous
projects were setup.

### Directories

Several directories have been added to your project. The
directories `docs` and `journals` are places for you and
your team-mates to, respectively, put any documentation
about your project that you create and to put your
project-journal entries. See the _README.md_ file in each
directory for more info.

The other directories, `ghi` and `sample_service`, are
sample services, that you can start building off of or use
as a reference point.

Inside of `ghi` is a minimal React app that has an "under
construction" page. It is setup similarly to all of the
other React projects that you have worked on.

Inside of `sample_service` is a minimal FastAPI application.
"Where are all the files?" you might ask? Well, the
`main.py` file is the whole thing, and go take look inside
of it... There's not even much in there..., hmm? That is
FastAPI, we'll learn more about it in the coming days. Can
you figure out what this little web-application does even
though you haven't learned about FastAPI yet?

Also in `sample_service` is a directory for your migrations.
If you choose to use PostgreSQL, then you'll want to use
migrations to control your database. Unlike Django, where
migrations were automatically created for you, you'll write
yours by hand using DDL. Don't worry about not knowing what
DDL means; we have you covered. There's a sample migration
in there that creates two tables so you can see what they
look like.

The sample Dockerfile and Dockerfile.dev run your migrations
for you automatically.

### Other files

The following project files have been created as a minimal
starting point. Please follow the guidance for each one for
a most successful project.

* `docker-compose.yaml`: there isn't much in here, just a
  **really** simple UI and FastAPI service. Add services
  (like a database) to this file as you did with previous
  projects in module #2.
* `.gitlab-ci.yml`: This is your "ci/cd" file where you will
  configure automated unit tests, code quality checks, and
  the building and deployment of your production system.
  Currently, all it does is deploy an "under construction"
  page to your production UI on GitLab and a sample backend
  to Render.com. We will learn much more about this file.
* `.gitignore`: This is a file that prevents unwanted files
  from getting added to your repository, files like
  `pyc` files, `__pycache__`, etc. We've set it up so that
  it has a good default configuration for Python projects.

## How to complete the initial deploy

There will be further guidance on completing the initial
deployment, but it just consists of these steps:

### Setup GitLab repo/project

* make sure this project is in a group. If it isn't, stop
  now and move it to a GitLab group
* remove the fork relationship: In GitLab go to:

  Settings -> General -> Advanced -> Remove fork relationship

* add these GitLab CI/CD variables:
  * PUBLIC_URL : this is your gitlab pages URL
  * SAMPLE_SERVICE_API_HOST: enter "blank" for now

#### GitLab pages URL

https://chatty-cathys.gitlab.io/chat-catch


### Update GitLab CI/CD variables


Copy the service URL for your new render.com service and then paste
that into the value for the SAMPLE_SERVICE_API_HOST CI/CD variable
in GitLab.

### Deploy it

https://chat-catch.onrender.com
