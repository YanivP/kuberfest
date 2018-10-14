import importlib
import tools
from tools.debug import Debug
import argparse


# Commands will be run in the same order of the dictionary
commands = {
    'dev': {
        'description': 'Run as a development environment.',
        'action': 'store',
        'type': bool,
    },
    'print_environment': {
        'description': 'Print the deployment environment.',
        'const': True,
        'default': True,
        'hidden': True,
        'action': 'store',
        'type': bool,
    },
    'context': {
        'description': 'Switch Kubernetes context',
        'default': 'minikube',
        'action': 'store',
        'type': str,
    },
    'delete': {
        'description': 'Delete the kubernetes namespace.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
    },
    'start_minikube': {
        'description': 'Start minikube as part of the deployment.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
    },
    'build': {
        'description': 'Build the project and container.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
    },
    'push': {
        'description': 'Push the docker to the repository.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
    },
    'deploy': {
        'description': 'Deploy kubernetes yamls.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
    },
    'init_db': {
        'description': 'After deployment, also initialize the database and schema.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
    },
    'dev': {
        'description': 'Build a development environment.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
    },
    'minikube_ip': {
        'description': 'Print minikube ip.',
        'const': True,
        'default': True,
        'hidden': True,
        'action': 'store',
        'type': bool,
    }
}


class CommandsController:
    parsed_arguments = None

    def __init__(self, project):
        self.project = project

    @staticmethod
    def parse_arguments():
        if CommandsController.parsed_arguments is not None:
            return CommandsController.parsed_arguments

        parser = argparse.ArgumentParser(
            description='Kuberfest framework',
            add_help=True,
        )

        # Project dir argument
        parser.add_argument(
            'project-dir', 
            nargs=1,
            action='store',
            help='Project app directory',
        )

        # Commands arguments
        for command, command_data in commands.items():
            parser.add_argument(
                '--{}'.format(command),
                nargs='?',
                action=command_data['action'],
                # Uses this vlaue if arg appears, but no explicit value is given 
                const=command_data['const'] if 'const' in command_data else None,
                # Uses this value if arg doesn't appear
                default=command_data['default'] if 'default' in command_data else None, 
                required=True if 'default' not in command_data else None,
                type=command_data['type'],
                help=argparse.SUPPRESS if 'hidden' in command_data and command_data['hidden'] else command_data['description'],
            )

        CommandsController.parsed_arguments = parser.parse_args().__dict__
        return CommandsController.parsed_arguments

    def _run_command(self, command, values):
        if command in commands:
            i = importlib.import_module('commands.' + command)
            result = i.run(self.project, values)
            if not result:
                return False

        return True

    def run_commands(self):
        parsed_arguments = self.parse_arguments()

        for command in commands.keys():
            if not self._run_command(command, parsed_arguments[command]):
                Debug.error('Stopped with partial results.')
                return
