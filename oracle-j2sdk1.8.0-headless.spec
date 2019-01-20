# Copyright: Nico Kadel-Garcia <nkadel@gmail.com>

Summary: RPM plugin to allow cloudera Oracle Java to replace openjdk
Version: 1.8.0
Name: oracle-j2sd%{version}-headless
Release: 0.1%{?dist}
License: Java
Group: Development/Tools
URL: http://archive.cloudera.com/director/

Packager: Nico Kadel-Garcia <nkadel@gmail.com>

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: oracle-j2sdk1.8
Provides: 1:java-headless = 1:%{version}
Provides: 1:java-devel = 1:%{version}
Conflicts: java*openjdk*

%description
%{name} provides the dependency needed for Java dependent components
to operate with the Cloudera packaged Oracle JDK.

%prep
#%setup

%build
true

%install
true

%clean
%{__rm} -rf %{buildroot}

%files

%changelog
* Sun Jan 20 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.8.0-0.1
- Provide java-devel for more 
- Use 1:version instead of version
- Provide "true" hooks for build and install to avoid spurious build errors

* Thu Dec 13 2018 Nico Kadel-Garcia <nkadel@gmail.com> - 1.8.0-0
- Initial build

