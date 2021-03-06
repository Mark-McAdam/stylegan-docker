# backend/main.py
import time
import config
import inference
import asyncio
import uuid
import cv2
import uvicorn
import numpy as np

from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile

from PIL import Image
from concurrent.futures import ProcessPoolExecutor
from functools import partial


app = FastAPI()


async def generate_remaining_models(models, image, name: str):
    executor = ProcessPoolExecutor()
    event_loop = asyncio.get_event_loop()
    await event_loop.run_in_executor(
        executor, partial(process_image, models, image, name)
    )


def process_image(models, image, name: str):
    for model in models:
        output, resized = inference.inference(models[model], image)
        name = name.split(".")[0]
        name = f"{name.split('_')[0]}_{models[model]}.jpg"
        cv2.imwrite(name, output)


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/{style}")
async def get_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    model = config.STYLES[style]
    start = time.time()
    output, resized = inference.inference(model, image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, output)
    models = config.STYLES.copy()
    del models[style]
    asyncio.create_task(generate_remaining_models(models, image, name))
    return {"name": name, "time": time.time() - start}


# TODO uncomment this and change port to something useful
if __name__ == "__main__":
    # TODO change port back to 8080 for localhost
    uvicorn.run("main:app", host="0.0.0.0", port=${PORT})
