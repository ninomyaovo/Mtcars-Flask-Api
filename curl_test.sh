curl -H "Content-Type: application/json" \
     -X POST \
     -d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}' \
     http://localhost:5050/predict_mpg
