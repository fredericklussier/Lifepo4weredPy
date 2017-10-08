Lifepo4weredPyWrapper
=====================

A wrapper to enable lifepo4wered SO library to Python.
reference: http://lifepo4wered.com/lifepo4wered-pi3.html

Using the Raspbery Pi zero in many projects, I found this product
very usefull. I adopted so to help my python colleagues, I design this. 

You can find the documentation of the lifepo4wered product:
http://lifepo4wered.com/files/LiFePO4wered-Pi3-Product-Brief.pdf.

Status
------
In development.

Installation
------------
If you want to use this wrapper, you need:
1- a lifepo4wered-pi3 as well as a Raspeberry Pi3 ;-)
2- download and build the driver (http://lifepo4wered.com/lifepo4wered-pi3.html)
3- download this wrapper
4- In lifepo4weredSO.py file change the path of the liblifepo4wered.so where you build it.

To dowload and install the LiFePO4wered-Pi drivers and CLI applications,
please read https://github.com/xorbit/LiFePO4wered-Pi.

To download or clone this wrapper, please read https://help.github.com/articles/cloning-a-repository/

.. code-block:: batch

    $ git clone https://github.com/fredericklussier/ObservablePy.git

Usage
-----

.. code-block:: python

    import lifepo4weredPy
    baterryVoltage = read(lifepo4weredEnum.VBAT)

Detail
------

Read
~~~~
To read data from the lifepo4wered.

.. code-block:: python

    read(what)

* what (lifepo4weredEnum): The information to read.
* return (int): the information.
* raise (ValueError): if information is not a lifepo4weredEnum member.
* raise (RuntimeError): if the information is not read access.

.. code-block:: python

    from Lifepo4weredPyWrapper import lifepo4weredEnum, read
    baterryVoltage = read(lifepo4weredEnum.VBAT)

Write
~~~~~
To write data to the lifepo4wered.

.. code-block:: python

    write(what, value)

* what (lifepo4weredEnum): The information name to write.
* value (int): the value to write.
* return (int): the written value.
* raise (ValueError): if information is not a lifepo4weredEnum member.
* raise (RuntimeError): if the information is not read access.
* raise (TypeError): if value is not an integer.

.. code-block:: python

    from Lifepo4weredPyWrapper import lifepo4weredEnum, read
    baterryVoltage = write(lifepo4weredEnum.LED_STATE, 2) # LED pulsing

canRead
~~~~~~~
Mention if the program is allowed to read the information.

.. code-block:: python

    canRead(what)

* what (lifepo4weredEnum): The information name.
* return (bool): True if you can read, otherwise False.
* raise (ValueError): if information is not a lifepo4weredEnum member.

.. code-block:: python

    from Lifepo4weredPyWrapper import lifepo4weredEnum, read
    if canRead(lifepo4weredEnum.LED_STATE):
        do()

canWrite
~~~~~~~~
More important, this function mention if the program is allowed to write the information.

.. code-block:: python

    canWrite(what)

* what (lifepo4weredEnum): The information name.
* return (bool): True if you can write, otherwise False.
* raise (ValueError): if information is not a lifepo4weredEnum member.

.. code-block:: python

    from Lifepo4weredPyWrapper import lifepo4weredEnum, read
    if canWrite(lifepo4weredEnum.LED_STATE):
        do()


lifepo4wered variables
~~~~~~~~~~~~~~~~~~~~~~
list of elements accessible.
please read section Low level I2C register specification
 of http://lifepo4wered.com/files/LiFePO4wered-Pi3-Product-Brief.pdf

.. code-block:: python

    class lifepo4weredEnum(Enum):
        I2C_REG_VER = 0
        I2C_ADDRESS = 1
        LED_STATE = 2
        TOUCH_STATE = 3
        TOUCH_CAP_CYCLES = 4
        TOUCH_THRESHOLD = 5
        TOUCH_HYSTERESIS = 6
        DCO_RSEL = 7
        DCO_DCOMOD = 8
        VIN = 9
        VBAT = 10
        VOUT = 11
        VBAT_MIN = 12 
        VBAT_SHDN = 13
        VBAT_BOOT = 14
        VOUT_MAX = 15
        VIN_THRESHOLD = 16
        VOFFSET_ADC = 17
        AUTO_BOOT = 18
        WAKE_TIME = 19
        SHDN_DELAY = 20
        AUTO_SHDN_TIME = 21
        PI_RUNNING = 22
        CFG_WRITE = 23

lifepo4wered defines
~~~~~~~~~~~~~~~~~~~~
list of defines used in lifepo4wered operations.
please read section Low level I2C register specification
 of http://lifepo4wered.com/files/LiFePO4wered-Pi3-Product-Brief.pdf

.. code-block:: python

    # Register access masks
    ACCESS_READ = 0x01
    ACCESS_WRITE = 0x02

    # Touch states and masks
    TOUCH_INACTIVE = 0x00
    TOUCH_START = 0x03
    TOUCH_STOP = 0x0C
    TOUCH_HELD = 0x0F
    TOUCH_ACTIVE_MASK = 0x03
    TOUCH_MASK  = 0x0F

    # LED states when Pi on
    LED_STATE_OFF = 0x00
    LED_STATE_ON = 0x01
    LED_STATE_PULSING = 0x02
    LED_STATE_FLASHING = 0x03

    # Auto boot settings
    AUTO_BOOT_OFF = 0x00
    AUTO_BOOT_VBAT = 0x01
    AUTO_BOOT_VBAT_SMART = 0x02
    AUTO_BOOT_VIN = 0x03
    AUTO_BOOT_VIN_SMART = 0x04

License
-------
Distributed under the MIT license: https://opensource.org/licenses/MIT

Copyright (c) 2017 Frédérick Lussier (www.linkedin.com/in/frederick-lussier-757b849)
