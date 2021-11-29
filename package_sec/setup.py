from setuptools import setup

setup(
name='package_sec',
version='0.2',
description='description',
url='http://github.com/name/package_name',
author='Shuvalova Anastasia',
author_email='shuvalova.nastya@mail.ru',
license='MIT',
packages=['time_pkg.pretty_print_pkg'],
namespace_packages=['time_pkg'],
install_requires=[
    'package_fst>0.1'
],
entry_points={
'console_scripts': [
'get_time=time_pkg.pretty_print_pkg.pretty_print_module:main'
]
}
)




