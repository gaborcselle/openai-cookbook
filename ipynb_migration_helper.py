import json
import os
import argparse

def extract_code_from_ipynb(ipynb_path, output_dir):
    with open(ipynb_path, 'r', encoding='utf-8') as file:
        notebook = json.load(file)

    base_name = os.path.splitext(os.path.basename(ipynb_path))[0]

    for index, cell in enumerate(notebook.get('cells', [])):
        if cell.get('cell_type') == 'code':
            code = ''.join(cell.get('source', []))
            cell_name = cell.get('metadata', {}).get('name', f'cell{index}')
            output_path = os.path.join(output_dir, f'{base_name}_{cell_name}.py')

            with open(output_path, 'w', encoding='utf-8') as code_file:
                code_file.write(code)

def extract_notebook_cells(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                extract_code_from_ipynb(os.path.join(root, file), root)

def reinsert_notebook_cells(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                base_name = os.path.splitext(os.path.basename(notebook_path))[0]

                with open(notebook_path, 'r+', encoding='utf-8') as notebook_file:
                    notebook = json.load(notebook_file)

                    for index, cell in enumerate(notebook.get('cells', [])):
                        if cell.get('cell_type') == 'code':
                            cell_name = cell.get('metadata', {}).get('name', f'cell{index}')
                            code_file_path = os.path.join(root, f'{base_name}_{cell_name}.py')

                            if os.path.exists(code_file_path):
                                with open(code_file_path, 'r', encoding='utf-8') as code_file:
                                    cell['source'] = code_file.readlines()

                    notebook_file.seek(0)
                    # notebooks include extra newline at the end
                    notebook_file.write(json.dumps(notebook, indent=1) + '\n')
                    notebook_file.truncate()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Jupyter Notebooks')
    parser.add_argument('directory', type=str, help='Directory to search for .ipynb files')
    parser.add_argument('--reinsert', action='store_true', help='Reinsert code cells into notebooks')
    args = parser.parse_args()

    if args.reinsert:
        reinsert_notebook_cells(args.directory)
    else:
        extract_notebook_cells(args.directory)
