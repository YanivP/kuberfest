from commands import CommandsController
import sys
from project import Project
import tools
from tools.debug import Debug


# First argument must be the project
if len(sys.argv) < 2 or '--' in sys.argv[1]:
    Debug.error("First argument must be a project directory")
    exit()

# Build project object
project = Project(sys.argv[1])

# Run commands
command_controller = CommandsController(project)

if command_controller.check_commands():
    command_controller.run_commands()
