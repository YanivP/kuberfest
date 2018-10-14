import importlib
import tools
from tools.debug import Debug
import argparse


# Commands will be run in the same order of the dictionary
commands = {
    'dev': {
        'description': 'Run as a development environment.',
        'is_flag': True,
        'action': 'store',
    },
    'print_environment': {
        'description': 'Print the deployment environment.',
        'default': True,
        'hidden': True,
        'is_flag': True,
        'action': 'store',
    },
    'context': {
        'description': 'Switch Kubernetes context',
        'default': 'minikube',
        'action': 'store',
    },
    'delete': {
        'description': 'Delete the kubernetes namespace.',
        'default': False,
        'is_flag': True,
        'action': 'store',
    },
    'start_minikube': {
        'description': 'Start minikube as part of the deployment.',
        'default': False,
        'is_flag': True,
        'action': 'store',
    },
    'build': {
        'description': 'Build the project and container.',
        'default': False,
        'is_flag': True,
        'action': 'store',
    },
    'push': {
        'description': 'Push the docker to the repository.',
        'default': False,
        'is_flag': True,
        'action': 'store',
    },
    'deploy': {
        'description': 'Deploy kubernetes yamls.',
        'default': False,
        'is_flag': True,
        'action': 'store',
    },
    'init_db': {
        'description': 'After deployment, also initialize the database and schema.',
        'default': False,
        'is_flag': True,
        'action': 'store',
    },
    'dev': {
        'description': 'Build a development environment.',
        'default': False,
        'is_flag': True,
        'action': 'store',
    },
    'minikube_ip': {
        'description': 'Print minikube ip.',
        'default': True,
        'hidden': True,
        'is_flag': True,
        'action': 'store',
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

        for command, command_data in commands.items():
            const = None
            if 'is_flag' in command_data:
                const = command_data['is_flag']
            elif 'const' in command_data:
                const = command_data['const']

            parser.add_argument(
                '--{}'.format(command),
                nargs='?',
                action=command_data['action'],
                help=command_data['description'],
                # Uses this value if arg doesn't appear
                default=command_data['default'] if 'default' in command_data else None, 
                required=True if 'default' not in command_data else None,
                # Uses this vlaue if arg appears, but no explicit value is given 
                const=const  
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
