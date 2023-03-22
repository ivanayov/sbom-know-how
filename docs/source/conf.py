# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SBOM Know How'
copyright = '2023, VMware Inc.'
author = 'Ivana Atanasova'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser','sphinx.ext.autosectionlabel','sphinxcontrib.plantuml','sphinx_needs']

templates_path = ['_templates']
exclude_patterns = []

needs_types = [dict(directive="tool-data", title="Tool data", prefix="TOOL", color="", style="node")]
needs_extra_options = ['tool', 'generation', 'consumption', 'transformation', 'vulnerabilty_scanning', 'licensing', 'cyclonedx', 'spdx', 'sbom_quality']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'classic'
html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]