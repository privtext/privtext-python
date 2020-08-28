
privtext usage docummntation
====================================

By default once the message is read by recepient it is deleted by the server. Commmand line options let you set different expiration rules too.

Usage
-----

Simple example

.. code-block:: console

    privtext "Hello world"

or

.. code-block:: console

    python -m privtext "Hello world"


the script returns a link of the following format

.. code-block:: console

    https://privtext.com/R8MnvR#BKWrZhG81


You don't have to open a browser to read the note:

.. code-block:: console

    privtext "https://privtext.com/R8MnvR#BKWrZhG81"

or

.. code-block:: console

    python -m privtext "https://privtext.com/R8MnvR#BKWrZhG81"

Privtext a file


.. code-block:: console

    privtext < file.txt

Will create a privtext link with contents of the file. Make sure the file is in utf-8 encoding. Also mind size limits

You may use the `-s` or `--split-lines` option when privtexting a file, this will split the files into lines and create a link for each line of text within the file. 

For example:

.. code-block:: console

    privtext -s < passwords.txt

will return a list of URLs, only per line.

At the moment a maximum  of 30 lines is accepted.

Troubleshooting
---------------

Sometimes the privtext utility cannot contact the privtext.com server. The solution is to revise the rules of your firewall and/or use a proxy to bypass the firewall.

