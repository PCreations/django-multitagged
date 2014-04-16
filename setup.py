import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-multitagged',
    version='0.1',
    packages=['multitagged'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Django app. Provides a way to tag (with django-taggit) multiple models with same TaggedItem',
    long_description=README,
    url='https://github.com/PCreations/django-multitagged',
    author='Pierre Criulanscy',
    author_email='pcriulan@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django'
    ],
)