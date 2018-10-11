import tools

def run(project):
    tools.debug(
        "Starting deployment with {0} environment...".format(
            'DEVELOPMENT' if tools.is_development() else 'PRODUCTION'
        )
    )

    return True