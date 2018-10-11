import tools
from tools.debug import Debug

def run(project):
    Debug.info(
        "Starting deployment with {0} environment...".format(
            'DEVELOPMENT' if project.is_development() else 'PRODUCTION'
        )
    )

    return True