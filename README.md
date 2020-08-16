# nginx-api

## Concept

Nginx-api is a web interface developed in python that facilitates the configuration of nginx remotely, with this type of interface it becomes much easier to configure a new host on nginx remotely or internally, this tool aims to facilitate the process of continuous integration and continuous delivery of projects hosted on a small infrastructure.

## Use case

For example, this application fits perfectly in a scenario where we have an EC2 container from AWS with nginx acting as a reverse proxy for backends, we can use tools like GitLab Runner, Exoframe, Jenkins to do the CI/CD of the projects, but what about the reverse proxy? We need a simple way to configure a new host, every time a new project is hosted, this is where nginx-api comes in to solve this situation.
