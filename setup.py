from setuptools import setup, find_packages

setup(
    name='lets-commands',  # Keep the package name lowercase for consistency
    version='0.1.0',
    packages=find_packages(),  # This should automatically find 'lets_digest'
    entry_points={
        'console_scripts': [
            'lets-digest=lets_digest.digest:main'  # Reference the main function correctly
        ]
    },
    author='Raed Tulefat',
    author_email='raed@example.com',
    description='Various command line tools for daily tasks',
    install_requires=[
        # Add any dependencies here
    ]
)
