# SpinxTutorial
Install [mini-conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) for linux as conda env is better suited to install packages such as pandoc. 
- conda config --set auto_activate_base false (__deactivating base is autocall is good)
- conda env create -f readthedocs-environment.yml
- conda activate <environment_name>
- conda deactivate
- conda env update -f readthedocs-environment.yml
### For Jupyther Notebooks
pip install nbsphinx


### Links for references . 
- [Using conda build config](https://docs.readthedocs.io/en/stable/guides/conda.html)
- [ Building Jupyter notebook html by using nbsphinx and conda install pandoc (**Only works with conda and not pip**) ](https://jeanbilheux.pages.ornl.gov/post/convert_notebooks_to_html_pages/ )

### Adding .venv python virtual environment file 
-to save unwanted errors for other repository deriving out from this base repo. 
