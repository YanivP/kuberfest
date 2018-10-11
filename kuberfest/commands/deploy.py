import tools
import os
import settings
from tools.yaml_tool import YamlTool

def run(project):
    tools.debug("Setting up kubernetes yamls...")

    yaml_tool = YamlTool(project)

    project.delete_tmp_dir()
    yamls = list()
    for yaml_file_name in settings.template_file_names:
        yamls.append(yaml_tool.get_yaml(yaml_file_name, **project.get_variables()))
    yaml_tool.merge_yamls(yamls, settings.output_yaml_file_name)
    yaml_tool.run_yaml(settings.output_yaml_file_name)

    # Wait for deployments
    deployments = list()
    deployments_data = yaml_tool.get_yaml_types(yaml_tool.get_output_yaml(), 'Deployment')
    for deployment_data in deployments_data:
        deployments.append(deployment_data['metadata']['name'])

    tools.wait_for_deployments(
        namespace=project.get_variable('NAMESPACE'),
        deployments=deployments,
    )

    return True
