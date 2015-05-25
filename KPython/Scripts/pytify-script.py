#!k:\ArcherVMPeridot\htdocs\KPython\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytify==2.0.4','console_scripts','pytify'
__requires__ = 'pytify==2.0.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pytify==2.0.4', 'console_scripts', 'pytify')()
    )
