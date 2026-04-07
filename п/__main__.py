# -*- coding: utf-8 -*-
"""
Точка входа для `python -m п`
"""

import sys
import os

# Добавить родительский каталогъ в path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from п.транспайлеръ import ТранспайлеръП, ОшибкаП, главная

def main():
    главная()

if __name__ == '__main__':
    main()
