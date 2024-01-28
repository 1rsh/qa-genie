import pathlib
from setuptools import setup, find_packages

VERSION = '1.0.0a3'
DESCRIPTION = 'Generating Question Answer Database from Unstructured Text'
LONG_DESCRIPTION = pathlib.Path("README.md").read_text()

setup(
    name="qa_genie",
    version=VERSION,
    author="Irsh Vijayvargia",
    author_email="<irsh.iitkgp@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="The Unlicense",
    project_urls = {
        "GitHub": "https://github.com/1rsh/qa-genie"
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires = ">=3.9",
    install_requires=['hugchat==0.3.0', 'pandas', 'tqdm'],
    packages=find_packages(),
    include_package_data=True,
    keywords=['python', 'question generation', 'question answer', 'nlp', 'llm', 'llm for question answering', 'huggingface'],
    
)