from kuberfest.tools.kubernetes import KubernetesTool
from kuberfest.tools.debug import Debug
import os


def run(project, value):
    Debug.info('Switching Kubernetes context...')
    KubernetesTool(project).switch_config(value)

    return True
