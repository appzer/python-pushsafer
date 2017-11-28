# pushsafer 0.2
#
# Copyright (C) 2016  Kevin Siml <info@appzer.de>
# forked from https://github.com/Thibauth/python-pushover

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import time
import os

import requests

__all__ = ["init", "Client", "MessageRequest",
           "InitError"]

MESSAGE_URL = "https://www.pushsafer.com/api"

PRIVATEKEY = None


def init(privatekey):

    global PRIVATEKEY
    PRIVATEKEY = privatekey


class InitError(Exception):

    def __str__(self):
        return ("No privatekey provided. Init the pushsafer module by "
                "calling the init function")


class Request:

    def __init__(self, request_type, url, payload):
        if not PRIVATEKEY:
            raise InitError

        payload["k"] = PRIVATEKEY
        request = getattr(requests, request_type)(url, params=payload, verify=False)
        self.answer = request.json()

    def __str__(self):
        return str(self.answer)


class MessageRequest(Request):

    def __init__(self, payload):
        Request.__init__(self, "post", MESSAGE_URL, payload)


class Client:

    def __init__(self, device=None, privatekey=None):
        self.devices = []

    def send_message(self, message, title, device, icon, sound, vibration, url, urltitle, time2live, picture1, picture2, picture3):

        payload = {"m": message}
		
        if device:
            payload["d"] = device
			
        if icon:
            payload["i"] = icon

        if sound:
            payload["s"] = sound
			
        if vibration:
            payload["v"] = vibration
			
        if title:
            payload["t"] = title

        if url:
            payload["u"] = url

        if urltitle:
            payload["ut"] = urltitle

        if time2live:
            payload["l"] = time2live

        if picture1:
            payload["p"] = picture1

        if picture2:
            payload["p2"] = picture2

        if picture3:
            payload["p3"] = picture3

        return MessageRequest(payload)
