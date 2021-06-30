#!/usr/bin/env python3
## Moving files with SFTP
# import from standard library
import os

# imports from pip
import paramiko

HOME = '/home/jordaj2'
def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22)  ## IP and port

    ## how to connect (see other labs on using id_rsa private / public keypairs)
    t.connect(username="bender", password="alta3")

    ## Make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    ## iterate across the files within directory
    for x in os.listdir(f"{os.environ['HOME']}/filestocopy/"):  # iterate on directory contents
        if not os.path.isdir(f"{os.environ['HOME']}/filestocopy/" + x):  # filter everything
            # that is NOT a directory
            sftp.put(f"{os.environ['HOME']}/filestocopy/" + x, "/tmp/" + x)  # move file to target location

    ## close the connection
    sftp.close()  # close the connection


## call the main function
main()