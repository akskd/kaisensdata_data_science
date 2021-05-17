FROM python:3.7
RUN pip install twine
COPY ./ ./
RUN python setup.py sdist bdist_wheel
CMD ["twine", "upload" , "-u", "{{ cookiecutter.pypi_user }}" , "-p", "{{ cookiecutter.pypi_pwd}}" ,"--repository-url" , "{{ cookiecutter.pypi }}" , "dist/*"]


