#!/usr/bin/python3

"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""

from fabric import Connection
from datetime import datetime
import os


def do_pack():
    # Creating 'versions' folder if it not exists
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Generate the final archive path using current timestamp
    timesamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{time_stamp}.tgz'
    archive_path = os.path.join('versions', archive_name)

    # Creating the tar archive using tar command
    tar_comm = f'tar -czvf {archive_path} web_static'
    result = c.local(tar_command)

    # Check if the tar command was successful
    if result.ok:
        return archive_path
    else:
        return None
