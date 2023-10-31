from setuptools import setup

package_name = 'ros2_test_communicate'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'ros2_test_communicate.test_talker',
        'ros2_test_communicate.test_listener',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='htm2323',
    author_email="is0578ri@ed.ritsumei.ac.jp",
    maintainer='htm2323',
    maintainer_email="is0578ri@ed.ritsumei.ac.jp",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TODO: Package description.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_talker= ros2_test_communicate.test_talker:main',
            'test_listener= ros2_test_communicate.test_listener:main',
        ],
    },
)