import tools
import os

def run():
    tools.debug("Building container...")
    cwd = os.getcwd()
    os.chdir(tools.get_project_dir())
    os.system(
        'docker-compose build --build-arg "-t {} ."'.format(
            tools.get_variable('REPOSITORY')
        )
    )
    os.chdir(cwd)

    return True