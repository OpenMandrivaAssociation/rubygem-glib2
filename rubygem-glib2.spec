
%define	gem_name	glib2

Summary:	Ruby binding of GLib-2.x
Name:		rubygem-%{gem_name}

Version:	3.4.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems
BuildRequires:	rubygems-devel 
BuildRequires:	rubygem(pkg-config)
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(glib-2.0)
Obsoletes:      ruby-glib2

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
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_archdir}

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

cp -a .%{gem_archdir}/* \
    %{buildroot}/%{gem_archdir}/

/bin/rm -r %{buildroot}/%{gem_dir}/gems/%{gem_name}-%{version}/ext/


%files
%{gem_dir}/gems/%{gem_name}-%{version}/lib/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/%{gem_name}/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/gnome2
%{gem_dir}/gems/%{gem_name}-%{version}/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/*gemspec
%{gem_dir}/gems/%{gem_name}-%{version}/sample/*.rb
%{gem_dir}/specifications/%{gem_name}-%{version}*.gemspec
%{gem_dir}/gems/%{gem_name}-%{version}/test/*.rb
%{gem_dir}/cache/*.gem

%{gem_extdir_mri}/%{gem_name}.so                                                                                                                                                                                 

%exclude %{gem_extdir_mri}/gem_make.out
%exclude %{gem_extdir_mri}/mkmf.log
%exclude %{gem_extdir_mri}/gem.build_complete
%exclude %{gem_dir}/gems/%{gem_name}-%{version}/Rakefile

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}/rdoc/*
%doc %{gem_dir}/doc/%{gem_name}-%{version}/ri/*
%doc %{gem_dir}/gems/%{gem_name}-%{version}/[A-Z]*

%files  devel                                                                                                                                                                                                  
%{gem_extdir_mri}/*.h



