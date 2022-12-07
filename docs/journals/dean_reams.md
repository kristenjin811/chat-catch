12/6/22
Today, I worked on:

- 

12/5/22
Today, I worked on:

- After wenqi provided the front-end appearance of the
web app I started to try and implement the components that
we want the functionality to work. It's been a challenge.
I did get members to populate based off chat-rooms, did get
messages to to populate to with emojis to a database.

12/4/22
Today, I worked on:

- trying to figure out websocket communication I think
that i'm not going to completely understand how to
make a connection with a websocket server. I wish
this wasn't so hard.

12/3/22
Today, I worked on:

- creating react components that will request things from
or to the backend, along with trying to see how to
implement websocket communication.

12/2/22
Today, I worked on:

- working on the getting endpoints back up and running

along with a little research about websocket's which has not been
implemented nor is it seem clear how to use it. I do plan on using
the weekend to try and figure out how to implement things

12/1/22
Today, I worked on:

- continuing to reimplement code

After the restructuring of the code base, it did take a bit of
work to get everything back up to a working state. Now it is a bit
clearer and ready to start working. Where we created endpoints
and tested them got a few up and running was semi productive event,
even though I wish we were farther lol.

11/30/22
Today, I worked on:

- helping refactor file structure

After looking at the code base, the group decided it was a little
confusing so the structure was redone to allow for better clarity on the code base.

11/29/22
Today, I worked on:

- created unit tests for our app

It was kinda interesting and a little nice to see green finally on three of the test created.
I did notice that throughout the process we do not have a put request
in our app so I think I will try to make that happen.

11/28/22
Today, I worked on:

- making a poller from users to a userVO inside of chat database

after getting it mostly coded out we have come to the conclusion that
we most likely will not need a poller to do what we want to do so unfortunately
that was some time spent squandered but I learned a little so that helps.

11/23/22
Today, I worked on:

- Trying to get socket.io to connect with our db

After we had tried for about 5 hours to figure out how to connect
socket.io to our database with multiple failures and limited help
in that area, we have decided to switch to just using websockets.

11/22/22
Today, I worked on:

- Endpoints

I think that endpoint is a word I no longer know.. It seems
like we have been on endpoints for a long time but hopefully we
are getting there.

11/21/22
Today, I worked on:

- Finishing more of the endpoints and fixing any errors

Today was all about finally getting to endpoints after getting mongo to
work with fastapi. We did as a group get post, delete, and get to work.
Alot of ah-ha moments come in the from of code. So far it's been placement
so that scope is properly established.

11/18/22
Today, I worked on:

- Trying to get mongo_db to connect to fastapi

Today was a bit tuff as I did not get done what I wanted to do.
Mongo didn't want to be friends with us. We did finally get mongo to accept
a post request from fast api. It did have errors though.. so kind of a win.

11/16/22
Today, I worked on:

- Adding a branch to implement queries/models for the reaction endpoints

At first I worked with the group to nail down some commonality as far as naming conventions
for our branch and how we were going to try and deal with merge requests.

Today I found that -a after say git branch -a would show all the branches that you have
access to.

11/15/22
Today, I worked on:

- Adding the mongodb and fast_api dependencies

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
