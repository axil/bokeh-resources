# bokeh-resources

Bokeh (https://bokeh.org/) Python plotting library has two main modes for serving static content: CDN and inline.
  
   - 'cdn' (=content distribution network) mode needs internet connection every time you open the notebook
   
   - 'inline' mode increases the size of ipynb files by 6Mb

`bokeh-resources` is a jupyter extension that makes jupyter serve bokeh files locally. 

It keeps the size of ipynb files small and works offline as well.
 
## Installation: 

``` bash
pip install bokeh-resources
python -m bokeh-resources.install
```
    
Or alternatively

``` bash
git clone https://github.com/axil/bokeh-resources
cd bokeh_resources
python install.py
```
    
This will install the extension to jupyter and to create the symlink (see 'Updating' below)

After this the package itself can be safely uninstalled (`pip uninstall bokeh-resources`).

To uninstall the extension run
    
    jupyter nbextensions uninstall bokeh_resources


## Usage:

In bokehlab:
  
``` python
%bokehlab local
```
    
In bokeh:

``` python
from bokeh.io import output_notebook
from bokeh.resources import Resources
output_notebook(Resources('server', root_url='/nbextensions/bokeh_resources'))
```

## Updating:

Serving is performed through a symbolic link (or a directory junction on Windows). 

This means that it is resilient to bokeh updates.

(= the extension does not need to be updated when `bokeh` is updated to the next version).
