## Nov 15, 2022

Today, I worked on:

* Connecting mongodb and adding fast_api dependencies

We created mongo-db volumes in docker, updated the docker-composer.yaml with three services: mongo, fast-api, and ghi. We also registered pymongo in requirements.txt. We built and ran the docker images. FastAPI docs page ran locally using docker compose successfully.

After that, I worked on my part of the user stories, which are endpoints 9-12. I also created issues in git lab according to the user stories.

* Goal for this week:
FastAPI docs page running locally using docker compose
Create journal files if they are not made already
Take MVP and put it in the readme.md
Any API work/docs need to be in the readme.md


## Nov 16, 2022

Today, I worked on:

* When I was trying to set up the project on my local computer with docker compose, the terminal kept saying that my port 8000 was in use. My team mates tried to help me with this. We tried to delete all the images and containers, used many commands, restarted my laptop, and it still did not work. Finally, I tried with sudo lsof -i:8000 to check what is running on port 8000, and then typed sudo kill <<pid number>> to kill the process running on port 8000. The commands work and the port issue was fixed.

The project now works in my local environment with swagger ui.

## Nov 23, 2022

This week, I worked on creating authenticator. I did pair programming with Michael and I was the driver. I used a website to generate the 64-indexed key. We tried to connect to SIGNING KEY from docker-compose.yaml file, but somehow it just does not recognize the signing key which I put in there. We checked the format and everything but couldn't figure out what we missed. Hopefully we can solve this blocker tomorrow.

## Nov 24, 2022

The blocker from yester was solved but we didnt change any code for it. It seems that sometimes the computer just need wait for a moment and then it work. Now, we are able to connect to the SIGNING KEY in docker-compose file.

## Nov 29, 2022
I worked on CI/CD on my own today. I was able to make CI work. The react front end showed on the new url.
Will be continuing working on the CD part tomorrow.

## Nov 30, 2022
I worked on CD part today. I successfully deployed the project on render.com. I still need to figure out how to connect mongodb to the deployment.

## Nov 30, 2022
The deployment stopped when one person from our team commit their changes. We need to figure out how to commit without failing the deployment.


## Dec 1, 2022
The deployment was only successful with a specific commit. I fixed it and today it was able to automatically and successfully deploy with the latest commit. Fastapi docs was shown on render url. The frontend is showing on its public url as well. Pipline is all fixed. I still need to check if mongodb is connected when our team has routes and data ready for it.

Today my group got together to merge and clean up the branches together. We merged everything useful to main to have a fresh start for everyone. I feel more confident about using git in a group now.

## Dec 2, 2022
Goal: Today's goal was to check if MongoDB is successfully connected to our published application. When our team started working this morning, I saw that our deployment failed again. Need to fix that.

I haven't seen this error message before:
``` pymongo.errors.ServerSelectionTimeoutError: mongo:27017: [Errno -2] Name or service not known, Timeout: 30s, Topology Description: <TopologyDescription id: 638a5751e06dccaa5544c07e, topology_type: Unknown, servers: [<ServerDescription ('mongo', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('mongo:27017: [Errno -2] Name or service not known')>]>```
I think it has something to do with mongodb connection.

We were able to solve this issue with the help of Andrew. The connection named in config.py is wrong. It should be pointing to DATABASE_URL inside docker-compose.yaml. So it should look like this:
```MONGODB_URL = os.environ.get("DATABASE_URL")```

Goal: To import emoji api, and css.
