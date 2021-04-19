#!/bin/usr/env python3
"""Contacts agenda that contains fields as: first name, last name, phone number and email.
    Multiple commands: list, add, delete, search, modify and exit.
"""


import sys

AGENDA_FILE = 'agenda_file.csv'


def serialize(registration):
    """A string as field1, field2"""
    return registration.split(',')


def deserialize(registration):
    """List [field1, field2]"""
    output = ''
    for index, element in enumerate(registration):
        if index != 0:
            output = '%s' % output
        output='%s%s' % (output, element)
    return output


def load_data(agenda_file):
    register_list = []
    handler = open(agenda_file, 'r')
    fields = handler.readlines()
    handler.close()
    for registration in fields:
        register_list.append(serialize(registration.strip()))
    return register_list


def menu(actions):
    print('Agenda')
    for action in actions.keys():
        print('---%s (%s)' % (action, action[0]))


def agenda_add():
    global AGENDA_FILE
    print('Add a contact in agenda')
    registration = []
    for submenu_action in ['First Name:', 'Last Name: ', 'Phone: ', 'Email: ']:
        registration.append(input(submenu_action))
    print('You have inserted: %s' % deserialize(registration))
    append_agenda(AGENDA_FILE, registration)


def agenda_modify():
    global AGENDA_FILE
    print('Modify any registration')
    register_list = load_data(AGENDA_FILE)
    agenda_list()
    index = input('Insert the registration number: ')
    if not index.isnumeric() or int(index) < 0:
        print('You have inserted a wrong registration number!')
        return
    index = int(index)
    agenda_add()
    register_list = load_data(AGENDA_FILE)
    register_list.pop(index)
    rewrite_agenda(AGENDA_FILE, register_list)


def agenda_remove():
    global AGENDA_FILE
    print('Delete a registration')


def agenda_search():
    global AGENDA_FILE
    print('Search for a registration')
    search_string = input('Search by: ')
    register_list = load_data(AGENDA_FILE)
    results = []
    for registration in register_list:
        for field in registration:
            if search_string in field:
                print(deserialize(registration))
                break


def agenda_list():
    global AGENDA_FILEe
    register_list = load_data(AGENDA_FILE)
    for index, registration in enumerate(register_list):
        print('%s - %s' % (index, deserialize(registration)))


def agenda_exit():
    sys.exit()


def rewrite_agenda(file, registration_list):
    """Rewrite agenda from scratch"""
    handler = open(file, 'w')
    for registration in registration_list:
        handler.write('%s\n' % deserialize(registration))
    handler.close()


def append_agenda(file, registration):
    """Insert a registration at the end"""
    handler = open(file, 'a')
    handler.write("%s\n" % deserialize(registration))
    handler.close()


def get_menu_action(actions, user_input):
    if user_input.isalpha() and len(user_input) == 1:
        for action_name in actions.keys():
            if action_name.lower().startswith(user_input.lower()):
                return actions[action_name]
    print('Wrong input!')
    return None


def main():
    """Entrypoint"""
    actions = {
        'List': agenda_list,
        'Add': agenda_add,
        'Delete': agenda_remove,
        'Modify': agenda_modify,
        'Search': agenda_search,
        'Exit': agenda_exit
    }

    while True:
        menu(actions)
        user_action = input()
        if get_menu_action (actions, user_action):
            get_menu_action(actions, user_action)()

    # registration = ["Joey", "J", "073216543", "joeyj@email.com"]


if __name__ == "__main__":
    main()