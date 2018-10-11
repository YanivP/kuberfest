import tools

def run(project):
    key_input = input("Are you sure you want to delete the namespace '{0}'? y/n\n".format(
            tools.get_variables()['NAMESPACE'])
        )
    while(True):
        if key_input.lower() == 'y':
            tools.delete_namespace(tools.get_variables()['NAMESPACE'])
            return True
        elif key_input.lower() == 'n':
            tools.debug("Cancelling...")
            return False
        else:
            key_input = input("Please input 'y' or 'n'\n")
