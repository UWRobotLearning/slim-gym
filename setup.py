from setuptools import find_packages, setup

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
    packages=find_packages(),
    python_requires=">=3.6",
    url="https://www.gymlibrary.dev/",
    version=0.26.0,
    zip_safe=False,
)
