FROM yhnw/openwrt-sdk:base

ENV SDK_URL {{ user_url }}
ENV SDK_SUFFIX .tar.xz

RUN sudo -iu openwrt wget -nv $SDK_URL &&\
    sudo -iu openwrt tar xf "$(basename $SDK_URL)" &&\
    sudo -iu openwrt rm "$(basename $SDK_URL)" &&\
    sudo -iu openwrt mv "$(basename $SDK_URL $SDK_SUFFIX)" sdk &&\
    sudo -iu openwrt sdk/scripts/feeds update -a &&\
    sudo -iu openwrt ln -s ../feeds/base/package/utils sdk/package/utils
