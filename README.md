# Map dashboard with Bokeh and Plotly

## data source:
![COVID-19data](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/data)

## Visualizations
![COVID-19_log_cases-sublploting](plots/COVID-19_cases-sublploting_19052020.png)
![COVID-19 plot](plots/plot_covid19_2020.png)

## Predictive modeling - test
![ML model](ml-model.png)


### How to run it on docker
1. Launch Docker:
`systemctl start docker` (if you run Kali linux)

1.1. Test docker is well installed:
`docker run hello-world`

2. Create a Docker image, Build it and run a container from it
(with option to tag it with the file name and send all the folder's content):
`docker build --tag notebook .`

3. For the first time, run & publish docker image (notebook) file (on port 80 by default):
`docker run --publish 80:80 notebook`

4. Moving forward, to expose the docker image via command up (down being to remove the image files that are up):
`docker-compose up -d website` ||
`docker-compose up`

5. Run unit-tests with docker-compose built selenium, and remove (--rm):
`docker-compose run --rm unit-tests`

6. Build our website image with docker-compose that enables running test:
`docker-compose up -d website selenium`

7. Build terraform from its online location:
`docker build -t terraform`

8. Build and testing a terraform docker image file after modification of the docker-compose.yml file with terraform:
`docker build -t terraform . -f terraform.Dockerfile`



