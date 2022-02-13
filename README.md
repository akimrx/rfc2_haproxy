![Role tests](https://github.com/akimrx/rfc2_haproxy/actions/workflows/ci.yml/badge.svg)

Role Name
=========

Example haproxy role.

Role Variables
--------------

See `defaults/main.yml`

| Variable | Default | Description |
|----------|---------|-------------|
| `haproxy_version` | `2.0.*` | haproxy apt package version |



Running tests locally
---------------------
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
ansible-galaxy collection install community.docker==2.1.1

molecule -v test
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
      - rfc2_haproxy
```

License
-------

MIT

Author Information
------------------

akimrx
