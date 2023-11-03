# FastAPI  + Zarr + Xarray + Dask

A demo of FastAPI application to extract data at the specific points defined by [latitudes and longitudes] from a zarr dataset using Dask and Xarray.

The key aim to speed up point data extraction from data in zarr formats using dask's local cluster. 

[Zarr](https://zarr.readthedocs.io/en/latest/tutorial.html) arrays have been designed for use as the source or sink for data in parallel computations. Here, we use Zarr data as data source. It means that multiple concurrent read operations may occur. 

Both multi-threaded and multi-process parallelism are possible. The bottleneck for most storage and retrieval operations is compression/decompression, and the Python global interpreter lock (GIL) is released wherever possible during these operations, so Zarr will generally not block other Python threads from running.

Steps to run:

1) Run command `dask scheduler` to start Dask Schedular, you can visit the dashboard here: http://localhost:8787/status
2) Run command `dask worker localhost:8786` to start Dask worker
3) Run command `uvicorn server:app --reload --port 8090` to start the ASGI web server
4) Launch Swagger at http://localhost:8090/docs/ 
5) Invoke HTTP via curl using command curl -X 'POST' \
                'http://localhost:8090/pips/' \
                -H 'accept: application/json' \
                -H 'Content-Type: application/json' \
                -d '{
                "latitude": [15, 3],
                "longitude": [200, 5]
                }'`
6) You should see the results as below:

```json
{
  "time(secs)": 0.15551209449768066,
  "result": [
    {
      "points": 0,
      "time": 1356998400000,
      "lat": 15,
      "lon": 200,
      "air": 296.2900085449
    },
    {
      "points": 0,
      "time": 1357020000000,
      "lat": 15,
      "lon": 200,
      "air": 296.2900085449
    },
    {
      "points": 0,
      "time": 1357041600000,
      "lat": 15,
      "lon": 200,
      "air": 296.3999938965
    },
    {
      "points": 0,
      "time": 1357063200000,
      "lat": 15,
      "lon": 200,
      "air": 297.5
    },
    {
      "points": 0,
      "time": 1357084800000,
      "lat": 15,
      "lon": 200,
      "air": 297.7900085449
    },
    ...
}
```

## References
https://www.dask.org/get-started

https://docs.xarray.dev/en/stable/

https://fastapi.tiangolo.com/

https://github.com/chirdeeptomar/fastapi-with-dask

https://zarr.readthedocs.io/en/stable/

