import json
import time
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, status
from backend import Item, get_data

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root() -> dict:
    return {"Hello": "World"}


@app.post("/pips/")
async def extract(args: Item):
    if args.latitude and args.longitude:
        if len(args.latitude) != len(args.longitude):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The latitude and longitude should have the same length.",
            )

        begin = time.time()
        result = await get_data(args)
        parsed = json.loads(result.to_json(orient="records"))

        return {
            "time(secs)": (time.time() - begin),
            "result": parsed,
        }
    else:
        return {'Alert': 'Please provide latitude and longitude information'}

