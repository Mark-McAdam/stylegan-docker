# stylegan-docker
Style transfer application, FastAPI backend to serve predictions, Streamlit for the user interface, OpenCV for the predictions



Mark-McAdam/stylegan-docker
### Style transfer web app 

#### Tools used
- FastAPI: for the API
- streamlit : for the interface
- Docker: to containerize the app

#### Download the models
```bash
./download_models.sh
```

#### Run
```bash
docker-compose up -d
```