#!/usr/local/bin/python

"""
ber-kit

Usage:
  ber-kit drain
  ber-kit undrain
  ber-kit -h | --help
  ber-kit --version

Options:
  -h --help                             Show this screen
  --version                             Show version

Examples:
  $ ber-kit drain --url http://marathon.example.com --hosts 172.31.37.92,172.31.35.101

Help:
  See https://bitbucket.org/connectedsolutions/ber-kit
"""

import sys
import importlib
import json
import time
import argparse
import requests
from inspect import getmembers, isclass

from . import __version__ as VERSION


def parse_args():
  """ Parses command line arguments. """

  # Create the main parser
  parser = argparse.ArgumentParser(description='Mesos Migration Kit')
  parser.set_defaults(which='drain')
  subparsers = parser.add_subparsers(help='', dest='subcommand')

  # Drain parser
  drain_parser = subparsers.add_parser('drain', help='do drain things')
  drain_parser.add_argument('--url', dest='url', type=str, help='Marathon URL (http://marathon.example.com)')
  drain_parser.add_argument('--hosts', dest='hosts', type=str, help='Hosts going to go for maintenance')

  # Undrain parser
  drain_parser = subparsers.add_parser('undrain', help='do undrain things')
  drain_parser.add_argument('--url', dest='url', type=str, help='Marathon URL (http://marathon.example.com)')
  drain_parser.add_argument('--hosts', dest='hosts', type=str, help='Hosts that have finished maintenance')

  # Return it
  args = parser.parse_args()
  return args

def main():
    """Main CLI entrypoint."""
    args = parse_args()

    from ber_kit.commands import drain, undrain
    eval("%s.main(%s)" % (args.subcommand, 'args'))
    #print "Importing and running [%s]..." % (args.subcommand)
