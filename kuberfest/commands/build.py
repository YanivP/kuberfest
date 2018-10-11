import tools
import os

def run(project):
    tools.debug("Building container...")
    repository = project.get_variable('REPOSITORY')
    cwd = os.getcwd()
    os.chdir(project.dir)
    os.system(
        'docker-compose build --build-arg "-t {} ."'.format(repository)
    )
    os.chdir(cwd)

    return True