from dgu.harvesters.base import Dataset

class TestDataset(Dataset):
    def convert(self, data):
        pass

def test_dataset_init():
    d = Dataset(name='test', title='Test')
    assert d.name == 'test'
    assert d.title == 'Test'

def test_dataset_sublass_init():
    d = TestDataset(name='test', title='Test')
    assert d.name == 'test'
    assert d.title == 'Test'
