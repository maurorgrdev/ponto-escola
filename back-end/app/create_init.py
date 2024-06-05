import os
import shutil

def create_init_files(directory):
    for root, dirs, files in os.walk(directory):
        if root.endswith('__pycache__'):
            continue  # Ignora a pasta __pycache__

        for d in dirs:
            if d != '__pycache__':  # Verifica se o diretório não é __pycache__
                init_file = os.path.join(root, d, '__init__.py')
                if not os.path.exists(init_file):
                    with open(init_file, 'w') as f:
                        pass  # Cria um arquivo __init__.py vazio
                    print(f'Created {init_file}')
                else:
                    print(f'{init_file} already exists')

if __name__ == '__main__':
    create_init_files(os.path.dirname(os.path.abspath(__file__)))