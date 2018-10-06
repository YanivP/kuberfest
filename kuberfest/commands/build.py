import tools
import os

def run():
    tools.debug("Building container...")
    repository = tools.get_variable('REPOSITORY')
    cwd = os.getcwd()
    os.chdir(tools.get_project_dir())
    os.system(
        'docker-compose build --build-arg "-t {} ."'.format(repository)
    )
    os.chdir(cwd)

    return True