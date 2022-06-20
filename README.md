# bokeh-resources

Bokeh (https://bokeh.org/) Python plotting library has two main modes for serving static content: CDN and inline.
  
   - 'CDN' mode needs internet connection every time you open the notebook
   
   - 'inline' mode increases size of ipynb files by 6Mb

This extension allows to serve bokeh files locally thus keeping the size of ipynb files small and not require 
internet connection.
 
## Installation: 

    pip install bokeh-resources
    
Then run `install.py` to install the extension to jupyter and to create the symlink (see 'Updating' below)

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

The extension creates a symlink (or a directory junction on Windows). This means that it is resilient to bokeh updates
(= the extension does not need to be updated when the bokeh is updated to next version).
