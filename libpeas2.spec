%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define _disable_ld_no_undefined 1

%define oname peas2
%define api 2.0
%define major 0
%define libname %mklibname %{oname}
%define devname %mklibname %{oname} -d
%define girname %mklibname %{oname}-gir

Summary:	Library for plugin handling
Name:		libpeas2
Version:	2.2.0
Release:	2
Group:		System/Libraries
License:	LGPLv2+
Url:		https://www.gnome.org/
Source0:	https://download.gnome.org/sources/libpeas/%{url_ver}/libpeas-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gladeui-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(python)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  luajit
BuildRequires:	vala
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:  pkgconfig(mozjs-140)

%description
This is GNOME's plugin handling library.

#---------------------------------------------------------------------------

%package data
Summary:	Library for plugin handling - data files
Group:		System/Libraries

%description data
This is GNOME's plugin handling library - data files

%files data -f libpeas-2.lang
%doc AUTHORS

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library plugin handling
Group:		System/Libraries
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{libname}
This is GNOME's plugin handling library.

%files -n %{libname}
%{_libdir}/libpeas-2.so.%{major}*
%{_libdir}/libpeas-2/loaders/libgjsloader.so
%{_libdir}/libpeas-2/loaders/libpythonloader.so

#---------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Peas-2.typelib

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{devname}
%{_includedir}/libpeas-2/
%{_libdir}/libpeas-2.so
%{_libdir}/pkgconfig/libpeas-2.pc
%{_datadir}/gir-1.0/Peas-2.gir
#---------------------------------------------------------------------------

%prep
%setup -q -n libpeas-%{version}
%autopatch -p1

%build
%meson  \
        -Dlua51=false \
        -Dvapi=true
%meson_build

%install
%meson_install

%find_lang libpeas-2 %{?no_lang_C}
