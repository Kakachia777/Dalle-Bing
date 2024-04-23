from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dallebing',
    version='1.0.3',
    author='Kakachia777',
    author_email='beka.kakachia777@google.com',
    description='dallebing is an unofficial API wrapper for Bing Copilot Image Creator (based on OpenAI DALL-E 3).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kakachia777/dallebing',
    project_urls={
        'Bug Tracker': 'https://github.com/Kakachia777/dallebing/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['requests', 'browser-cookie-3x', 'psutil'],
    python_requires='>=3.6'
)