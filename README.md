# Kuberfest Framework (WIP)
A lightweight framework for fast cloud development.

## Intro

Kuberfest lets you easily run a local Kubernetes environment, test your deployment in Minikube, and export it as a YAML for a production Kubernetes cluster deployment.

The framework attempts to automate the following real world problems:
1. Differences between dev and production environments are a source for bugs.
2. Syncing the dev environment between team members is challenging and often results in breaks.
3. Maintaining a complex "setup" readme file is tedious and often results in outdated information.
4. New team members are required to waste many hours on manually installing software and configuring their environments.
5. Copy-pasting settings such as environment variables is annoying and often results in mistakes.

Kuberfest is programming language and framework agnostic. Kuberfest itself is built in Python 3.6.

## Current version
0.0.1a (do not use this for anything yet)

## Requirements
* pip
* Python 3.6
* kubectl
* Minikube (tested with virtualbox)

Tested on 'MacOSX 10.13.6'

## Installation
WIP 

## How to use Kuberfest framework
### Through terminal:
python kuberfest/run.py demo_project --start-minikube --delete --build --deploy --init-db

### Through VS Code:
1. Load the root folder in VS Code.
2. Use 'Run demo project' debug profile.

## Motivation
This framework is developed as a way to thoroughly study Kubernetes and on-the-way automate some of the processes in professional projects I'm working on. If you have any comments on the way I'm doing things don't hesitate to shoot me an email :)

## QA
### What do I need to know before using Kuberfest?
1. Learn [how to dockerize your application](https://docs.docker.com/engine/reference/builder/).
2. Learn [how to configure a kubernetes cluster](https://kubernetes.io/docs/concepts/configuration/).
3. Run a Kubernetes cluster, [such as Amazon EKS](https://aws.amazon.com/getting-started/projects/deploy-kubernetes-app-amazon-eks/).
 
### Does my project need to be written in Python?
Nope, use any programming language or framework.

### Why is the demo project written in DotNet Core?
Why are you asking weird questions?
