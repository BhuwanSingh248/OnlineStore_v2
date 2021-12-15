"""
    tell pytest when pytest command hits is will run specified functions first 

"""

pytest_plugins = [
    "config.tests.fixtures",
    "config.tests.selenium",
    "config.tests.factories",
]
