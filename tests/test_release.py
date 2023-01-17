import pytest
import andromeda

def test_import():
    assert andromeda.__package__ == 'andromeda'

if __name__ == '__main__':
    pytest.main()