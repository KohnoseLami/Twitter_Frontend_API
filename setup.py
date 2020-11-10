from setuptools import setup
with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name='Twitter_Frontend_API',
    version='0.1.3',
    description='Get information from Twitter using the front-end API built into the Twitter website.',
    url='https://github.com/KohnoseLami/Twitter_Frontend_API',
    author='神瀬来未',
    author_email='info@vxxx.cf',
    license='MIT',
    keywords='twitter scraper frontend api',
    packages=[
        "Twitter_Frontend_API",
    ],
    install_requires=required,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)