import sys
from src.logger import logging


def error_message_details(error,error_details:sys):
        
        _,_,exe_tb=error_details.exc_info()

        file_name=exe_tb.tb_frame.f_code.co_filename

        error_message="Error occured in python script name [{0}] line number is [{1}] error message [{2}]".format()

        file_name,exe_tb.tb_lineno,str(error)

        return error_message



class CustomException(Exception):
            
            def __init__(self, error_message,error_details: sys):
                    super().__init__(error_message)


            def __str__(self):
                    return self.error_message
            
