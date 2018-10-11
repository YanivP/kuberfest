from commands import CommandsController
import sys
from project import Project
from tools.debug import Debug


# First argument must be the project
if len(sys.argv) < 2 or '--' in sys.argv[1]:
    Debug.error("First argument must be a project directory")
    exit()

# Build a project object for the rest of the runtime
project = Project(sys.argv[1])

# Run commands for project
command_controller = CommandsController(project)
if command_controller.check_commands():
    command_controller.run_commands()
