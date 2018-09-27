import tools
import os
import settings
import commands
import collections

def run():
    ordered_arguments = collections.OrderedDict(sorted(commands.commands.items()))

    print("\nThe following arguments are available:")
    print("-------------------------------------------------")
    for argument, data in ordered_arguments.items():
        if 'hidden' not in data or not data['hidden']:
            argument_string = argument.ljust(15)
            print(
                "--{argument} | {description}".format(
                    argument=argument_string,
                    description=data['description'],
                )
            )
    print("-------------------------------------------------")
    print("")

    return True