import typer
import yaml
from pathlib import Path
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

app = typer.Typer()

@app.command()
def basic(input_filename: Path, output_filename: Path = typer.Option(None)):
    """
    Processes a file by converting each line to uppercase and writing it to an output file.
    
    :param input_filename: The name of the input file.
    :param output_filename: The name of the output file. If not provided, it will be input_filename.processed.
    """
    if output_filename is None:
        output_filename = input_filename.with_suffix('.processed')
    
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            processed_line = function_map['upper_case'](line)
            outfile.write(processed_line)

@app.command()
def dynamic(input_filename: Path, 
            output_filename: Path = typer.Option(None, "--output-filename", help="Output filename"),
            config_filename: Path = typer.Option(Path("pipeline.yaml"), "--config-filename", help="Configuration file for pipeline")):
    """
    Processes a file using a pipeline defined in a YAML configuration file.
    
    :param input_filename: The name of the input file.
    :param output_filename: The name of the output file. If not provided, it will be input_filename.processed.
    :param config_filename: The name of the YAML configuration file.
    """
    if output_filename is None:
        output_filename = input_filename.with_suffix('.processed')
    
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        with open(config_filename, 'r') as config_file:
            config = yaml.safe_load(config_file)
            pipeline = config.get('pipeline', [])
        
        for line in infile:
            for func_name in pipeline:
                func = function_map.get(func_name)
                if func:
                    line = func(line)
                else:
                    typer.echo(f"Function {func_name} not found.")
            outfile.write(line)
            

@app.command()
def process_stream(input_filename: Path, 
                   output_filename: Path = typer.Option(None, "--output-filename", help="Output filename"),
                   config_filename: Path = typer.Option(Path("pipeline.yaml"), "--config-filename", help="Configuration file for pipeline")):
    """
    Processes a file using a pipeline of stream functions defined in a YAML configuration file.
    
    :param input_filename: The name of the input file.
    :param output_filename: The name of the output file. If not provided, it will be input_filename.processed.
    :param config_filename: The name of the YAML configuration file.
    """
    if output_filename is None:
        output_filename = input_filename.with_suffix('.processed')
    
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        with open(config_filename, 'r') as config_file:
            config = yaml.safe_load(config_file)
            pipeline = config.get('pipeline', [])
        
        lines = infile.readlines()
        for func_name in pipeline:
            func = function_map.get(func_name)
            if func:
                lines = func(lines)
            else:
                typer.echo(f"Function {func_name} not found.")
        
        for line in lines:
            outfile.write(line)


if __name__ == "__main__":
    app()