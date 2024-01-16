import unittest
import tempfile
import os
import yaml

class TestYaml(unittest.TestCase):
    def setUp(self) -> None:
        with open('./test.yaml','rb') as f:
            self.yaml = yaml.load(f)

    def test_read_yaml(self):
        print(self.yaml)
        self.assertEqual(type(self.yaml),dict)

    # def test_load(self):
    #     temp = tempfile.NamedTemporaryFile()
    #     metricsjson.save(metrics=self.metrics, path=temp.name)
    #     metrics = metricsjson.load(path=temp.name)
    #     self.assertDictEqual(d1=metrics.dict(), d2=self.metrics.dict())
        

