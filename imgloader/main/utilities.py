import os
from datetime import datetime

from django.conf import settings


def logger(message, mr_data):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    path = os.path.join(settings.BASE_DIR, f'error_log/{now}_{message}.txt')
    file = open(path, 'w')
    file.write(str(mr_data))
    file.close()
