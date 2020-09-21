# PensionContent



## Python activate code

To make it easier to setup a virtual env, add:
```bash
function setup_virtual_env {
    echo "setting up the virtual env"
    virtualenv -p /usr/bin/python3 venv
    source venv/bin/activate
    if [ -f requirements.txt ] ; then
      echo "installing requirements"
      pip install -r requirements.txt
    fi
}
alias activate="setup_virtual_env"
```