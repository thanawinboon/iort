#this is the python file that is used for the terminal to run
#the command in the middle is the same syntax as the CLI

import subprocess

myprocess = subprocess.Popen(
    [
        'ls',
        '-l'
        ]
    , stdin=subprocess.PIPE
    )