#!/usr/bin/env python


"""
test all the tools in tolino cloud
"""

import os
import unittest
import configparser


from pytolino.tolino_cloud import Client, PytolinoException


class TestClient(unittest.TestCase):

    """all test concerning the Client class. """

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

    def test_init_nopartner(self):

        with self.assertRaises(PytolinoException):
            Client(server_name='this tolino partner does not exists')

    def test_init_partner_config(self):
        self.assertIn('server_settings', dir(self.client))
        n_settings = len(self.client.server_settings)
        self.assertGreater(n_settings, 0) 

    def test_hardware_id(self):
        self.assertIn('hardware_id', dir(self.client))
        self.assertIsInstance(self.client.hardware_id, str)


def get_credentials():
    CREDENTIAL_FILEPATH = os.path.join(os.path.expanduser('~'), 'credentials.ini')
    if os.path.exists(CREDENTIAL_FILEPATH):
        credentials = configparser.ConfigParser()
        credentials.read(CREDENTIAL_FILEPATH)
        username = credentials['DEFAULT']['username']
        password = credentials['DEFAULT']['password']
    else:
        import getpass
        username = input('username')
        password = getpass.getpass()
    return username, password

def run_login():

    username, password = get_credentials()
    client = Client()
    client.login(username, password)


if __name__ == '__main__':
    run_login()

