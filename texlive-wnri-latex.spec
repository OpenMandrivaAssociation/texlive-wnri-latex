Name:		texlive-wnri-latex
Version:	22338
Release:	2
Summary:	LaTeX support for wnri fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wnri-latex
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wnri-latex.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
