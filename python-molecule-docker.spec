%global debug_package %{nil}

Name: python-molecule-docker
Epoch: 100
Version: 1.0.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Molecule Docker Driver
License: MIT
URL: https://github.com/ansible-community/molecule-docker/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-molecule-docker
Summary: Molecule Docker Driver
Requires: python3
Requires: python3-ansible-compat >= 0.5.0
Requires: python3-docker >= 4.3.1
Requires: python3-molecule >= 3.4.0
Requires: python3-requests
Requires: python3-selinux
Provides: python3-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-docker) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-molecule-docker
Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

%files -n python%{python3_version_nodots}-molecule-docker
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-molecule-docker
Summary: Molecule Docker Driver
Requires: python3
Requires: python3-ansible-compat >= 0.5.0
Requires: python3-docker >= 4.3.1
Requires: python3-molecule >= 3.4.0
Requires: python3-requests
Requires: python3-selinux
Provides: python3-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-docker) = %{epoch}:%{version}-%{release}

%description -n python3-molecule-docker
Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

%files -n python3-molecule-docker
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-molecule-docker
Summary: Molecule Docker Driver
Requires: python3
Requires: python3-ansible-compat >= 0.5.0
Requires: python3-docker >= 4.3.1
Requires: python3-molecule >= 3.4.0
Requires: python3-requests
Requires: python3-libselinux
Provides: python3-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python3dist(molecule-docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(molecule-docker) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-molecule-docker = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(molecule-docker) = %{epoch}:%{version}-%{release}

%description -n python3-molecule-docker
Molecule Docker Plugin is designed to allow use docker containers for
provisioning test resources.

%files -n python3-molecule-docker
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
