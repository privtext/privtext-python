Установка
============

через pip
--------

Вы можете установить его в самом глобальном интерпретаторе Python (возможно, как пользовательский пакет с помощью флага ``--user``). Будьте осторожны, если установщик Python обрабатывается вашей операционной системой или другим менеджером пакетов. pip может не взаимодействовать с этими инструментами и может оставить вашу систему в несогласованном состоянии. Обратите внимание: если вы пойдете по этому пути, вам необходимо убедиться, что pip обновлен до последней версии:

.. code-block:: console
    python -m pip install privtext
    python -m privtext


через setup.py
--------

Мы не рекомендуем, но официально поддерживаем этот метод. Лучше использовать установщик, поддерживающий интерфейс PEP-517, например pip с последней версией. При этом вы можете установить пакет с помощью этого метода, вызвав команду установки:

.. code-block:: console
    python ./setup.py install

Исходный код
--------

Последнюю рабочую версию исходной зборки всегда можно скачать на официальном репозитории GitHub по ссылке:

.. code-block:: console
    pip install git+https://github.com/privtext/privtext-python

или

.. code-block:: console
    git clone https://github.com/privtext/privtext-python


Совместимость Python и ОС
--------

privtext работает со следующими реализациями интерпретатора Python:

    -  `CPython <https://www.python.org/>` версий 2.7.x, 3.4.x+
    -  `PyPy <https://pypy.org/>` 2.7 and 3.4+.

Это означает, что privtext работает с последней версией исправления каждой из этих дополнительных версий. Предыдущие версии исправлений поддерживаются по принципу «максимальных усилий».




CPython поставляется в нескольких формах, и каждая ОС переупаковывает его, часто применяя некоторую индивидуальную настройку. Поэтому мы не можем универсально сказать, что мы поддерживаем все платформы, а скорее указать те, на которых мы проводим тестирование. В случае тех, которые здесь не указаны, поддержка неизвестна, но, скорее всего, будет работать. Если вы обнаружите какие-либо случаи, пожалуйста, отправьте запрос функции в нашем трекере проблем.

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

В случае macOS мы поддерживаем:

    - installations from `python.org <https://www.python.org/downloads/>`_
    - python versions installed via `brew <https://docs.brew.sh/Homebrew-and-Python>`_ (both older python2.7 and python3)
    - Python 3 part of XCode (Python framework - ``/Library/Frameworks/Python3.framework/``)
    - Python 2 part of the OS (``/System/Library/Frameworks/Python.framework/Versions/``)

Windows
--------

    - Установки с `python.org <https://www.python.org/downloads/>`_
    - Windows Store Python `3.7+ <https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l>`_

Варианты упаковки
--------

    - Обычный вариант (файловая структура взята с python.org).
