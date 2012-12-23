:: qtlabgui.bat
:: Runs QTlab GUI part on Windows

@ECHO OFF

SET PATH=%CD%\3rd_party\Console2\;%PATH%

:: If using a separate GTK install (and not the one provided in the
:: pygtk-all-in-one installer), uncomment and adjust the following
:: two lines to point to the appropriate locations
::SET GTK_BASEPATH=%CD%\3rd_party\gtk
::SET PATH=%CD%\3rd_party\gtk\bin;%CD%\3rd_party\gtk\lib;%PATH%

:: Check for version of python
IF EXIST c:\python27\python.exe (
    SET PYTHON_PATH=c:\python27
    GOTO mark1
)
IF EXIST c:\python26\python.exe (
    SET PYTHON_PATH=c:\python26
    GOTO mark1
)
:mark1

:: Run QTlab GUI
start %PYTHON_PATH%\pythonw.exe source/gui/guiclient.py %*
:: start Console -w "QTLab GUI" -r "/k %PYTHON_PATH%\python.exe %PYTHON_PATH%\scripts\ipython-script.py --gui=gtk -i source/gui/guiclient.py -- -p 12003 %*
