import logging
import os
import traceback


class LoggerConnector:
    @staticmethod
    def get_logger(name):

        level = logging.DEBUG

        try:
            logger = logging.getLogger(name)
            log_file = os.path.join(os.getenv("FM_APP_LOGDIR", '../logs/'), str(name) + '.log')

            # if file not exists
            if not os.path.exists(log_file):
                d = os.path.dirname(log_file)
                if not os.path.exists(d):
                    os.makedirs(d)
                f = open(log_file, 'w+')
                f.close()

            hdlr = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                '%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] -- %(name)s -- %(message)s')
            hdlr.setFormatter(formatter)
            logger.addHandler(hdlr)

            logger.setLevel(level)
            return logger

        except Exception as e:
            msg = "Unable to create logger " + name + str(e) + "TRACE = " + traceback.print_exc(e)
            return msg
