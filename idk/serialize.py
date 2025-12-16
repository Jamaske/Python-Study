#!/usr/bin/env python3
import os
import sys

# Список игнорируемых расширений
IGNORE_EXTS = {
    ".pyc", ".pyo", ".so", ".dll", ".exe", ".dll",
    ".bin", ".dat", ".class", ".jar",
    ".zip", ".tar", ".gz", ".7z", ".rar",
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico",
    ".pdf", ".mp3", ".mp4", ".avi", ".mov",
}
# Список игнорируемых директорий
IGNORE_DIRS = {"__pycache__", ".git", ".svn", "node_modules"}

def serialize_dir(root):
    for dirpath, dirnames, files in os.walk(root):
        # пропускаем игнорируемые директории
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in files:
            ext = os.path.splitext(fname)[1].lower()
            if ext in IGNORE_EXTS:
                continue

            path = os.path.join(dirpath, fname)
            rel = os.path.relpath(path, root)
            try:
                with open(path, encoding='utf-8', errors='replace') as f:
                    content = f.read()
            except (IsADirectoryError, PermissionError):
                continue

            # строка с относительным путём
            print(f"\n<<path:{rel}>>\n")
            # вывод содержимого файла, удаляя лишние переводы строк в конце
            print(content.rstrip('\n'))

if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    serialize_dir(root)

# Пример использования:
# chmod +x serialize.py
# ./serialize.py /path/to/project