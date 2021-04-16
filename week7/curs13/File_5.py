#!/usr/bin/env python3
"""Deleting a file from script"""
import os


def main():

    os.remove('your_file.txt') if os.path.exists('your_file.txt') else print('File is not found')


if __name__== "__main__":
    main()