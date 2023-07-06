#!/usr/bin/python3

"""
Deploying the archive
base file -> 1-pack_web_static.py
"""


from fabric.api import env, put, run
import os


# Set web servers IP Addresses
env.hosts = ['18.207.140.105', '52.87.216.159']

def do_deploy():
    # The function deploys the archive to the web servers
    if not os.path.exists(archive_path):
        return False

    try:
        # Uploading the archive on the servers
        put(archive_path, '/tmp')

        # Extracting the archive
        archive_filename = os.path.basename(archive_path)
        archive_dirname = os.path.splitext(archive_filename)[0]
        release_path = '/data/web_static/releases/{}'.format(archive.dirname)
        run('mkdir -p {}'.format(release_path)
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Delete the Upload archive
        run('rm /tmp/{}'.format(archive_filename)

        # Move the extracted archive to the correct location
        run('mv {}/web_static/* {}'.format(release_path, release_path)
        # Removing the symbolic link
        run('rm -rf {}/web_static'.format(release_path)
        # Delete the current symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_path)

    except Exception as e:
        print('Deployment failed:', e)
        return False
