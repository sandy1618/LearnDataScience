# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Learn Data-Science'
copyright = '2022, Sandeep'
author = 'Sandeep'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
html_theme = "pydata_sphinx_theme"

html_title = 'Learn DataScience'
# html_short_title = 'Learn Python'
# html_logo = "_static/logo_passion.jpg"

html_theme_options = {
  "show_toc_level": 1,
  "show_nav_level": 4,
  "navbar_end": ["navbar-icon-links.html", "search-field.html"],
  "search_bar_text": "Search here...",
  "page_sidebar_items": ["page-toc", "edit-this-page"],
  # "left_sidebar_end": ["sidebar-ethical-ads"],
  "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sandy1618/LearnDataScience",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        },
       
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/sandeep-kumar-nayak-48085865/",
            "icon": "fab fa-linkedin",
            "type": "fontawesome",
            # The default for `type` is `fontawesome` so it is not actually required in any of the above examples as it is shown here
        },
    ],
}

html_sidebars = {
    "**": ["search-field.html", "sidebar-nav-bs.html", "sidebar-ethical-ads.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'IPython.sphinxext.ipython_console_highlighting',
]
# Upgrade ipython 
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'furo'

# source_suffix = ['.rst', '.ipynb']
nbsphinx_allow_errors = True