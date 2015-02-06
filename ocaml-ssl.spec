Name:           ocaml-ssl
Version:        0.4.6
Release:        2
Summary:        SSL bindings for OCaml

Group:          Development/Other
License:        LGPLv2+ with exceptions
URL:            http://savonet.sourceforge.net/wiki/Savonet
Source:        http://sourceforge.net/projects/savonet/files/ocaml-ssl/%{version}/ocaml-ssl-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.1
BuildRequires:  ocaml-findlib
BuildRequires:  openssl-devel
BuildRequires:  gawk
Requires:       openssl

%description
SSL bindings for OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

# Copy the examples to the docdir.
mkdir -p %{buildroot}%{_docdir}/%{name}-devel-%{version}/examples
cp examples/*.ml %{buildroot}%{_docdir}/%{name}-devel-%{version}/examples

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING README
%{_libdir}/ocaml/ssl
%exclude %{_libdir}/ocaml/ssl/*.a
%exclude %{_libdir}/ocaml/ssl/*.cmxa
%exclude %{_libdir}/ocaml/ssl/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%defattr(-,root,root,-)
%{_libdir}/ocaml/ssl/*.a
%{_libdir}/ocaml/ssl/*.cmxa
%{_libdir}/ocaml/ssl/*.mli
%{_docdir}/%{name}-devel-%{version}/




%changelog
* Fri Sep 16 2011 Alexandre Lissy <alissy@mandriva.com> 0.4.5-3
+ Revision: 700030
- Updating sources to latest 0.4.5
- Release bump, rebuilding against latest ocaml

* Fri Apr 16 2010 Funda Wang <fwang@mandriva.org> 0.4.4-2mdv2011.0
+ Revision: 535264
- rebuild for openssl

* Wed Mar 17 2010 Florent Monnier <blue_prawn@mandriva.org> 0.4.4-1mdv2010.1
+ Revision: 522812
- update to new version 0.4.4

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.3-3mdv2010.1
+ Revision: 496363
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.3-2mdv2010.0
+ Revision: 389925
- rebuild

* Tue Feb 03 2009 Florent Monnier <blue_prawn@mandriva.org> 0.4.3-1mdv2009.1
+ Revision: 337170
- updated version

* Tue Jan 06 2009 Florent Monnier <blue_prawn@mandriva.org> 0.4.2-1mdv2009.1
+ Revision: 326276
- import ocaml-ssl

