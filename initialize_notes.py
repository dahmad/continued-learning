from glob import glob
import logging
from pathlib import Path
from shared import *


# set-up
logging.basicConfig(level=logging.INFO)

for file_path_origin in file_paths_origin:
    file_path_target = file_path_origin.replace(directory_origin, directory_target).replace(file_format_origin, file_format_target)
    if file_path_target in file_paths_target:
        logging.info(f"Notes file \"{file_path_target}\" already exists for source material \"{file_path_origin}\"")
    else:
        logging.info(f"Creating file \"{file_path_target}\" for source material \"{file_path_origin}\"")
        Path(file_path_target).touch()