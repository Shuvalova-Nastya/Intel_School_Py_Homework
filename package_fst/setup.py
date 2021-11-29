from setuptools import setup

setup(
name='package_fst',
version='0.2',
description='description',
url='http://github.com/name/package_name',
author='Shuvalova Anastasia',
author_email='shuvalova.nastya@mail.ru',
license='MIT',
packages=['time_pkg.get_time_pkg'],
namespace_packages=['time_pkg'],
install_requires=[
'requests==2.26.0'
],
entry_points={
'console_scripts': [
'get_time=time_pkg.get_time_pkg.get_time_module:main'
]
}
)




