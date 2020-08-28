Installation
============

via pip
--------

.. code-block:: console
    pip install privtext


or


.. code-block:: console
    python -m pip install privtext

Python is a popular programming language and usually included in all linux distributions. Pip is a python package manager and is included in all latest python versions starting from version 3.4. If you do not  have python or pip installed on your system, google the pip installation instructions for your system, although most likely it is already installed.

via setup.py
--------

We don’t recommend it, but officially support this method. One should prefer using an installer that supports PEP-517 interface, such as pip with latest version. That being said you might be able to install a package via this method with calling the install command:

.. code-block:: console
    git clone https://github.com/privtext/privtext-python
    cd privtext-python
    python ./setup.py install

Source code
--------

The latest working version of assembly you can download from the official GitHub repository by link:

.. code-block:: console
    pip install git+https://github.com/privtext/privtext-python

or

.. code-block:: console
    git clone https://github.com/privtext/privtext-python


Compatibility
--------

privtext works with the following Python interpreter implementations:

    -  `CPython <https://www.python.org/>` versions 2.7.x, 3.4.x+
    -  `PyPy <https://pypy.org/>` 2.7 and 3.4+.

This means privtext works on the latest patch version of each of these minor versions. Previous patch versions are supported on a best effort approach.

CPython is shipped in multiple forms, and each OS repackages it, often applying some customization along the way. Therefore we cannot say universally that we support all platforms.

Linux
--------

    - installations from `python.org <https://www.python.org/downloads/>`_
    - Ubuntu 16.04+ (both upstream and `deadsnakes <https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa>`_ builds)
    - Fedora
    - RHEL and CentOS
    - OpenSuse
    - Arch Linux

macOS
--------

In case of macOS we support:

    - installations from `python.org <https://www.python.org/downloads/>`_
    - python versions installed via `brew <https://docs.brew.sh/Homebrew-and-Python>`_ (both older python2.7 and python3)
    - Python 3 part of XCode (Python framework - ``/Library/Frameworks/Python3.framework/``)
    - Python 2 part of the OS (``/System/Library/Frameworks/Python.framework/Versions/``)

Windows
--------

    - Installations from `python.org <https://www.python.org/downloads/>`_
    - Windows Store Python `3.7+ <https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l>`_


