import os

def run():
    if os.popen('minikube ip').read().strip() == '':
        os.system('minikube start')

    return True