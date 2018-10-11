import tools
import os
import settings
import commands

def run(project):
    ip=os.popen('minikube ip').read().strip()
    if ip != '':
        tools.debug(
            "You can access the app through: {address}".format(
                address='http://{ip}:{port}/api/values'.format(
                    ip=ip, 
                    port=tools.get_variables()['API_SERVICE_NODE_PORT']
                )
            )
        )
    else:
        tools.debug("Minikube is unavailable")

    return True