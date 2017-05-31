cd /root/rpmbuild

#Copy spec file into generic location
cp $1 /root/rpmbuild/SPECS/build.spec

#Fetch sources
spectool -g -R SPECS/build.spec

#Install build dependencies
yum-builddep -y SPECS/build.spec

#Install build the binary package
rpmbuild -bb SPECS/build.spec
