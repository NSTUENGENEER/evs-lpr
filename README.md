# ModelEvs Client

## Installation
```bash
pip3 install git+https://github.com/NSTUENGENEER/evs-lpr.git
```
or
```bash
git clone https://github.com/NSTUENGENEER/evs-lpr.git
cd ./modelevs-client
python3 setup.py install
```

## Quick Start
```python3
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
# model_evs.download_repo_for_model("numberplate_options")
# model_evs.download_dataset_for_model("numberplate_options")

# ls local storage
models_list = model_evs.ls_models_local()
print(models_list)
```
## Tests
```bash
python3 ./tests/test.py
```
