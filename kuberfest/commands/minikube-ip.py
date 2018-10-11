import tools
import os
import settings
import commands
from tools.debug import Debug


def run(project):
    ip=os.popen('minikube ip').read().strip()
    if ip != '':
        Debug.info(
            "You can access the app through: {address}".format(
                address='http://{ip}:{port}/api/values'.format(
                    ip=ip, 
                    port=project.get_variable('API_SERVICE_NODE_PORT')
                )
            )
        )
    else:
        Debug.error("Minikube is unavailable")

    return True