# coding: utf-8
"""Tests for context_managers module."""
from abipy.core.testing import AbipyTest
from abipy.tools.context_managers import Timer, temporary_change_attributes


class TestContextManagers(AbipyTest):
    """Test context_managers."""

    def test_api(self):
        """Testing tonumber"""

        class Something(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        with Timer("Creating Something"):
            s = Something(1, 2)

        assert s.x == 1 and s.y == 2

        with temporary_change_attributes(s, x=4, y=5):
            assert s.x == 4 and s.y == 5

        assert s.x == 1 and s.y == 2
