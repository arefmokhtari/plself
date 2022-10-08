import logging
import colorlog

underline_on = "\x1b[4m"
underline_off = "\x1b[24m"

SUCCESS = 5
logging.addLevelName(SUCCESS, 'SUCCESS')
colorlog.ColoredFormatter.default_time_format = '%H:%M:%S'
colorlog.ColoredFormatter.default_msec_format = ''

formatter = colorlog.LevelFormatter(fmt={
    "DEBUG": f"%(log_color)s[%(asctime)s \x1b[37m{underline_on}%(levelname)s{underline_off}%(log_color)s] %(name)s: %(message)s (%(module)s:%(lineno)d)",
    "INFO": f"%(log_color)s[%(asctime)s \x1b[37m{underline_on}%(levelname)s{underline_off}%(log_color)s] %(name)s: %(message)s",
    "WARNING": f"%(log_color)s[%(asctime)s \x1b[37m{underline_on}%(levelname)s{underline_off}%(log_color)s] %(name)s: %(message)s (%(module)s:%(lineno)d)",
    "ERROR": f"%(log_color)s[%(asctime)s \x1b[37m{underline_on}%(levelname)s{underline_off}%(log_color)s] %(name)s: %(message)s (%(module)s:%(lineno)d)",
    "CRITICAL": f"%(log_color)s[%(asctime)s \x1b[37m{underline_on}%(levelname)s{underline_off}%(log_color)s] %(name)s: %(message)s (%(module)s:%(lineno)d)",
    "SUCCESS": f"%(log_color)s[%(asctime)s \x1b[37m{underline_on}%(levelname)s{underline_off}%(log_color)s] %(name)s: %(message)s"
},
    log_colors={'SUCCESS': 'green', 'INFO': 'light_blue', 'DEBUG': 'cyan',
                'WARNING': 'yellow', 'ERROR': 'red',
                'CRITICAL': 'red'}, reset=True)
handler = logging.StreamHandler()
handler.setFormatter(formatter)


class Logging(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        self.addHandler(handler)
        self.setLevel(level)
        self.success = self.success
        self.SUCCESS = SUCCESS

    def success(self, msg: str, *args, **kwargs):
        if self.isEnabledFor(self.SUCCESS):
            self._log(self.SUCCESS, msg, args, **kwargs)
