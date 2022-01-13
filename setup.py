from setuptools import setup

package_name = 'random_number_action_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lsc',
    maintainer_email='chulslee20@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "random_number_action_server = random_number_action_python.random_number_action_server:main",
            "random_number_action_client = random_number_action_python.random_number_action_client:main"
        ],
    },
)
