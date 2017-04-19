from dgu.harvesters.base import Dataset

class TestDataset(Dataset):
    def convert(self, data):
        for k, v in data.items():
            setattr(self, k, v)

def test_dataset_init():
    d = Dataset()
    d.convert(dict(name='test', title='Test'))
    assert len(d.validate()) > 0

def test_dataset_sublass_init():
    d = TestDataset()
    d.convert(dict(name='test', title='Test'))
    assert d.name == 'test'
    assert d.title == 'Test'
