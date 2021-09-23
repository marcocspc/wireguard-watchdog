# -*- coding: utf-8 -*-

import os
from shutil import which
from subprocess import call 
from Errors import WireguardNotFound
import logging

def is_wg_installed():
    if which("wg") is None

def get_peer_list(conf_file_path):
    if is_wg_installed():
        with open(conf_file_path, 'r') as conf_file:
            content = conf_file.read()
    else:
        logging.error("Wireguard not found.")
        raise WireguardNotFound

def run(connection):
    if (is_ssh_installed()):
        cmd = connection.get_ssh_command()
        call(cmd)
    else:
        print('SSH is not available.')

def scp(connection):
    if (is_scp_installed()):
        cmd = connection.get_scp_command()
        call(cmd)
    else:
        print('SCP is not available.')
