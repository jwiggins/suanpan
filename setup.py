from __future__ import unicode_literals

from setuptools import setup, find_packages

setup(name='suanpan',
      version='0.0.1',
      license='BSD',
      author='John Wiggins',
      author_email='jwiggins@enthought.com',
      description='算盘: An iMessage bot for tracking spending',
      long_description='',
      url='https://github.com/jwiggins/suanpan',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Operating System :: MacOS',
      ],
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'suanpan = suanpan.agent:main',
          ],
      },
      )
