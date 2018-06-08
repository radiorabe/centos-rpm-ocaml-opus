Name:     ocaml-opus

Version:  0.1.2
Release:  1
Summary:  OCaml bindings for opus
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-opus
Source0:  https://github.com/savonet/ocaml-opus/releases/download/%{version}/ocaml-opus-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ogg
BuildRequires: opus-devel
Requires:      opus

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
/usr/lib64/ocaml/opus/META
/usr/lib64/ocaml/opus/opus.a
/usr/lib64/ocaml/opus/opus.cma
/usr/lib64/ocaml/opus/opus.cmi
/usr/lib64/ocaml/opus/opus.cmxa
/usr/lib64/ocaml/opus/opus.mli
/usr/lib64/ocaml/opus/ogg_demuxer_opus_decoder.cmi
/usr/lib64/ocaml/opus/ogg_demuxer_opus_decoder.cmx
/usr/lib64/ocaml/opus/ogg_demuxer_opus_decoder.mli
/usr/lib64/ocaml/opus/opus.cmx
/usr/lib64/ocaml/opus/libopus_stubs.a
/usr/lib64/ocaml/stublibs/dllopus_stubs.so
/usr/lib64/ocaml/stublibs/dllopus_stubs.so.owner

%description
OCAML bindings for opus


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-opus.spec
