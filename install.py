import os
from pathlib import Path
import bokeh
from notebook.nbextensions import install_nbextension

alias = Path(install_nbextension('bokeh_resources')) / 'static'
target = Path(bokeh.__file__).parent / 'server' / 'static'
os.system(f'mklink /j {alias} {target}')