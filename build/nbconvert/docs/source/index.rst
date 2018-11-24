=============================================
nbconvert: Convert Notebooks to other formats
=============================================

Using ``nbconvert`` enables:

    - **presentation** of information in familiar formats, such as PDF.
    - **publishing** of research using LaTeX and opens the door for embedding
      notebooks in papers.
    - **collaboration** with others who may not use the notebook in their
      work.
    - **sharing** contents with many people via the web using HTML.

Overall, notebook conversion and the ``nbconvert`` tool give scientists and
researchers the flexibility to deliver information in a timely way across
different formats.

Primarily, the ``nbconvert`` tool allows you to convert a Jupyter ``.ipynb``
notebook document file into another static format including HTML, LaTeX, PDF,
Markdown, reStructuredText, and more. ``nbconvert`` can also add productivity
to your workflow when used to execute notebooks programmatically.

If used as a Python library (``import nbconvert``), ``nbconvert`` adds
notebook conversion within a project. For example, ``nbconvert`` is used to
implement the "Download as" feature within the Jupyter Notebook web
application. When used as a command line tool (invoked as
``jupyter nbconvert ...``), users can conveniently convert just one or a
batch of notebook files to another format.


**Contents:**

.. toctree::
   :maxdepth: 2
   :caption: User Documentation

   install
   usage
   nbconvert_library
   latex_citations
   execute_api

.. toctree::
   :maxdepth: 2
   :caption: Configuration

   config_options
   customizing
   external_exporters

.. toctree::
   :maxdepth: 2
   :caption: Developer Documentation

   architecture
   api/index

.. toctree::
   :maxdepth: 2
   :caption: About nbconvert

   changelog

.. toctree::
   :maxdepth: 1
   :caption: Questions? Suggestions?

   Jupyter mailing list <https://groups.google.com/forum/#!forum/jupyter>
   Jupyter website <https://jupyter.org>
   Stack Overflow - Jupyter <https://stackoverflow.com/questions/tagged/jupyter>
   Stack Overflow - Jupyter-notebook <https://stackoverflow.com/questions/tagged/jupyter-notebook>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
