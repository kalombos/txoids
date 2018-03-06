from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(name='txoids',
          version='0.1.9',
          url="https://github.com/kalombos/txoids",
          download_url="https://github.com/kalombos/txoids",
          description='Tool for parsing switches using SNMP',
          long_description="Tools for parsing switches using SNMP protocol. "
                           "It uses pynetsnmp library which works pretty fast with SNMP. ",
          author='Nikolay Gorshkov',
          author_email='nogamemorebrain@gmail.com',
          maintainer='kalombo',
          maintainer_email='nogamemorebrain@gmail.com',
          packages=find_packages(),
          install_requires=[
              'pynetsnmp-2',
          ],
          keywords=['snmp', 'twisted', 'pynetsnmp', 'netsnmp'],
          )
