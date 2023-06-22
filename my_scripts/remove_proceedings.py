import os
import click
import logging
import yaml
import shutil

def get_yaml_from_index_file(f):   
    with open(f, 'r') as file:
        text = file.read()
    
    start_delimiter = '---'
    end_delimiter = '---'

    start_index = text.find(start_delimiter)
    end_index = text.find(end_delimiter, start_index + len(start_delimiter))

    if start_index == -1 or end_index == -1:
        logging.warning(f"No YAML front matter found in file {f}")
        return None

    yaml_text = text[start_index + len(start_delimiter):end_index].strip()

    try:
        yaml_data = yaml.safe_load(yaml_text)
        return yaml_data
    except yaml.YAMLError as e:
        logging.warning(f"Error parsing YAML in file {f}")
        return None


def find_directories(folder_path):
    directories = []
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            directories.append(dir_path)
    return directories

def remove_if_not_author(folder_path):
    for directory in find_directories(folder_path):
        index_md_path = os.path.join(directory, 'index.md')
        if os.path.isfile(index_md_path):
            data = get_yaml_from_index_file(index_md_path)
            if 'Jacopo Mauro' not in data['authors']:
                shutil.rmtree(directory)
                #logging.info(data)
                logging.info(f'Removing the folder {directory} since not foudn in authors. Title was {data["title"]}')

        else:
            logging.warning(f"No index.md found in {directory}")


def copy_pdf_files(pdfs_path, dirs_path):
    for directory in [x for x in os.listdir(dirs_path) if os.path.isdir(os.path.join(dirs_path, x))]:
        pdf = os.path.join(pdfs_path, directory + '.pdf')
        if os.path.exists(pdf):
            shutil.copy(pdf, os.path.join(dirs_path, directory))
            logging.debug(f"Copied pdf '{pdf}' into '{directory}'")
        else:
            logging.warning(f"No pdf file found matching directory {directory}")



@click.command()
@click.argument('webpubsFolder', default='../content/publication' , type=click.Path(exists=True),)
@click.argument('pdfFolder', default='../original_papers', type=click.Path(exists=True))
@click.option('--verbose', '-v', count=True, help='Increase verbosity (can be used multiple times)')
def process_pubs(webpubsfolder, pdffolder, verbose):
    log_level = logging.WARNING  # Default log level
    if verbose == 1:
        log_level = logging.INFO
    elif verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level, format='%(message)s')

    webpubsfolder = os.path.abspath(webpubsfolder)
    pdffolder = os.path.abspath(pdffolder)
    remove_if_not_author(webpubsfolder)
    copy_pdf_files(pdffolder, webpubsfolder)

if __name__ == '__main__':
    process_pubs()