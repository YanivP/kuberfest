### Planned features ###
* Make environment variables easily exportable to container.
  * Also consider production environment such as encrypted variables.
* Generate a migrations server for deployments as a prove of concept it can include.
* Fix issue with Postgres not persisting after restarting a pod.
* Create python script for downloading all dependencies.
  * Python
  * Kubernetes
  * Minikube
  * VMWare
* Create a project generator script.
* Auto-generate a docker-compose.yml file which will take the image name from an external source.

### Wishful features ###
* Set up a simple CI/CD to a real AWS Kubernetes cluster in order to prove the concept.
  * Requires funding, EKS is very expensive.
