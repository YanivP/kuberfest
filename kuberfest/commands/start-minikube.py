import os

def run(project):
    if os.popen('minikube ip').read().strip() == '':
        os.system('minikube start')

    return True