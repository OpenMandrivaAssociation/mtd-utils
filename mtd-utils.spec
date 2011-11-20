Summary:	Utilities for dealing with MTD (flash) devices
Name:		mtd-utils
Version:	1.4.8
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		http://www.linux-mtd.infradead.org
Source0:	ftp://ftp.infradead.org/pub/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:	zlib-devel
BuildRequires:	libuuid-devel
BuildRequires:	liblzo-devel
BuildRequires:	acl-devel

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
%make

%install
%makeinstall_std

%files
%doc COPYING device_table.txt
%{_sbindir}/doc*
%{_sbindir}/flash*
%{_sbindir}/mtdinfo
%{_sbindir}/ftl*
%{_sbindir}/jffs2dump
%{_sbindir}/jffs2reader
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
%{_sbindir}/mkfs.ubifs
%{_sbindir}/ubiattach
%{_sbindir}/ubicrc32
%{_sbindir}/ubidetach
%{_sbindir}/ubiformat
%{_sbindir}/ubiupdatevol
%{_sbindir}/ubirsvol
%{_sbindir}/ubirmvol
%{_sbindir}/ubirename
%{_sbindir}/ubinize
%{_sbindir}/ubinfo
%{_sbindir}/ubimkvol

