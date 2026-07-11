%global tl_name everyshi
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.00
Release:	%{tl_revision}.1
Summary:	Take action at every \shipout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/everyshi
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everyshi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everyshi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/everyshi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides hooks into \sshipout called \EveryShipout and
\AtNextShipout analogous to \AtBeginDocument. With the introduction of
the LaTeX hook management this package became obsolete in 2020 and is
only provided for backwards compatibility. For current versions of LaTeX
it is only mapping the hooks to the original everyshi macros. In case
you use an older LaTeX format, everyshi will automatically fall back to
its old implementation by loading everyshi-2001-05-15.

