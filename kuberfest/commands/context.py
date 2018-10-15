import tools
from tools.kubernetes import KubernetesTool
from tools.debug import Debug
import os


def run(project, value):
    Debug.info('Switching Kubernetes context...')
    context = project.get_variable('CONTEXT')

    # TODO: Allow switching manually
    KubernetesTool(project).switch_config(value)

    return True