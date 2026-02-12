#!/usr/bin/env python
"""
CLI utility for comparing configuration files.
"""

import argparse
import json


def parse_file(file_path):
    """Read and parse JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)


def main():
    """Entry point for the gendiff CLI."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish'
    )
    
    args = parser.parse_args()
    
    # Читаем и парсим файлы
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)
    
    # Пока просто выводим данные для проверки
    print("File 1:", data1)
    print("File 2:", data2)
    print(f"Output format: {args.format}")


if __name__ == '__main__':
    main()
