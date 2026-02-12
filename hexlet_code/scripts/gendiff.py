#!/usr/bin/env python
"""
CLI utility for comparing configuration files.
"""

import argparse


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
    
    # Пока просто заглушка
    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Output format: {args.format}")


if __name__ == '__main__':
    main()
