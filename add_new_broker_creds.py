#!/usr/bin/python
# -*- coding: utf-8 -*-


import os

path_to_RT_directory = '/home/serge/TMP/1'
broker_name = 'new_test_broker2'
bin_files_list = ['openprocurement_tests',
                  'op_tests',
                  'python_interpreter',
                  'rebot',
                  'rflint',
                  'rfshell']


def add_broker_to_bin(broker_name, path_to_RT_directory, bin_files_list):
    if os.path.exists('{}/robot_tests/bin'.format(path_to_RT_directory)):
        print ('Path to RT exists')
        for file_name in bin_files_list:
            file_path = '{}/robot_tests/bin/{}'.format(path_to_RT_directory, file_name)
            broker_directory = "  '{}/robot_tests/src/robot_tests.broker.{}',\n".format(path_to_RT_directory, broker_name)
            if os.path.exists(file_path):
                with open(file_path, 'r') as rf:
                    content = rf.readlines()
                    if broker_directory not in content:
                        for string in content:
                            if 'robot_tests/src/robot_tests.broker' in string:
                                index = content.index(string)
                                content.insert(index, broker_directory)
                                print ('File {} updated'.format(file_name))
                                break
                    else:
                        print ('Paths to broker directory: {}  already exists in {}'.format(broker_directory, file_name))
                with open(file_path, 'w') as wf:
                    wf.writelines(content)
            else:
                print ('File {} does not exist'.format(file_name))
    else:
        print('Incorrect path: {}'.format('{}/robot_tests/bin'.format(path_to_RT_directory)))


def add_broker_directory_in_src(broker_name, path_to_RT_directory):
    path_to_broker_directory = '{}/robot_tests/src/robot_tests.broker.{}'.format(path_to_RT_directory, broker_name)
    if not os.path.exists(path_to_broker_directory):
        os.mkdir(path_to_broker_directory)
        print ('Create directory:  {}'.format(path_to_broker_directory))
    else:
        print ('Broker directory is already exists.. Nothing to do!')


add_broker_to_bin(broker_name, path_to_RT_directory, bin_files_list)
add_broker_directory_in_src(broker_name, path_to_RT_directory)
