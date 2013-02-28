from setuptools import setup

setup(
    name='django-api-playground',
    version='0.2-bja',
    packages=['apiplayground', 'apiplayground.templatetags'],
    zip_safe = False,
    include_package_data=True,
    url='http://github.com/emidln/django-api-playground',
    license='BSD',
    author='fatiherikli, emidln',
    author_email='emidln@gmail.com',
    description='API Playground for RESTful APIs',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        "Framework :: Django",
    ],
)
