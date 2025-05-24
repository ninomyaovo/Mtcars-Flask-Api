# Mtcars-Flask-Api

This repository contains a predicting model trained for the classic `mtcars` dataset. The goal of this repository is to provide files and steps needed to clone this repository and reproduce the API.

The API uses all the features(`cyl`, `disp`, `hp`, `drat`, `wt`, `qsec`, `vs`, `am`, `gear`, `carb`) along with a linear model to predict the outcome of `mpg`. After building up the model, a docker image was created and uploaded to dockerhub, then deployed in google cloud run.

## Steps to deploy API
### 1. Clone this github repository to local:
```
git clone https://github.com/ninomyaovo/Mtcars-Flask-Api
cd Mtcars-Flask-Api
```


### 2. Build docker image
```
docker build -t ninomya/mtcars-flask-api:latest .
```

### 3. Run image
```
docker run -p 5050:5050 ninomya/mtcars-flask-api:latest
```

### 4. Push to dockerhub
```
docker push ninomya/mtcars-flask-api:latest
```

### 5. Deploy to google cloud run 
Note: This step solves issues regarding the Apple M1/M2 chip users. Directly deploy google cloud run after creating this dockerhub repo.
```
docker buildx create --use
docker buildx build --platform linux/amd64 -t docker.io/ninomya/mtcars-flask-app:latest . --push
```

## Test to run code
### Locally:
```
curl -H "Content-Type: application/json" \
-X POST \
-d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}' \
http://localhost:5050/predict_mpg
```

### On Google Cloud Run:
```
curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}' \
     https://mtcars-flask-app-696925248391.europe-west1.run.app/predict_mpg
```

### Expected output:
```
{
  "predicted_mpg": 22.59950576126238
}
```
