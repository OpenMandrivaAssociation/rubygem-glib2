
%define	gem_name	glib2

Summary:	Ruby binding of GLib-2.x
Name:		rubygem-%{gem_name}

Version:	3.4.1
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems
BuildRequires:	rubygems-devel 
BuildRequires:	rubygem(pkg-config)
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  rubygem-native-package-installer
Obsoletes:      ruby-glib2 = 3.0.7

%description
Ruby binding of GLib-2.x.

%package	doc
Summary:	Documentation for %{name}
Group:		Development/Ruby
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%package    devel
Summary:    Development files for %{name}
Group:      Development/Ruby

%description	devel
Development files for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_extdir_mri}

#/bin/rm -r .%{gem_instdir}/ext/

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so,*.h} \
    %{buildroot}/%{gem_extdir_mri}/


%files
%{gem_instdir}/lib/*.rb
%{gem_instdir}/lib/%{gem_name}/*.rb
%{gem_instdir}/lib/gnome2
%{gem_instdir}/*.rb
%{gem_instdir}/sample/*.rb
%{gem_spec}
%{gem_instdir}/glib2.gemspec
%{gem_instdir}/test/*.rb
%{gem_cache}
%{gem_extdir_mri}/%{gem_name}.so 
%{gem_extdir_mri}/gem.build_complete
%{gem_instdir}/Rakefile

/usr/lib/debug/%{gem_instdir}/ext/%{gem_name}/glib2.so-3.4.1-2.x86_64.debug
%{gem_instdir}/ext/%{gem_name}/.sitearchdir.time
%{gem_instdir}/ext/%{gem_name}/Makefile
%{gem_instdir}/ext/%{gem_name}/depend
%{gem_instdir}/ext/%{gem_name}/extconf.rb
%{gem_instdir}/ext/%{gem_name}/glib2.def
%{gem_instdir}/ext/%{gem_name}/glib2.so

%exclude %{gem_instdir}/ext/%{gem_name}/*.o

%files doc
%doc %{gem_docdir}/rdoc/*
%doc %{gem_docdir}/ri/*
%doc %{gem_instdir}/[A-Z]*

%files  devel
%{gem_extdir_mri}/*.h
%{gem_instdir}/ext/%{gem_name}/*.c
%{gem_instdir}/ext/%{gem_name}/*.h
%{gem_instdir}/ext/%{gem_name}/ruby-glib2.pc

