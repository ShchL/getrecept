from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import random
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = '45d11cdde2424e35a41d4a37e919f5b1'
base_url = 'https://api.spoonacular.com/recipes/'

@app.get("/")
async def root():
    random_recipe_id = random.randint(1, 900)
    endpoint = f'{base_url}{random_recipe_id}/information'
    params = {'apiKey': api_key}
    r = requests.get(endpoint, params=params)
    return {'info':r.json(), 'id': random_recipe_id}

@app.get("/list/")
async def get_list(q: list | None = Query()):
    recipe_list = []
    for recipe_id in q:
        endpoint = f'{base_url}{recipe_id}/information'
        params = {'apiKey': api_key}
        r = requests.get(endpoint, params=params)
        recipe_list.append({'info':r.json(), 'id': recipe_id})
    return recipe_list

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))
