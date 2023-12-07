import json
import os

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

# Example usage:
for ipynb_file in os.listdir('examples/azure'):
    if ipynb_file.endswith('.ipynb'):
        extract_code_from_ipynb(os.path.join('examples/azure', ipynb_file), 'examples/azure')
