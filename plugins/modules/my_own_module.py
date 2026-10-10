#!/usr/bin/python

# Copyright: (c) 2026, Dmitriy <@S1ugger96>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file with specified content

version_added: "1.0.0"

description:
    - Creates a text file on the remote host at I(path) with I(content).
    - If the file already exists with the same content, nothing is changed (idempotent).

options:
    path:
        description: Path to the file on the remote host.
        required: true
        type: str
    content:
        description: Text content to write into the file.
        required: false
        type: str
        default: ''

author:
    - Dmitriy (@S1ugger96)
'''

EXAMPLES = r'''
- name: Create file with content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: hello world
'''

RETURN = r'''
path:
    description: Path to the file.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: Content written to the file.
    type: str
    returned: always
    sample: 'hello world'
'''

import io
import os

from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default=''),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    result = dict(
        changed=False,
        path=path,
        content=content
    )

    # файл уже есть с тем же содержимым -> ничего не делаем
    if os.path.isfile(path):
        try:
            with io.open(path, 'r', encoding='utf-8') as f:
                current = f.read()
        except (IOError, OSError, UnicodeError) as e:
            module.fail_json(msg='Cannot read file %s: %s' % (path, e), **result)
        if current == content:
            module.exit_json(**result)

    result['changed'] = True

    if module.check_mode:
        module.exit_json(**result)

    try:
        dirname = os.path.dirname(path)
        if dirname and not os.path.isdir(dirname):
            os.makedirs(dirname)
        with io.open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    except (IOError, OSError, UnicodeError) as e:
        module.fail_json(msg='Cannot write file %s: %s' % (path, e), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
