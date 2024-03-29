Summary:	Utilities for dealing with MTD (flash) devices
Name:		mtd-utils
Version:	2.1.2
Release:	2
License:	GPLv2+
Group:		Development/Other
URL:		http://www.linux-mtd.infradead.org
Source0:	ftp://ftp.infradead.org/pub/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(lzo2)
BuildRequires:	pkgconfig(libacl)

%description
The mtd-utils package contains utilities related to handling MTD devices,
and for dealing with FTL, NFTL JFFS2 etc.

%package ubi
Summary:	Utilities for dealing with UBI
Group:		Development/Other

%description ubi
The mtd-utils-ubi package contains utilities for manipulating UBI on
MTD (flash) devices.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING
%{_sbindir}/doc*
%{_sbindir}/flash*
%{_sbindir}/ftl*
%{_sbindir}/jffs2dump
%{_sbindir}/jffs2reader
%{_sbindir}/mkfs.jffs2
%{_sbindir}/*mtd*
%{_sbindir}/nand*
%{_sbindir}/nftl*
%{_sbindir}/recv_image
%{_sbindir}/rfd*
%{_sbindir}/serve_image
%{_sbindir}/sumtool
%{_mandir}/*/*

%files ubi
%{_sbindir}/mkfs.ubifs
%{_sbindir}/ubi*
