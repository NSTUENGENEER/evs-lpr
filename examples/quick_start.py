# import python modules
import os
import sys

# add package root
sys.path.append(os.getcwd())

from modelevs_client import (ModelEvs,
                             models_example)

# initial
model_evs = ModelEvs(models=models_example,
                     local_storage=os.path.join(os.getcwd(), "./data"))

# download model
model_evs.download_model_by_name("numberplate_options")
model_evs.download_repo_for_model("numberplate_options")

# ls local storage
models_list = model_evs.ls_models_local()
print(models_list)
