Summary:	Cairo/GTK+ Canvas
Name:		goocanvas
Version:	1.0.0
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goocanvas/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	4858a22239e45cf374195bae520021c2
URL:		http://sourceforge.net/projects/goocanvas/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GooCanvas is a new canvas widget for GTK+ that uses the Cairo 2D
library for drawing. It has a model/view split, and uses interfaces
for canvas items and views, so you can easily turn any application
object into canvas items.

%package devel
Summary:	Header files for goocanvas
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for goocanvas.

%package apidocs
Summary:	goocanvas API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
goocanvas API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libgoocanvas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgoocanvas.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgoocanvas.so
%{_libdir}/libgoocanvas.la
%{_includedir}/goocanvas-1.0
%{_pkgconfigdir}/goocanvas.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/goocanvas

