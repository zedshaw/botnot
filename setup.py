try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'What if monit were a botnet?',
    'author': 'Zed A. Shaw',
    'url': 'http://pypi.python.org/pypi/botnot',
    'download_url': 'http://pypi.python.org/pypi/botnot',
    'author_email': 'zedshaw@zedshaw.com',
     'version': '1.0',
     'scripts': ['bin/botnot'],
     'install_requires': ['python-lust', 'python-modargs', 'setproctitle',
                          'gevent'],
     'packages': ['botnot', 'botnot.checks'],
     'name': 'botnot'
}

setup(**config)
