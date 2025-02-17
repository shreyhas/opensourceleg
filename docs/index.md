# opensourceleg

An open-source software library for numerical computation, data acquisition, <br>and control of lower-limb robotic prostheses.

[![Release](https://img.shields.io/github/v/release/neurobionics/opensourceleg)](https://img.shields.io/github/v/release/neurobionics/opensourceleg)
[![Build status](https://img.shields.io/github/actions/workflow/status/neurobionics/opensourceleg/main.yml?branch=main)](https://github.com/neurobionics/opensourceleg/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/neurobionics/opensourceleg)](https://img.shields.io/github/commit-activity/m/neurobionics/opensourceleg)
[![License](https://img.shields.io/github/license/neurobionics/opensourceleg)](https://img.shields.io/github/license/neurobionics/opensourceleg)

<img src="https://github.com/neurobionics/opensourceleg/blob/66ad4289ef9ba8701fac9337778f87b657286484/assets/images/banner.gif?raw=true" width="800" title="Open-Source Leg">

## Installation

The easiest and quickest way to install the _opensourceleg_ library is via [pip](https://pip.pypa.io/en/stable/):

```bash
pip install opensourceleg
```

> If you plan on installing the _opensourceleg_ library on a Raspberry Pi, we recommend using [opensourcelegpi](https://github.com/neurobionics/opensourcelegpi) tool, which is a cloud-based CI tool used to build an up-to-date OS for a [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) that can be used headless/GUI-less to control autonomous/remote robotic systems. This tool bundles the _opensourceleg_ library and its dependencies into a single OS image, which can be flashed onto a microSD card and used to boot a Raspberry Pi. For more information, click [here](https://github.com/neurobionics/opensourcelegpi/blob/main/README.md).

### Developing

To modify, develop, or contribute to the [opensourceleg](https://pypi.org/project/opensourceleg/) library, we encourage you to install [Poetry](https://python-poetry.org), which is a python packaging and dependency management tool. Once you have Poetry installed on your local machine, you can clone the repository and install the _opensourceleg_ library by running the following commands:

```bash
git clone https://github.com/neurobionics/opensourceleg.git
cd opensourceleg

poetry install
poetry shell
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/neurobionics/opensourceleg/settings/secrets/actions/new).
- Create a [new release](https://github.com/neurobionics/opensourceleg/releases/new) on Github.
- Create a new tag in the form `*.*.*`.
- For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

## License

The _opensourceleg_ library is licensed under the terms of the [LGPL-v2.1 license](https://github.com/neurobionics/opensourceleg/raw/main/LICENSE). This license grants users a number of freedoms:

- You are free to use the _opensourceleg_ library for any purpose.
- You are free to modify the _opensourceleg_ library to suit your needs.
- You can study how the _opensourceleg_ library works and change it.
- You can distribute modified versions of the _opensourceleg_ library.

The GPL license ensures that all these freedoms are protected, now and in the future, requiring everyone to share their modifications when they also share the library in public.
