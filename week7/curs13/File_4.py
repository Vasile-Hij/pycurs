#!/usr/bin/env python3

def main():
    file_input = open('file_input.txt', 'r')
    file_output = open('file_output.txt', 'w')

    while True:
        line = file_input.readline()
        if not line:
            break
        for word in line.split():
            file_output.write(word[0])
        file_output.write(' ')
    file_input.close()
    file_output.close()


if __name__ == "__main__":
    main()
