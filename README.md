# Image Classification App - Flask, Gunicorn, Nginx, Docker

An image classification app that uses VGG16 for predicting classes and scores for images uploaded to a Flask app. This project was made as a tutorial to share how ML models can be deployed into production or packaged as interactive web-apps for data scientists and data engineers intending to share their machine learning models with a wider audience, beyond a notebook or local development environment. 

## Run Instructions

### Prerequisites
- Have Docker installed along with the Compose plugin
- Make sure no other service is running on port 80 or port 8000 as the nginx and app containers utilize these ports


### Launch
- Run the run.sh script e.g. sudo bash run.sh
- You should see the app and nginx containers start up
- Acess the app through your network e.g. http://localhost or http://localhost:8000