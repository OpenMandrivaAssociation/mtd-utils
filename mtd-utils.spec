Summary: Utilities for dealing with MTD (flash) devices
Name: mtd-utils
Version: 1.2.0
Release: %mkrel 1
License: GPLv2+
Group: Development/Other
URL: http://www.linux-mtd.infradead.org
Source0: ftp://ftp.infradead.org/pub/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires: zlib-devel
BuildRequires: liblzo-devel
BuildRequires: acl-devel

%description
The mtd-utils package contains utilities related to handling MTD devices,
and for dealing with FTL, NFTL JFFS2 etc.

%package ubi
Summary: Utilities for dealing with UBI
Group: Development/Other

%description ubi
The mtd-utils-ubi package contains utilities for manipulating UBI on 
MTD (flash) devices.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING device_table.txt
%{_sbindir}/bin2nand
%{_sbindir}/doc*
%{_sbindir}/flash*
%{_sbindir}/ftl*
%{_sbindir}/jffs2dump
%{_sbindir}/mkbootenv
%{_sbindir}/mkfs.jffs2
%{_sbindir}/mtd_debug
%{_sbindir}/nand*
%{_sbindir}/nftl*
%{_sbindir}/recv_image
%{_sbindir}/rfd*
%{_sbindir}/serve_image
%{_sbindir}/sumtool
%{_mandir}/*/*

%files ubi
%{_sbindir}/mkpfi
%{_sbindir}/pddcustomize
%{_sbindir}/pfi*
%{_sbindir}/unubi
%{_sbindir}/ubi*

