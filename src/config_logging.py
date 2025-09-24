import logging
import os

# Настройка логирования для модуля masks
logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG)

formatter_masks = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler_masks = logging.FileHandler('logs/masks.log', mode='w')
file_handler_masks.setFormatter(formatter_masks)

logger_masks.addHandler(file_handler_masks)

# Настройка логирования для модуля utils
logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)

formatter_utils = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler_utils = logging.FileHandler('logs/utils.log', mode='w')
file_handler_utils.setFormatter(formatter_utils)

logger_utils.addHandler(file_handler_utils)
