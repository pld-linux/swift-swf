Summary:	Open-source alternative to Adobe Flash
Name:		swift-swf
Version:	11.10.2
Release:	0.1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://launchpad.net/~skykooler/+archive/swift-swf/+files/%{name}_%{version}.tar.gz
# Source0-md5:	387853e28616abd1eeb368e7e58f790c
URL:		http://swift-swf.blogspot.com/
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.7.1
BuildRequires:	python-distutils-extra >=2.18
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.586
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WIFT (which stands for "ShockWave Is Free Territory") is a free,
open-source alternative to Adobe Flash. It is written in Python, and
uses PyGTK for a GUI, swfc for compiling, and Cairo for image
processing. It has the ability to export to HTML5 as well as .swf,
allowing for viewing on non-Flash-compatible devices (such as the
iPhone or the Kindle), and can pack all resources into a single HTML
file for portability. Swift supports ActionScript, allowing for
interactive content creation.

%prep
%setup -q -c

%build
cd trunk
CC=%{__cc} \
CXX=%{__cxx} \
OVERRIDE_CFLAGS="%{rpmcflags}" \
OVERRIDE_LDFLAGS="%{rpmldflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--libdir="%{_libdir}"

%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_postclean %{_libdir}/%{name}

# move manpages and locales to proper place
#mv $RPM_BUILD_ROOT%{_datadir}/%{name}/man $RPM_BUILD_ROOT%{_mandir}
#mv $RPM_BUILD_ROOT%{_datadir}/%{name}/localization/locales $RPM_BUILD_ROOT%{_datadir}/locale

# set proper filenames for locales (TODO: switch to patch if possible)
#for file in $RPM_BUILD_ROOT%{_datadir}/locale/*; do
#	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\).*:\1:')
#	mkdir $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
#	mv $RPM_BUILD_ROOT%{_datadir}/locale/$lang/*.mo \
#	$RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
#done;
#for file in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/messages.mo; do
#	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
#	mv $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/messages.mo \
#	$RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}.mo
#done;
#for file in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/iso639.mo; do
#	lang=$(echo $file|%{__sed} 's:.*locale/\(.*\)/LC_MESSAGES.*:\1:')
#	mv $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/iso639.mo \
#	$RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/%{name}_iso639.mo
#done;
#
#%{__rm} $RPM_BUILD_ROOT%{_bindir}/%{name}-uninstall

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
#%doc Changelog.yaml COPYRIGHT README
#%attr(755,root,root) %{_bindir}/%{name}
#%{_datadir}/%{name}
#%{_libdir}/%{name}
#%{_mandir}/man1/*.1*
