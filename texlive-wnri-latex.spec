# revision 22338
# category Package
# catalog-ctan /macros/latex/contrib/wnri-latex
# catalog-date 2011-05-06 00:56:07 +0200
# catalog-license gpl2
# catalog-version 1.0b
Name:		texlive-wnri-latex
Version:	1.0b
Release:	2
Summary:	LaTeX support for wnri fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/wnri-latex
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX support for the fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/wnri-latex/ot1wnr.fd
%{_texmfdistdir}/tex/latex/wnri-latex/ot1wnss.fd
%{_texmfdistdir}/tex/latex/wnri-latex/ot1wntt.fd
%{_texmfdistdir}/tex/latex/wnri-latex/wnri.def
%{_texmfdistdir}/tex/latex/wnri-latex/wnri.sty
%doc %{_texmfdistdir}/doc/latex/wnri-latex/README
%doc %{_texmfdistdir}/doc/latex/wnri-latex/wnri.pdf
%doc %{_texmfdistdir}/doc/latex/wnri-latex/wnritest.tex
#- source
%doc %{_texmfdistdir}/source/latex/wnri-latex/wnri.dtx
%doc %{_texmfdistdir}/source/latex/wnri-latex/wnri.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
