import tools
import os

def run(project):
    tools.debug('Switching Kubernetes context...')
    context = project.get_variable('CONTEXT')

    # TODO: Allow switching manually
    tools.switch_config('minikube')

    return True