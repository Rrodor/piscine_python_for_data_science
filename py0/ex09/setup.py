from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="rrodor",
    author_email="rrodor@student.42perpignan.fr",
    description="A sample test package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rrodor/piscine_python_for_data_science.git",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        # Add your project's classifiers here
    ],
    python_requires='>=3.10',
)
