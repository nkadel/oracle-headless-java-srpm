# Copyright: Nico Kadel-Garcia <nkadel@gmail.com>

Summary: RPM plugin to allow cloudera Oracle Java to replace openjdk
Version: 1.8.0
Name: oracle-j2sd%{version}-headless
Release: 0%{?dist}
License: Java
Group: Development/Tools
URL: http://archive.cloudera.com/director/

Packager: Nico Kadel-Garcia <nkadel@gmail.com>

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: oracle-j2sdk1.8
Provides: 1:java-headless-%{version}
Conflicts: java*openjdk*

%description
%{name} provides the dependency needed for Java dependent components
to operate with the Cloudera packaged Oracle JDK.

%prep
#%setup

#%build

#%install

#%clean
%{__rm} -rf %{buildroot}

%files

%changelog
* Thu Dec 13 2018 Nico Kadel-Garcia <nkadel@gmail.com> - 1.8.0-0
- Initial build

