# import python modules
import os
import sys
import asyncio

# add package root
sys.path.append(os.getcwd())

from modelevs_client import (ModelEvs,
                             models_example)


async def get_model(i, model_name):
    # initial
    model_evs = ModelEvs(models=models_example,
                         local_storage=os.path.join(os.getcwd(), "./data"))

    # download model
    info = model_evs.download_model_by_name(model_name)

    # ls local storage
    print(i, info)
    return info

model_names = ["numberplate_options", "numberplate_options"]
futures = [get_model(i, model_name) for i, model_name in enumerate(model_names)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
