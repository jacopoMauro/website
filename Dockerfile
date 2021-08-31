FROM klakegg/hugo:0.83.1-ext-debian-ci AS hugo

RUN git clone --depth=1 https://github.com/jacopoMauro/website.git /src && \
    # try to test if the site can be build
    hugo 

WORKDIR /src
EXPOSE 1313

CMD [ "hugo", "server", "--disableLiveReload", "--bind", "0.0.0.0" ]
