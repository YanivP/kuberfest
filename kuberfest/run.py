from commands import CommandsController
import sys
from project import Project
from tools.debug import Debug


parsed_arguments = CommandsController.parse_arguments()

# Build a project object for the rest of the runtime
project = Project(parsed_arguments['project-dir'][0])

# Run commands for project
command_controller = CommandsController(project)
command_controller.run_commands()
