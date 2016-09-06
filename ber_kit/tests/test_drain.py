#!/usr/bin/env python

import ber_kit
from ber_kit.commands import drain

import json
from test_data import DrainData

import mock

class ArgsMock(object):
    """
    Mock up the args-parser object
    """
    url = ''
    hosts = ''

    def __init__(self, url, hosts):
        self.url = url
        self.hosts = hosts

def test_single_drain():
    marathon_endpoint = 'http://marathon.com:1234'
    hosts = '1.2.3.4'

    # Mock setup
    args = ArgsMock(marathon_endpoint, hosts)

    # Create Mocks

    # Make the call
    # drain.main(args) #TODO e2e test

    # Assertions
    assert True == True
