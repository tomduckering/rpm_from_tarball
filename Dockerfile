FROM centos:7
RUN yum -y install epel-release
RUN yum -y install rpm-build rpmdevtools redhat-rpm-config yum-utils
RUN rpmdev-setuptree
ADD ./build.sh /build.sh
VOLUME /spec_src

