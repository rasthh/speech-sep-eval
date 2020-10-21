import pytest
from pipeline import BasePipeline


def test_basepipeline():
    modules = {
        "datasets": None,
        "preprocessings": None,
        "models": None,
        "postprocessings": None,
        "metrics": None,
        "reports": None,
    }
    pipeline = BasePipeline(**modules)

    with pytest.raises(NotImplementedError):
        pipeline.run()
