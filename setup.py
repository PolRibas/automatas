from setuptools import setup, find_packages

setup(
    name='automatas',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        # Añade otras dependencias aquí
    ],
    entry_points={
        'console_scripts': [
            'automatas=mi_proyecto.modulo:main',
        ],
    },
)
