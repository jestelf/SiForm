import os
import sys

# Добавляем каталог src в PYTHONPATH, чтобы модули можно было импортировать
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
