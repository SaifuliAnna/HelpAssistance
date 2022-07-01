from setuptools import setup, find_namespace_packages

setup(
    name='HelpAssistance',
    version='0.0.9',
    description='The project "HelpAssistance" - its your personal CLI assistant.' \
                ' AddressBook, NoteBook, CleanFolder - in one app.',
    author='Anna Saifulina',
    author_email='saifulianna.it@gmail.com',
    url='https://github.com/SaifuliAnna',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    data_files=[('helpme_pack', ['helpme_pack/AddressBook.bin', 'helpme_pack/NoteBook.bin'])],
    include_package_data=True,
    entry_points={'console_scripts': [
        'helpme=helpme_pack.main:main']}
)
