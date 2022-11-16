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
