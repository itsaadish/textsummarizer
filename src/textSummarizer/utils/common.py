import sys
import os

def error_message_detail(error,err_detail:sys):
   _,_,exc_tb =  err_detail.exc_info()
   file_name = exc_tb.tb_frame.f_code.co_filename
   error_message = f'error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]'

   return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys) -> None:
        super.__init__(error_message)

        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self) -> str:
        return self.error_message
    
    import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    