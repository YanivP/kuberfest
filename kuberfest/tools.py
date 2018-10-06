from consts import kuberfest_dir
import sys
import os
import collections
import yaml as yaml_module
import commands

def get_project_dir():
    return sys.argv[1]

def debug(text):
    print(">>> {text}".format(text=text))

# Import project settings
try:
    project_dir = "{0}/{1}".format(get_project_dir(), kuberfest_dir)
    debug("Importing project settings at '{}'...".format(project_dir))
    sys.path.append(project_dir)
    import settings as project_settings
except ModuleNotFoundError:
    debug("Project dir not found at '{}'".format(project_dir))
    exit()

_config = 'minikube'
def switch_config(config_name):
    _config = config_name
    os.system(
        'kubectl config use-context {context}'.format(
            context=_config
        )
    )

_is_development = False
def set_development(is_development):
    global _is_development
    _is_development = is_development

def is_development():
    global _is_development
    return _is_development

def get_variables():
    try:
        import variables
        return variables.__dict__
    except ModuleNotFoundError:
        debug("You must have a 'variables.py' file in your project's 'kuberfest' folder")
        exit()

def get_variable(variable_name):
    variables = get_variables()
    if variable_name not in variables:
        debug("Variable '{}' not found".format(variable_name))
        exit()

    return variables[variable_name]

def delete_tmp_dir():
    os.system('rm -r {0}/{1}'.format(get_project_dir(), project_settings.output_dir))
    os.system('mkdir {0}/{1}'.format(get_project_dir(), project_settings.output_dir))

def get_yaml(yaml_file_name, **kwargs):
    with open(
        "{project_dir}/{templates_dir}/{yaml_file_name}".format(
            project_dir=get_project_dir(),
            templates_dir=project_settings.templates_dir,
            yaml_file_name=yaml_file_name,
        ), 'r') as yaml_file:
        yaml_string = yaml_file.read()
        return yaml_string.format(**kwargs)

def merge_yamls(yamls_list, output_file_name):
    all_yaml_strings = ''
    for yaml_string in yamls_list:
        all_yaml_strings += '---\n{0}\n\n'.format(yaml_string.strip())
        
    with open(
        "{project_dir}/{output_dir}/{output_file_name}".format(
            project_dir=get_project_dir(),
            output_dir=project_settings.output_dir, 
            output_file_name=output_file_name
        ),
        "w+"
    ) as yaml_file:
        yaml_file.write(all_yaml_strings)

def run_yaml(yaml_file_name, **kwargs):
    os.system(
        'kubectl apply -f {project_dir}/{output_dir}/{yaml_file_name}'.format(
            project_dir=get_project_dir(),
            output_dir=project_settings.output_dir,
            yaml_file_name=yaml_file_name,
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

def get_output_yaml():
    with open('{}/{}/{}'.format(get_project_dir(), project_settings.output_dir, project_settings.output_yaml_file_name), 'r') as output_yaml_file:
        yaml_string = output_yaml_file.read()
        return yaml_string

def get_yaml_types(yaml_string, yaml_type):
    ret_list = list()
    
    yamls = yaml_string.split('---')
    for yaml in yamls:
        if len(yaml.strip()) > 0:
            yaml_dict = yaml_module.load(yaml)
            if isinstance(yaml_dict, dict) and yaml_dict['kind'] == yaml_type:               
                ret_list.append(yaml_dict)

    return ret_list

def wait_for_deployments(namespace, deployments, yaml_file_name):
    debug("Waiting for deployments...")
    while (True):
        successes=0
        for deployment in deployments:
            status=os.popen(
                'kubectl rollout status deploy/{deployment} --namespace={namespace}'.format(
                    namespace=namespace,
                    deployment=deployment,
                )
            ).read().strip()

            if status == 'deployment "{deployment}" successfully rolled out'.format(deployment=deployment):
                debug(status)
                successes += 1

        if successes == len(deployments):
            break

def delete_namespace(namespace):
    os.system(
        'kubectl delete namespaces {namespace}'.format(
            namespace=namespace
        )
    )