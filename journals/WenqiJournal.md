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

*

* When I was trying to set up the project on my local computer with docker compose, the terminal kept saying that my port 8000 was in use. My team mates tried to help me with this. We tried to delete all the images and containers, used many commands, restarted my laptop, and it still did not work. Finally, I tried with sudo lsof -i:8000 to check what is running on port 8000, and then typed sudo kill <<pid number>> to kill the process running on port 8000. The commands work and the port issue was fixed.

The project now works in my local environment with swagger ui.
