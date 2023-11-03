from typing import List
from pydantic import BaseModel
import xarray as xr
from dask.distributed import Client, Future

DASK_CLUSTER = "localhost:8786"


class Item(BaseModel):
    latitude: List[float] = []
    longitude: List[float] = []


async def get_data(locs: Item) -> xr.DataArray:
    async with Client(DASK_CLUSTER, asynchronous=True) as client:
        zarr_store = r"data/air_rechunked_consolid.zarr"
        da_zr = xr.open_zarr(zarr_store, consolidated=True)['air']
        sel_lats = locs.latitude
        sel_lons = locs.longitude

        da_sel = da_zr.sel(lat=xr.DataArray(sel_lats, dims='points'),
                           lon=xr.DataArray(sel_lons, dims='points'),
                           method='nearest'
                           ).to_dask_dataframe()

        future: Future = client.compute(da_sel)
        return await future
