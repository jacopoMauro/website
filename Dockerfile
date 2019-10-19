FROM alpine as Source

#RUN apk update && \
#		apk add git
		
#RUN git clone --depth=1 https://github.com/jacopoMauro/website.git /git

########

FROM debian:10-slim

ENV HUGO_VERSION='0.58.3'
ENV HUGO_NAME="hugo_extended_${HUGO_VERSION}_Linux-64bit"
ENV HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_NAME}.tar.gz"
ENV BUILD_DEPS="wget"
WORKDIR /hugo
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ${BUILD_DEPS} \
    git \
    ca-certificates && \
    wget "${HUGO_URL}" && \
    tar -zxvf "${HUGO_NAME}.tar.gz" && \
    mv ./hugo /usr/bin/hugo && \
    apt-get remove -y ${BUILD_DEPS} && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    cd / && \
    rm -rf /hugo
WORKDIR /src

EXPOSE 1313

CMD [ "hugo", "server", "--bind", "0.0.0.0" ]
