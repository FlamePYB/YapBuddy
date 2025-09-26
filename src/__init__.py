"""Top-level package for YapBuddy source code."""

# Import subpackages to expose them as attributes of the `src` package.
from . import UI, Message_Mechanics, Utils, API  # noqa: F401

__all__ = ["UI", "Message_Mechanics", "Utils", "API"]
