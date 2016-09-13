# pushsafer 0.1
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
from ConfigParser import RawConfigParser, NoSectionError
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import os

import requests

__all__ = ["init", "Client", "MessageRequest",
           "InitError"]

MESSAGE_URL = "https://www.pushsafer.com/api"

PRIVATEKEY = None


def init(privatekey):
    """Initialize the module by setting the application privatekey which will be
    used to send messages.
    """
    global PRIVATEKEY
    PRIVATEKEY = privatekey


class InitError(Exception):
    """Exception which is raised when trying to send a message before
    initializing the module.
    """

    def __str__(self):
        return ("No privatekey provided. Init the pushsafer module by "
                "calling the init function")


class Request:
    """Base class to send a request to the Pushsafer server"""

    def __init__(self, request_type, url, payload):
        if not PRIVATEKEY:
            raise InitError

        payload["privatekey"] = PRIVATEKEY
        request = getattr(requests, request_type)(url, params=payload)
        self.answer = request.json()

    def __str__(self):
        return str(self.answer)


class MessageRequest(Request):
    """Class representing a message request to the Pushsafer API. You do not
    need to create them yourself, but the :func:`Client.send_message` function
    returns :class:`MessageRequest` objects if you need to inspect the requests
    after they have been answered by the Pushsafer server.

    The :attr:`answer` attribute contains a JSON representation of the answer
    made by the Pushsafer API. In the case where you have sent a message with
    a priority of 2, you can poll the status of the notification with the
    :func:`poll` function.
    """

    def __init__(self, payload):
        Request.__init__(self, "post", MESSAGE_URL, payload)


class Client:
    """This is the main class of the module. It represents a specific Pushsafer
    user to whom messages will be sent when calling the :func:`send_message`
    method.

    * ``device``: if provided further ties the Client object to the specified
      device.
    * ``privatekey``: if provided and the module wasn't previously initialized,
      call the :func:`init` function to initialize it.
    * ``config_path``: configuration file from which to import unprovided
      parameters. See Configuration_.
    * ``profile``: section of the configuration file to import parameters from.
    """

    def __init__(self, device=None, privatekey=None,
                 config_path="~/.pushsaferrc", profile="Default"):
        params = _get_config(profile, config_path, privatekey, device)
        self.device = params["d"]
        self.devices = []

    def send_message(self, message, **kwords):
        """Send a message to the user. It is possible to specify additional
        properties of the message by passing keyword arguments. The list of
        valid keywords is ``title, sound, icon, vibration,
        device`` which are described in the
        Pushsafer API documentation.

        This method returns a :class:`MessageRequest` object.
        """
        valid_keywords = ["title", "sound", "icon",
                          "vibration", "device"]

        payload = {"m": message}
        if self.device:
            payload["d"] = self.device
			
        if self.icon:
            payload["i"] = self.icon

        if self.sound:
            payload["s"] = self.sound
			
		if self.vibration:
            payload["v"] = self.vibration
			
        if self.title:
            payload["t"] = self.title

        for key, value in kwords.iteritems():
            if key not in valid_keywords:
                raise ValueError("{0}: invalid message parameter".format(key))

            payload[key] = value

        return MessageRequest(payload)


def _get_config(profile='Default', config_path='~/.pushsaferrc',
                privatekey=None, device=None):
    config_path = os.path.expanduser(config_path)
    config = RawConfigParser()
    config.read(config_path)
    params = {"k": None, "d": None}
    try:
        params.update(dict(config.items(profile)))
    except NoSectionError:
        pass
    if privatekey:
        params["k"] = privatekey
    if device:
        params["d"] = device

    if not PRIVATEKEY:
        init(params["k"])
        if not PRIVATEKEY:
            raise InitError

    return params


def main():
    parser = ArgumentParser(description="Send a message to pushsafer.",
                            formatter_class=RawDescriptionHelpFormatter,
                            epilog="""
For more details and bug reports, see: https://github.com/appzer/pushsafer-python""")
    parser.add_argument("--privatekey", help="Pushsafer private key")
    parser.add_argument("message", help="message to send")
    parser.add_argument("--title", "-t", help="message title")
	parser.add_argument("--icon", "-i", help="message icon")
	parser.add_argument("--sound", "-s", help="message sound")
	parser.add_argument("--vibration", "-v", help="message vibration")
    parser.add_argument("-c", "--config", help="configuration file\
                        (default: ~/.pushsaferrc)", default="~/.pushsaferrc")
    parser.add_argument("--profile", help="profile to read in the\
                        configuration file (default: Default)",
                        default="Default")
    parser.add_argument("--version", "-v", action="version",
                        help="output version information and exit",
                        version="""
%(prog)s 0.1
Copyright (C) 2016 Kevin Siml <info@appzer.de>
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""")

    args = parser.parse_args()
    Client(None, args.api_token, args.config,
           args.profile).send_message(args.message, title=args.title,
                                      timestamp=True)

if __name__ == "__main__":
    main()
