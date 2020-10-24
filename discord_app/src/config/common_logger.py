import logging
import os

logfile_path = os.path.join(os.path.dirname(__file__), "../../logs")
logfile_path = os.path.normpath(logfile_path)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=logfile_path + '/app.log',
                    filemode='w')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

app_logger = logging.getLogger(__file__)

if __name__ == "__main__":
    pass