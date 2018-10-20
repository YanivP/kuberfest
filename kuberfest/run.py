from kuberfest.tools.debug import Debug
from kuberfest.commands import CommandsController
import sys
from kuberfest.project import Project

def run():
    parsed_arguments = CommandsController.parse_arguments()

    # Build a project object for the rest of the runtime
    project = Project(parsed_arguments['project_dir'][0])

    # Run commands for project
    command_controller = CommandsController(project)
    command_controller.run_commands()
