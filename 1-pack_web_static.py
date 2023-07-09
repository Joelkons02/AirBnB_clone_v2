from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        # Create the folder versions if it doesn't exist
        local("mkdir -p versions")

        # Create the name of the archive
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + now + ".tgz"

        # Create the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path of the archive if it was created successfully
        return "versions/{}".format(archive_name)
    except:
        # Return None if an exception occurred
        return None
