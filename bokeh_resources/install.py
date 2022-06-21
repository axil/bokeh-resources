import os
import sys
from pathlib import Path
import bokeh
from notebook.nbextensions import install_nbextension

alias = Path(install_nbextension('bokeh_resources')) / 'static'
target = Path(bokeh.__file__).parent / 'server' / 'static'
if sys.platform == 'win32':
    os.system(f'mklink /j {alias} {target}')
else:
    alias.symlink_to(target)