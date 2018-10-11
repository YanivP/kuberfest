from consts import kuberfest_dir
import sys
import os
import collections
import commands


def debug(text):
    print(">>> {text}".format(text=text))

_config = 'minikube'
def switch_config(config_name):
    _config = config_name
    os.system(
        'kubectl config use-context {context}'.format(
            context=_config
        )
    )

def get_pods(namespace, app_name):
    pods_string = os.popen(
        'kubectl get pods --namespace={namespace} -l app={app_name} -o=jsonpath=\'{{range .items[*]}}{{.metadata.name}},{{end}}\''.format(
            namespace=namespace,
            app_name=app_name,
        )).read()

    pods_string = pods_string[:len(pods_string)-1]
    return pods_string.split(',')

def wait_for_deployments(namespace, deployments):
    debug("Waiting for deployments... [{}]".format(', '.join(deployments)))
    while (True):
        successes=0
        for deployment in deployments:
            status=os.popen(
                'kubectl rollout status deploy/{deployment} --namespace={namespace}'.format(
                    namespace=namespace,
                    deployment=deployment,
                )
            ).read().strip()

            print(status)
            
            if status == 'deployment "{deployment}" successfully rolled out'.format(deployment=deployment):
                debug(status)
                successes += 1

        if successes == len(deployments):
            break
