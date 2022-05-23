"""
The modelevs_client module.
"""
from .modelevs_client import ModelEvs
from .models_example import models_example
from .cli import main

__version__ = '1.1.0'

__all__ = (
    '__version__',
    'ModelEvs', 'models_example',
    'main',
)
