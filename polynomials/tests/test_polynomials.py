"""
Unit and regression test for the polynomials package.
"""

# Import package, test suite, and other packages as needed
import polynomials
import pytest
import sys

def test_polynomials_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "polynomials" in sys.modules
