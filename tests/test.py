# import python modules
import os
import sys
import unittest

# add package root
sys.path.append(os.getcwd())

from modelevs_client import (ModelEvs,
                             models_example)


class ModelEvsClientTest(unittest.TestCase):
    def test_download_model_by_name(self) -> None:
        model_evs = ModelEvs(models=models_example,
                             local_storage=os.path.join(os.getcwd(), "./data"))
        model_evs.download_model_by_name("numberplate_options")
        models_list = model_evs.ls_models_local()
        self.assertEqual(models_list, ["numberplate_options_2021_05_23.pt"])

    def test_download_repo_for_model(self) -> None:
        model_evs = ModelEvs(models=models_example,
                             local_storage=os.path.join(os.getcwd(), "./data"))
        model_evs.download_repo_for_model("numberplate_options")
        repos_list = model_evs.ls_repos_local()
        self.assertEqual(repos_list, ["evs-lpr"])

    def test_download_dataset_for_model(self) -> None:
        model_evs = ModelEvs(models=models_example,
                             local_storage=os.path.join(os.getcwd(), "./data"))
        model_evs.download_dataset_for_model("numberplate_options")
        datasets_list = model_evs.ls_datasets_local()
        self.assertEqual(datasets_list, ["autoriaNumberplateOptionsDataset-2021-05-17"])


if __name__ == '__main__':
    unittest.main()
