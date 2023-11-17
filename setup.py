from setuptools import find_packages, setup
import pyvectorguidance_setup

try:
    import sys
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'pyvectorguidance',
  packages=find_packages(),
  license=pyvectorguidance_setup.__license__,
  description = pyvectorguidance_setup.__description__,
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = pyvectorguidance_setup.__name__,
  author_email = pyvectorguidance_setup.__author_email__,
  url = pyvectorguidance_setup.__url__,
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['Python', 'Vector Guidance'],
  version=pyvectorguidance_setup.__version__,
  title=pyvectorguidance_setup.__title__,
  install_requires=[
          'numpy==1.26.0',
          'rich==13.3.1',
          'scipy==1.10.0'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.10'
  ],
)