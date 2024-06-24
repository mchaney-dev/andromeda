import pytest
from andromeda.model import Model

@pytest.fixture
def init_model():
    model = Model()
    return model

def test_model_import(init_model):
    assert init_model.name == 'gpt-neo-125m'