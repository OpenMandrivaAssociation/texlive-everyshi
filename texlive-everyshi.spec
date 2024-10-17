Name:		texlive-everyshi
Version:	57001
Release:	2
Summary:	Take action at every \shipout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/everyshi
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyshi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyshi.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/everyshi.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides hooks into \sshipout called \EveryShipout
and \AtNextShipout analogous to \AtBeginDocument. With the
introduction of the LaTeX hook management this package became
obsolete in 2020 and is only provided for backwards
compatibility. For current versions of LaTeX it is only mapping
the hooks to the original everyshi macros. In case you use an
older LaTeX format, everyshi will automatically fall back to
its old implementation by loading everyshi-2001-05-15.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/everyshi
%{_texmfdistdir}/tex/latex/everyshi
%doc %{_texmfdistdir}/doc/latex/everyshi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
