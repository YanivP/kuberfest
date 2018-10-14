import importlib
import tools
from tools.debug import Debug
import argparse
import consts


# Commands will be run in the same order of the dictionary
commands = {
    'development': {
        'short': 'dev',
        'description': 'run as a development environment.',
        'const': False,
        'default': False,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'print_environment': {
        'short': 'pc',
        'description': 'print the deployment environment.',
        'const': True,
        'default': True,
        'hidden': True,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'context': {
        'short': 'c',
        'description': 'switch Kubernetes context',
        'default': 'minikube',
        'action': 'store',
        'type': str,
        'nargs': '?',
    },
    'delete': {
        'short': 'del',
        'description': 'delete the kubernetes namespace.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'start_minikube': {
        'short': 'smkb',
        'description': 'start minikube as part of the deployment.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'build': {
        'short': 'b',
        'description': 'build the project and container.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'push': {
        'short': 'p',
        'description': 'push the docker to the repository.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'deploy': {
        'short': 'd',
        'description': 'deploy kubernetes yamls.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'init_db': {
        'short': 'idb',
        'description': 'after deployment, also initialize the database and schema.',
        'const': True,
        'default': False,
        'action': 'store',
        'type': bool,
        'nargs': '?',
    },
    'minikube_ip': {
        'short': 'mkbip',
        'description': 'print minikube ip.',
        'const': True,
        'default': True,
        'hidden': True,
        'action': 'store',
        'type': bool,
        'nargs': '?',
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
            prog=consts.kuberfest_name,
            description=consts.kuberfest_description,
            add_help=True,
        )

        # Project dir argument
        parser.add_argument(
            'project_dir', 
            nargs=1,
            action='store',
            help='Project app directory',
        )

        # Commands arguments
        for command, command_data in commands.items():
            parser.add_argument(                
                '--{}'.format(command),
                '--{}'.format(command_data['short']),
                metavar=str(command_data['type'])[8:-2],
                nargs=command_data['nargs'],
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
