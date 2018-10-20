from kuberfest.tools.debug import Debug
from kuberfest.commands import CommandsController
import sys
from kuberfest.project import Project

def run():
    # Build a project object for the rest of the runtime
    project = Project(CommandsController.get_project_dir_from_arguments())

    # Run commands for project
    command_controller = CommandsController(project)
    command_controller.run_commands()
