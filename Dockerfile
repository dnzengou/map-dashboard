FROM nginx:alpine
LABEL key="dnzengou <dnzengou@me>"

COPY notebook /notebook
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
