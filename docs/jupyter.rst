Jupyter tutorial
================

Installation
==============

Install

    $ virtualenv jupyter
    $ source ./jupyter/bin/activate
    $ pip install jupyter

Start your notebook saying::

    $ jupyter notebook

This will start a local notebook server. In my case, this was in url http://localhost:8888/?token=f1639d6df03110fdbbfb07bf7c29a9336156864ceb756862
You can then start creating a notebook interactively clicking on the ``New`` button on the top right.

In your jupyter notebook you can import and execute globally available code.

To interpret your notebook and convert it into a static html page do in the command line::

    $ jupyter nbconvert --to html Untitled4.ipynb

Useful Links
============

 - A complete tutorial with screenshots and everything: https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook 
 - the internal format of Jupyter notebooks: http://nbformat.readthedocs.io/en/latest/format_description.html
 - Best practices from an astrophysicist: https://www.svds.com/jupyter-notebook-best-practices-for-data-science/
 
 
 Notebook examples, to get some ideas:
   - Gallery of interesting notebooks: https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks
   - matplotlib: http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
   - Kaggle bulldozers: Basic cleaning of data: http://danielfrg.com/blog/2013/03/07/kaggle-bulldozers-basic-cleaning/
   - Python Data Science Handbook: https://github.com/jakevdp/PythonDataScienceHandbook