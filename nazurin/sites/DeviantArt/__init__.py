"""DeviantArt site plugin."""
from .api import DeviantArt
from .config import PRIORITY
from .interface import handle, patterns

__all__ = ['DeviantArt', 'PRIORITY', 'patterns', 'handle']
