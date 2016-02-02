from setuptools import setup, find_packages

try:
    setup(
        name = "baseride-django-billing",
        packages = find_packages(),
    )
        install_requires = [
            "json_field",
            "django >= 1.6.10, < 1.8",
        ],
        version = "0.1.0",
        classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Framework :: Django",
        ]

finally:
    pass
