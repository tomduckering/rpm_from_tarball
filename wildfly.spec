%global __os_install_post %{nil}

Name: wildfly
Summary: The JBoss Application Server
Version: 10.1.0
Release: 1
License: GPL
Group: Java/Middleware
Source: http://download.jboss.org/wildfly/10.1.0.Final/wildfly-10.1.0.Final.tar.gz
URL: http://wildfly.org
Distribution: NoDistro
Vendor: Tom Duckering
Packager: Tom Duckering <tom.duckering@gmail.com>
Requires: java => 1.8.0

%description
WildFly,formerly known as JBoss AS, or simply JBoss, is an application server authored by JBoss, now developed by Red Hat. WildFly is written in Java, and implements the Java Platform, Enterprise Edition (Java EE) specification

%prep
%setup -n %{name}-%{version}.Final

%build
#No compilation step

%install
install -d $RPM_BUILD_ROOT/opt/wildfly
cp -aR $RPM_BUILD_DIR/%{name}-%{version}.Final $RPM_BUILD_ROOT/opt/
mv $RPM_BUILD_ROOT/opt/%{name}-%{version}.Final $RPM_BUILD_ROOT/opt/%{name}-%{version}

%files
/opt/%{name}-%{version}

