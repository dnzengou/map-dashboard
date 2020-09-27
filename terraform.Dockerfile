FROM alpine
LABEL key="dnzengou <dnzengou@me>"

RUN wget -O /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.13.3/terraform_0.13.3_linux_amd64.zip && \
    unzip /tmp/terraform.zip -d /
RUN apk add --no-cache ca-certificates curl
USER nobody
ENTRYPOINT [ "/terraform" ]
