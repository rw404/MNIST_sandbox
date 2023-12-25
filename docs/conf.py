# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys


sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../.."))

project = "MNIST sandbox, mlops CS course, 2023"
copyright = "2023, <unk>"
author = "<unk>"

# The short X.Y version
version = "0.0.1"
# The full version, including alpha/beta/rc tags
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# autodoc_inherit_docstrings = False

# Disable docstring inheritance
autodoc_inherit_docstrings = False

# Show type hints in the description
autodoc_typehints = "description"

# Add parameter types if the parameter is documented in the docstring
autodoc_typehints_description_target = "documented_params"

autodoc_mock_imports = [
    "torch",
    "torch.nn",
    "torch.nn.Module",
    "pytorch_lightning",
    "pl",
    "pl.LightningModule",
    "torch.nn.modules.module.Module",
]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.imgmath",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "numpydoc",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]
