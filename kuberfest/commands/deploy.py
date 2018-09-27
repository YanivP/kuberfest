import tools
import os
import settings

def run():
    tools.debug("Setting up kubernetes yamls...")
    tools.delete_tmp_dir()
    yamls = list()
    for yaml_file_name in settings.template_file_names:
        yamls.append(tools.get_yaml(yaml_file_name, **tools.get_variables()))
    tools.merge_yamls(yamls, settings.output_yaml_file_name)
    tools.run_yaml(settings.output_yaml_file_name)

    # Wait for deployments
    deployments = list()
    deployments_data = tools.get_yaml_types(tools.get_output_yaml(), 'Deployment')
    for deployment_data in deployments_data:
        deployments.append(deployment_data['metadata']['name'])

    tools.wait_for_deployments(
        yaml_file_name=yaml_file_name,
        namespace=tools.get_variables()['NAMESPACE'],
        deployments=deployments,
    )

    return True
