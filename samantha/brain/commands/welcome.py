#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""


from samantha.brain.commands.command import Command


__all__ = ['Welcome']


class Welcome(Command):
    """
    Command class for Welcome messages
    """
    def __init__(self, text, channel):
        self.text = text
        self.channel = channel
        super(Welcome, self).__init__()

    def execute(self):
        """
        Command Executioner
        """
        return self.sender.send_text(
                text=self.text, channel=self.channel)