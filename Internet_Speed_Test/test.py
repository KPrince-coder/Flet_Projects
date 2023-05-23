"""Date: Tuesday, May 23, 2023"""
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import speedtest
# def log
logging.basicConfig(level=logging.DEBUG, filename=f'{__file__}_logs.log')

dir_path = os.path.join(os.path.dirname(
    __file__), 'tests_container')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

file_path = os.path.join(dir_path, 'tests.log')

logger = logging.getLogger(__name__)

file_handler = TimedRotatingFileHandler(
    filename=file_path,
    when='midnight',
    delay=True,
    backupCount=20

)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(
    logging.Formatter(
        '{asctime}:{levelname}:{name}:{message}',
        style='{',
        datefmt='%b-%d-%Y %H:%M:%S'
    )
)


logger.addHandler(file_handler)


def run_speed_test():
    """Converts download and upload speeds to Megabit per second (Mbps) and logs the result of the speed test including the download speed, upload speed, country,country code and city.


    Returns:
        speedtest: download speed, upload speed, country,country code and city
    """
    try:
        st = speedtest.Speedtest()

        download_speed = st.download() / 1_000_000  # in Mbps
        upload_speed = st.upload() / 1_000_000  # in Mbps

        best_server = st.get_best_server()
        country = best_server['country']
        city = best_server['name']
        country_code = best_server['cc']
        logger.info(
            f'Download Speed: {download_speed:.2f} Mbps: Upload Speed: {upload_speed:.2f} Mbps')

        return download_speed, upload_speed, country_code, city, country

    except speedtest.SpeedtestException as e:
        logger.error(f'Speed test failed: {e}')
        return None, None, None, None, None


if __name__ == '__main__':
    logger.info('hello what\'s up')
