11/22/22
Today, I worked on:

*

11/21/22
Today, I worked on:

* Finishing more of the endpoints and fixing any errors

Today was all about finally getting to endpoints after getting mongo to
work with fastapi. We did as a group get post, delete, and get to work.
Alot of ah-ha moments come in the from of code. So far it's been placement
so that scope is properly established.


11/18/22
Today, I worked on:

* Trying to get mongo_db to connect to fastapi

Today was a bit tuff as I did not get done what I wanted to do.
Mongo didn't want to be friends with us. We did finally get mongo to accept
a post request from fast api. It did have errors though.. so kind of a win.

11/16/22
Today, I worked on:

* Adding a branch to implement queries/models for the reaction endpoints

At first I worked with the group to nail down some commonality as far as naming conventions
for our branch and how we were going to try and deal with merge requests.



Today I found that -a after say git branch -a would show all the branches that you have
access to.


11/15/22
Today, I worked on:

* Adding the mongodb and fast_api dependencies

The whole group started here so that we could see how the
start of the project was understood by us all. We added mongodb code into our .yaml file and
added pymongo to our requirements.txt file. We made sure that our compose file was set up with
fast api. We then ran docker compose build/up and made sure that the localhost:8000/docs route would lead
us to a fastapi page.

Solo I worked on creating user stories for the api endpoints I worked on previously.

Today we found what uvicorn is doing after a brief google search. I didn't know that
it was server.


11/10/22
Created api_endpoint specs for

1. login - post
2. logout - delete
3. signup - post
4. list of chat room members - get
