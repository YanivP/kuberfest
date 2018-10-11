from commands import CommandsController
import sys
from project import Project
import tools

# First argument must be the project
project_dir_error_message = "First argument must be a project directory"
if len(sys.argv) < 2 or '--' in sys.argv[1]:
    tools.debug(project_dir_error_message)
    exit()

# Build project object
project = Project(
    project_dir = sys.argv[1],
    project_settings = tools.get_project_settings()
)

# Run commands
command_controller = CommandsController(project)

if command_controller.check_commands():
    command_controller.run_commands()
