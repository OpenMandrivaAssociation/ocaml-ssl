Name:           ocaml-ssl
Version:        0.4.4
Release:        %mkrel 2
Summary:        SSL bindings for OCaml

Group:          Development/Other
License:        LGPLv2+ with exceptions
URL:            http://savonet.sourceforge.net/wiki/Savonet
Source0:        http://downloads.sourceforge.net/savonet/ocaml-ssl-%{version}.tar.gz
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


