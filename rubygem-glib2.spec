%define rb_ver 2.7.0

Summary:	Ruby binding of GLib-2.x
Name:		rubygem-glib2

Version:	3.4.9
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/glib2-%{version}.gem
Patch0:		rbg_gc_marker_new.patch
BuildRequires:	rubygem-pkg-config
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  rubygem-native-package-installer
Obsoletes:      ruby-glib2 = 3.0.7

%description
Ruby binding of GLib-2.x.


%package    devel
Summary:    Development files for %{name}
Group:      Development/Ruby

%description	devel
Development files for %{name}

%prep
%autosetup -p1 -n %{gem_name}-%{version}

%build
%gem_build 

%install
%gem_install

%files
%exclude %{gem_instdir}/ext/%{gem_name}/*.o
%exclude %{gem_instdir}/ext/%{gem_name}/*.c
%exclude %{gem_instdir}/ext/%{gem_name}/*.h
%exclude %{gem_instdir}/extensions/x86_64-linux/%{rb_ver}/%{gem_name}-%{version}/*.h
%exclude %{gem_instdir}/ext/%{gem_name}/ruby-glib2.pc
%{gem_files}

%files  devel
%{gem_instdir}/ext/%{gem_name}/*.h
%{gem_instdir}/ext/%{gem_name}/ruby-glib2.pc
