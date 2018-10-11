import tools
import os
import settings

def run(project):
    tools.debug("Pushing docker file...")
    cwd = os.getcwd()
    os.chdir(tools.get_project_dir())
    os.system(
        'docker push {}'.format(
            tools.get_variable('REPOSITORY')
        )
    )
    os.chdir(cwd)

    return True