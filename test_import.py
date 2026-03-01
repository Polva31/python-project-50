import sys
print("sys.path:", sys.path)
try:
    from gendiff.cli import main
    print("Импорт успешен")
except ImportError as e:
    print("Ошибка импорта:", e)
