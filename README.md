![kuberfest_logo](https://user-images.githubusercontent.com/2112284/47258411-74416280-d4a3-11e8-8a30-d9df13fb9333.png)

# Kuberfest Framework (WIP)
A lightweight framework for fast cloud development.

## Current version
0.0.1a (Unpolished POC version, possibly buggy)

## Intro

Kuberfest lets you easily run a local Kubernetes environment, test your deployment in Minikube, and export it as a YAML for a production Kubernetes cluster deployment. It's designed to bridge the gap between Developers and Devops.

The framework attempts to solve the following real world problems through automation:
1. Differences between dev and production environments are a source for bugs.
1. Syncing the dev environment between team members is challenging and often results in breaks.
1. Maintaining a complex "setup" readme file is tedious and often results in outdated information.
1. New team members are required to waste many hours on manually installing software and configuring their environments.
1. Copy-pasting settings such as environment variables is annoying and often results in mistakes.

## Dependencies
* pip
* Python 3.6 (I suggest that you use a virtualenv)
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [Minikube](https://kubernetes.io/docs/setup/minikube/) (tested with virtualbox)

Tested on 'MacOSX 10.13.6'

## Installation
Kuberfest is available through pip: `pip install kuberfest`

## Project structure

### Framework
`./kbf`

An executable Python 3.6 script for running Kuberfest.

`./kuberfest/`

This is the framework folder, contains all base framework logic.

### In your own project (in our example: ./dotnet_demo_project/)
`./dotnet_demo_project/kuberfest/`

Your project must contain a `kuberfest` folder with the files and folders mentioned below.

`./dotnet_demo_project/kuberfest/templates`

Contains Kubernetes deployments yamls.

`./dotnet_demo_project/kuberfest/commands`

Can extend the framework's base commands into project-specific commands and automation.
For example, the `--init_db` command isn't part of Kuberfest, but actually an extention written specifically for the demo project.

`./dotnet_demo_project/kuberfest/output`

Will contain the final yaml which is then deployed in Kubernetes.

`./dotnet_demo_project/kuberfest/variables.py`

Can contain variables to be re-used in the Kubernetes yamls

`./dotnet_demo_project/kuberfest/settings.py`

Contains important definitions about your project.

## How to get the demo project running
1. Install base dependencies mentioned above.
1. As with most Python projects, it's best to use a container such as `virtualenv` to avoid conflicts with other projects.
1. Create a folder and copy the content of the `dotnet_demo_project` into it.
1. Open a terminal and navigate into the new project folder.
1. Run `pip install kuberfest`. That should install the `kbf` executable into your virtualenv.
1. Run `kbf --help` to see that you're able to display the help.
1. Run `kbf . --start_minikube --deploy --development --init_db` which will make sure minikube is started, generate and deploy the yamls, and init the db.
1. You should see the message: `You can access the app through: http://x.x.x.x:x/api/values`. Copy that URL to your browser and see if you're getting a response from the API.
1. To test if the database is working, try calling `http://x.x.x.x:x/api/values/1` to see that it inserts a new row with the value `1`. Calling the same API again should result in an index error (by design).

If you got all the way here, congrats! If not, drop me a note.

## Where to go from here?
The demo project you ran in the step before uses a Docker container image which was pre-built for the purpose of the demo. If you want to build your own Docker container image, you'll have to edit the relevant files and direct the project to your own Dockerhub account.

1. Edit the `image` value in `docker-compose.yaml` to your own repository.
1. Edit the `REPOSITORY` value in the demo project's `./kuberfest/variables.py` to the same repository.
1. Run `kbf . --build --push` to build and push your new container.
1. Run the same commands such as `kbf . --start_minikube --deploy --development --init_db` to see that everything is running correctly.

## Motivation
This framework is developed as a way to thoroughly study Kubernetes and on-the-way automate some of the processes in professional projects I'm working on. If you have any comments on the way I'm doing things don't hesitate to shoot me an email :)

## QA
### Why is it called Kuberfest?
Kuberfest uses Kubernetes (Kuber), is meant to allow fast development (fest), and so would save time for celebrations like Oktoberfest. It also sounds really cool.

### What do I need to know before using Kuberfest?
1. Learn [how to dockerize your application](https://docs.docker.com/engine/reference/builder/).
1. Learn [how to configure a kubernetes cluster](https://kubernetes.io/docs/concepts/configuration/).
1. Install the base dependencies mentioned above.
1. Optionally, run a Kubernetes cluster, [such as Amazon EKS](https://aws.amazon.com/getting-started/projects/deploy-kubernetes-app-amazon-eks/). Please note that it's very expensive. I personally don't have the budget to run a real EKS cluster, but if you're a company and want to support this project, drop me a line.
 
### What's planned for the future?
Please refer to [TODO.md](https://github.com/yanivp/kuberfest/blob/master/TODO.md) for a simple project roadmap.
 
### Does my project need to be written in Python?
Kuberfest is programming language and framework agnostic. Kuberfest itself is built in Python 3.6.

### Why is the demo project written in DotNet Core?
This is simply a first of multiple POCs that will come later once the framework is more mature. I like C# and wanted to understand the Entity Framework on the way.

## Credits and licenses
Kubernetes is free to use under the MIT license. Just be nice, give proper credits and keep it legal.

The beer logo is licensed creative commons as mentioned in [the source page](https://www.svgrepo.com/svg/14897/beer). It was manipulated to add the "K" letter on top of the beer mug and the "Kuberfest" name besides it.
