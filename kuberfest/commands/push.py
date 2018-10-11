import tools
import os
import settings
from tools.debug import Debug


def run(project):
    Debug.info("Pushing docker file...")
    cwd = os.getcwd()
    os.chdir(project.dir)
    os.system(
        'docker push {}'.format(
            project.get_variable('REPOSITORY')
        )
    )
    os.chdir(cwd)

    return True