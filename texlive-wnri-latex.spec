%global tl_name wnri-latex
%global tl_revision 22338

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0b
Release:	%{tl_revision}.1
Summary:	LaTeX support for wnri fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wnri-latex
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX support for the wnri fonts.

