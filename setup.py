# vim: set fileencoding=utf8:
from setuptools import setup, find_packages

version = '0.0.2'

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()
setup(
    name="django-userel",
    version=version,
    description = "Extend ForeignKey field for User. It support ``auto_now`` and ``auto_now_add``",
    long_description=read('README.rst'),
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = "django ForeignKey auto_now auto_now_add user",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/django-userel",
    download_url = r"https://github.com/lambdalisue/django-userel/tarball/master",
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'distribute',
        'setuptools-git',
    ],
    test_suite='packageutils.runtests.runtests',
    tests_require=[
        'django>=1.3',
        'PyYAML',
    ],
)
