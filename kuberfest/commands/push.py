import tools
import os
import settings

def run(project):
    tools.debug("Pushing docker file...")
    cwd = os.getcwd()
    os.chdir(project.dir)
    os.system(
        'docker push {}'.format(
            project.get_variable('REPOSITORY')
        )
    )
    os.chdir(cwd)

    return True