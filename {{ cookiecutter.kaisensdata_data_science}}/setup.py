from setuptools import find_packages, setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('./requirements.txt')

# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir) for ir in install_reqs if not str(ir).startswith("-") ]


setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='MIT',
    install_requires=[reqs]
)


