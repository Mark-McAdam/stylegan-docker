# stylegan-docker
Style transfer application, FastAPI backend to serve predictions, Streamlit for the user interface, OpenCV for the predictions


from root of project folder:
$ docker-compose up -d --build

This should create frontend and backend 


Sometimes I think I had to start manually the backend as well. Sometimes it shut down as soon as compose was finished. 

$ docker run -p 8080:8080 backend
