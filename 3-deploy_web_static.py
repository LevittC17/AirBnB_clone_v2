#!/usr/bin/python3

"""
Deploy the archive
base file -> 1-pack_web_static.py
"""

import os
form fabric.api import env, put, run



# Set the web servers' IP addresses and username
env.hosts = ['', '']
env.user = 'ubuntu'


def do_pack():
    """Create a compressed archive of the web_static folder"""
    try:
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_path = 'versions/web_static_{}.tgz'.format(current_time)
        local('mkdir -p versions')
        local('tar -czvf {} web_static'.format(archive_path)

        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """Deploys the archive to the servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web servers
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        archive_filename = os.path.basename(archive_path)
        release_dir = '/data/web_static/releases/' + archive_filename[:4]
        run('mkdir -p {}'.format(release_dir))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_dir))

        # Remove the upload archive
        run('rm /tmp/{}'.format(archive_filename))

        # Move the extracted files to the correct location
        run('mv {}/web_static/* {}'.format(release_dir, release_dir))

        # Remove the web_static symbolic link
        run('rm -rf {}/web_static'.format(release_dir))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_dir)

        print('New version deployed')
        return True

    except Exception as e:
        print('Deployment failed:', e)
        return False


def deploy():
    """Deployes the archive to the web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
