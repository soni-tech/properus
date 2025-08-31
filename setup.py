from setuptools import setup, find_packages

setup(
    name="properus_custom",
    version="0.0.1",
    description="Custom ERPNext app",
    author="Sony",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "frappe>=15"
    ],
    zip_safe=False
)
