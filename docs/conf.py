# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# from sphinx.builders.html import StandaloneHTMLBuilder
import subprocess
# import os

# Doxygen
subprocess.call('doxygen Doxyfile.in', shell=True)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WiThrottleProtocol'
copyright = '2023 - David Zuhn, Luca Dentella, Peter Akers'
author = 'Peter Akers'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "sphinx.ext.githubpages",
  # 'sphinxcontrib.spelling',
  'sphinx_rtd_dark_mode',
  'breathe'
]

autosectionlabel_prefix_document = True

# Don't make dark mode the user default
default_dark_mode = False

spelling_lang = 'en_UK'
tokenizer_lang = 'en_UK'
spelling_word_list_filename = ['spelling_wordlist.txt']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

highlight_language = 'c++'

numfig = True

numfig_format = {'figure': 'Figure %s'}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_logo = "./_static/images/withrottleprotocol-library.png"

html_favicon = "./_static/images/favicon.ico"

html_theme_options = {
    'style_nav_header_background': 'white',
    'logo_only': True,
    # Toc options
    'includehidden': True,
    'titles_only': False,
    # 'titles_only': True,
    'collapse_navigation': False,
    # 'navigation_depth': 3,
    'navigation_depth': -1,
    'analytics_id': 'G-L5X0KNBF0W',
}

html_context = {
    'display_github': True,
    'github_user': 'flash62au',
    'github_repo': 'WiThrottleProtocol',
    'github_version': 'sphinx/docs/',
}

html_css_files = [
    'css/withrottleprotocol_theme.css',
    'css/sphinx_design_overrides.css',
]

# Sphinx sitemap
# html_baseurl = 'https://flash62au.github.io/WiThrottleProtocol/'
# html_extra_path = [
#  'robots.txt',
# ]

# -- Breathe configuration -------------------------------------------------

breathe_projects = {
  "WiThrottleProtocol": "_build/xml/"
}
breathe_default_project = "WiThrottleProtocol"
breathe_default_members = ()
