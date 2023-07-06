#!/usr/bin/python3

"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Create the versions folder if it doesn't exist"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate the archive path using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = os.path.join("versions", archive_name)

        local("tar -czvf {} web_static".format(archive_path))
        return archive_path

    except Exception as e:
        print("An error occurred:", e)
        return None
