# Flask skeleton

* `main.py` -- code thath launches app
* `loadApi.py` -- functions for including endpoints functions
* `make.cmd` -- commands to prepare and run app
* `endpoints/common.py` -- file that imported by each endpoint main
* `endpoints/root` -- directory for `/` endpoint
* `endpoints/x` -- directory for /x endpoint
* `endpoints/x/main.py` -- file with class (one and only) describing x endpoint methods

Use `wizard.py endpoint_name [endpoint_name ...]` to create endpoints

Use name "root" to create "/" endpoint