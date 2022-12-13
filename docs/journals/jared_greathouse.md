December 12, 2022
Over the weekend we all worked hard to make sure pipelines were fixed, README was updated, memberlist showed up when inside a chatroom, and all unit tests except for mine were functional. I got some help from Adrian and James to get my unit test built as my api endpoints were using asynchronous queries and finding material to help me build a unit test based on them was difficult to come by. It took a bit to insert my unit test and fix the pipeline, but after we did. Adrian did a dry run with us and we performed a demo for Shahzhad and Andrew.

December 9, 2022
Woke up this morning and had an epiphany about why the websockets were closing down chatrooms when any user abruptly closed their web browser. I changed the websocket path to have user_name then chatroom_name instead of the reverse. I also turned off the dismissal broadcast message, as I think this was also contributing to the error.  We worked on fixing our deployment pipeline with flake8 work and working out more functionality.

December 8, 2022
Really discouraged today. We were able to merge my websocket code with the rest of the team's code base, we can initiate a websocket and do a few rounds of live-chat, but if any user refreshes their browser, all chatrooms which that user went to get closed and no other user can access them afterwords until the server is rebooted. Worked with Daniel until late and could not discover what the problem was.

December 7, 2022
I am still working on the websocket, but now we thought it was important for me to merge my websocket code as it currently is with everyone else's code that has been merged in main. My hope is that if we merge our code, we will have a better idea of exactly what needs to be done besides the websocket and unit tests.

December 6, 2022
The rest of the group appears to be making real head way on the authentication and front end. We are try to deploy our app as it is now, just to get familiar with the process. We now understand the pipeline and why every time we push it says pipeline failed. We are making sure to run flake8 on our project before pushing and leave all unit tests commented out with a fake test only, so we can pass the pipeline.

December 5, 2022
Over the weekend, I was able to get the websocket to connect, but all the rooms close down after a web browser refresh. back to the drawing board.

December 2, 2022
Working on getting the websocket working. Been wracking my brain trying to figure this out. I don't know if I can make this work.

December 1, 2022
We finished merging branches to main as a group and fixing our app file structure. Then Dean and I pair programmed our barebones endpoints for users and chatrooms. We are feeling much better about our project and understand that we will have to work through the weekend to get the back end fully functional.

November 30, 2022
We agreed that all the branches that we were making on our local systems were getting out of hand and our file structure was still chaotic. We decided to do some merging on our local systems and agreed about what to do with merges. I am creating a new document that explains the way all the files on the backend fit together. we are also trying to pass flake8 before pushing to main.

November 29, 2022
We feel pretty lost. I am stressed and not sure how things are fitting together. trying to not let my anxiety make me quick working on it. I hope something clicks for me soon... The rest of the group is doing well making unit tests, doing CI/CD, and front-end.

November 28, 2022
First day after thanksgiving weekend. Dean spent a good amount of time trying to figure out how to connect socket.io to mongo, but saw that the complexity and dependencies are multiplying. Nobody else did any work over the break. Understandable, but now the pressure is on and I still cannot see how things are coming together. I am going to try and slow down and just take things piece by piece and hope to come away with some new understanding. One thing is for sure, we are switching to websockets and no longer trying to implement socket.io

November 23, 2022
Last day before thanksgiving weekend. Dean is sick but promised to do some work trying to link up socket.io events to the mongodb.  I continued researching socket.io and how it can be implemented with mongo and fastapi. The others are working on front end, finding css kits, third party apis for emojis and wait not. I am not feeling super confident about the project and in-laws are in town for thanksgiving so I will probably not have much time to work on it.

November 22, 2022
Dean was able to implement the socket.io backend and demonstrated that different web browsers can connect to sockets and have a live chat, but chat is not persistent, so refreshing the web browser will erase all previous chat history. we know that we need to implement a client-side or front end socket.io also, and connect to mongo. I'm still confused about how the code works, but at least Dean was able to get part of this working.

November 21, 2022
Short week. Dean and I are researching Socket.io still and trying to find reference projects to let us try this out. documentation is hard to come by. seems like few people have used the tech stack of fastapi, mongodb, socket.io, and react.

November 18, 2022
I am sick and did not do any coding. just rested.

November 17, 2022
We did some pair programming today to create some endpoints, but my socket.io research gave me the insight that our endpoints will change because the implementation of websockets makes things different. I'm starting to not feel very well. Hopefully, I will feel better tomorrow.

November 16, 2022
Began making a model map in excalidraw that maps out the models and their relationships. Made issues to create model queries and group members assigned themselves to them. The group tested creating new branches, pushing them, and did a mock merge request.
We realized that we need to continue fleshing out the model maps to figure out what queries to make and how to break up our microservices.
My ah-ha moment today was realizing that I cannot wait for the mongo db lecture.


November 15, 2022
created issues that corresponded to our API endpoints and user stories. We got the fastapi docs page running locally, but mongo database is acting strange
Reflected on the fact that our endpoint list is not comprehensive.
My ah-ha moment was that we are now getting our project off the ground and feeling more capable of finishing this mod 3 project.
