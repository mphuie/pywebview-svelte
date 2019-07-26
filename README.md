# pywebview-svelte
pywebview + svelte integration + build (mac) app


# usage

- Get svelte dependencies `npm install`
- Get python dependencies `pip install -r requirements.txt`
- Build frontend `npm run build`
- Run `python main.py`
- Build mac app package `python py2app_setup.py py2app`


# notes
If you're on a mac and do not get an "app" when you run `main.py` - IE no menubar, window doesn't accept keyboard focus (ie you can't CMD-Q), you will need to patch your virtualenv.

- Download this repo `https://github.com/gldnspud/virtualenv-pythonw-osx`
- Unzip
- `cd install_pythonw`
- `python __init__.py <absolute path of your venv directory (the one that contains bin)>`


