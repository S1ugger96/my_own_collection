# my_own_role

Роль создаёт файл с помощью модуля `my_own_module`.

Переменные:
- `my_own_role_path` - путь к файлу (по умолчанию `/tmp/my_own_role.txt`)
- `my_own_role_content` - текст в файле (по умолчанию `Hello from my_own_role`)

Пример с своими значениями:

```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_own_role
      vars:
        my_own_role_path: /tmp/custom.txt
        my_own_role_content: "custom text\n"
```
