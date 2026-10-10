# my_own_namespace.yandex_cloud_elk

Коллекция для ДЗ «Создание собственных модулей».

Что внутри:
- модуль `my_own_module` - создаёт текстовый файл с нужным текстом
- роль `my_own_role` - запускает этот модуль

## Модуль my_own_module

Параметры:
- `path` - путь к файлу (обязательный)
- `content` - что записать в файл (по умолчанию пусто)

Если файл уже есть и текст в нём такой же, модуль ничего не меняет (changed: false).

Пример:

```yaml
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "hello world\n"
```

## Роль my_own_role

Переменные по умолчанию (defaults):
- `my_own_role_path: /tmp/my_own_role.txt`
- `my_own_role_content: "Hello from my_own_role\n"`

Пример playbook:

```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - my_own_namespace.yandex_cloud_elk.my_own_role
```

## Установка

```bash
ansible-galaxy collection build
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

