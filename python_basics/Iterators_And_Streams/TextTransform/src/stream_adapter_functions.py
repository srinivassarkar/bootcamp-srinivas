from typing import Callable, Iterator
from processing_functions import (
    upper_case, remove_stop_words, capitalize, fetch_geo_ip,
    lower_case, uk_to_us
)
from stream_functions import (
    number_the_lines, coalesce_empty_lines, break_lines
)

function_map = { 
    'upper_case': upper_case,  
    'remove_stop_words': remove_stop_words,
    'capitalize': capitalize,
    'fetch_geo_ip': fetch_geo_ip,
    'lower_case': lower_case,
    'uk_to_us': uk_to_us,
    'number_the_lines': number_the_lines,
    'coalesce_empty_lines': coalesce_empty_lines,
    'break_lines': break_lines
}



def string_to_stream_function(in_function: Callable[[str], str]) -> Callable[[Iterator[str]], Iterator[str]]:
    """
    Converts a string-processing function to a stream-processing function.
    
    :param in_function: The input string-processing function.
    :return: A stream-processing function.
    """
    def stream_function(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield in_function(line)
    return stream_function

# Example usage:
# stream_upper_case = string_to_stream_function(upper_case)
# for line in stream_upper_case(file_stream("example.txt")):
#     print(line)