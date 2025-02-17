from typing import Iterator

def number_the_lines(lines: Iterator[str]) -> Iterator[str]:
    """
    Adds line numbers as prefixes to each line.
    
    :param lines: An iterator of strings.
    :yield: The next line with a line number prefix.
    """
    for i, line in enumerate(lines, start=1):
        yield f"{i}: {line}"

def coalesce_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    """
    Removes multiple empty lines and produces only one empty line.
    
    :param lines: An iterator of strings.
    :yield: The next line with multiple empty lines coalesced.
    """
    last_was_empty = False
    for line in lines:
        if line.strip() == "":
            if not last_was_empty:
                yield line
                last_was_empty = True
        else:
            yield line
            last_was_empty = False

def remove_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    """
    Removes any empty lines.
    
    :param lines: An iterator of strings.
    :yield: The next non-empty line.
    """
    for line in lines:
        if line.strip() != "":
            yield line

def remove_even_lines(lines: Iterator[str]) -> Iterator[str]:
    """
    Removes all the even-numbered lines.
    
    :param lines: An iterator of strings.
    :yield: The next line, skipping even-numbered lines.
    """
    for i, line in enumerate(lines, start=1):
        if i % 2 != 0:
            yield line

def break_lines(lines: Iterator[str]) -> Iterator[str]:
    """
    Breaks up a single long line into shorter lines (20 characters each).
    
    :param lines: An iterator of strings.
    :yield: The next line, broken into shorter lines.
    """
    for line in lines:
        while len(line) > 20:
            yield line[:20]
            line = line[20:]
        if line:
            yield line