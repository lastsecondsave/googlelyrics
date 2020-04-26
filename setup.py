from setuptools import setup

setup(
    name="googlelyrics",
    version="0.1",
    description="Grab lyrics from Google search results.",
    author="lastsecondsave",
    packages=["googlelyrics"],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.22.0",
        "beautifulsoup4>=4.9.0"
    ],
    entry_points={
        "console_scripts": [
            "googlelyrics = googlelyrics.__main__:main"
        ]
    }
)
