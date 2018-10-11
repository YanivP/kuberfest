import importlib
import sys
import tools

# Commands will be run in the same order of the dictionary
commands = {
    'dev': {
        'description': 'Run as a development environment.',
    },
    'print-environment': {
        'description': 'Print the deployment environment.',
        'default': True,
        'hidden': True,
    },
    'help': {
        'description': 'Print all the arguments.',
        'stopper': True,
    },
    'context': {
        'description': 'Switch Kubernetes context',
        'default': True,
        'hidden': True,
    },
    'delete': {
        'description': 'Delete the kubernetes namespace.'
    },
    'start-minikube': {
        'description': 'Start minikube as part of the deployment.'
    },
    'build': {
        'description': 'Build the project and container.'
    },
    'push': {
        'description': 'Push the docker to the repository.'
    },
    'deploy': {
        'description': 'Deploy kubernetes yamls.'
    },
    'init-db': {
        'description': 'After deployment, also initialize the database and schema.'
    },
    'dev': {
        'description': 'Build a development environment.'
    },
    'minikube-ip': {
        'description': 'Print minikube ip.',
        'default': True,
        'hidden': True,
    }
}

class CommandsController:
    def __init__(self, project):
        self.project = project

    def run_command(self, command):
        if command in commands:
            i = importlib.import_module('commands.' + command)
            result = i.run(self.project)
            if not result:
                return False

        return True

    def check_commands(self):
        bad_commands = list()
        for arg in sys.argv[2:]:
            if arg[2:] not in commands:
                bad_commands.append(arg)

        if len(bad_commands) == 1:
            print('Command [{}] is unsupported'.format(', '.join(bad_commands)))
            return False
        elif len(bad_commands) > 1:
            print('Commands [{}] are unsupported'.format(', '.join(bad_commands)))
            return False

        return True

    def run_commands(self):
        for command in commands.keys():
            if 'default' in commands[command] and commands[command]['default'] or '--{}'.format(command) in sys.argv:
                if not self.run_command(command):
                    tools.debug('Stopped with partial results.')
                    return

            if 'stopper' in commands[command] and commands[command]['stopper'] and '--{}'.format(command) in sys.argv:
                break
