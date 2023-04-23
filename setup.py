from setuptools import find_packages, setup
from slimgym import __version__

requires = [numpy]

setup(
    author="Robot Learning",
    author_email="robotlearning@cs.uw.edu",
    classifiers=[
        # Python 3.6 is minimally supported (only with basic gym environments and API)
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Gym: A universal API for reinforcement learning environments",
    license="MIT",
    name="slimgym",
    requires=requires,
    packages=find_packages(),
    python_requires=">=3.6",
    url="https://www.gymlibrary.dev/",
    version=__version__,
    zip_safe=False,
)
