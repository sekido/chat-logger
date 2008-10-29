"""Skype Chat Logger
"""
__version__ = "0.01"
__date__    = "2008-10-29"
__author__  = "Ryosuke SEKIDO <ryosuke@sekido.info>"
__credits__ = "Copyright (c) 2008 Ryosuke SEKIDO"
__license__ = "Creative Commons Attributes 2.1 Japan"


# import libraries
import yaml


class ChatLogger:
    """ChatLogger main class
    """

    config_file = u"../etc/chat-logger.config.yml"

    def __init__(self, config_file = None):
        """Constractor

        @type config_file: Unicode
        @param config_file: Path for config file
        """

        # reset config file path
        if config_file is not None:
            self.config_file = config_file

        # load config file
        try:
            self.load_config_file()
        except IOError:
            pass

    def __del__(self):
        """Destractor
        """
        pass

    def load_config_file(self):
        """Load config file
        """

        # read file
        string = file(config_file).read()
        string = string.decode('utf8')

        # parse YAML
        config = yaml.load(string)


# vim: tw=0 ts=4 sw=4 sts=4 expandtab
