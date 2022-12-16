from setuptools import setup

setup(name="hellopkg",
    version="0.1.0",
    package_dirs=["hello"],
    entry_points={
          'console_scripts': [
          	'helloctl=hello.hello:hello'
          ],
})

