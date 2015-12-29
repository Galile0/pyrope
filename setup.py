from distutils.core import setup

setup(
        name='pyrope',
        version='1.0rc1',
        packages=['pyrope'],
        url='https://github.com/Galile0/pyrope',
        license='GNU GPL v3.0',
        author='Jan Temme',
        author_email='jan.temme@gmail.com',
        install_requires=[
              'bitstring',
          ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Programming Language :: Python :: 3 :: Only'
             ],
        description='parse and decode replay files from Rocket League'
)
