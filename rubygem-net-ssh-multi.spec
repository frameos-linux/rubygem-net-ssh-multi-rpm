# Generated from net-ssh-multi-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname net-ssh-multi
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Control multiple Net::SSH connections via a single interface
Name: rubygem-%{gemname}
Version: 1.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://net-ssh.rubyforge.org/multi
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(net-ssh) >= 1.99.2
Requires: rubygem(net-ssh-gateway) >= 0.99.0
Requires: rubygem(echoe) >= 0
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Control multiple Net::SSH connections via a single interface


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/lib/net/ssh/multi/channel.rb
%doc %{geminstdir}/lib/net/ssh/multi/channel_proxy.rb
%doc %{geminstdir}/lib/net/ssh/multi/dynamic_server.rb
%doc %{geminstdir}/lib/net/ssh/multi/pending_connection.rb
%doc %{geminstdir}/lib/net/ssh/multi/server.rb
%doc %{geminstdir}/lib/net/ssh/multi/server_list.rb
%doc %{geminstdir}/lib/net/ssh/multi/session.rb
%doc %{geminstdir}/lib/net/ssh/multi/session_actions.rb
%doc %{geminstdir}/lib/net/ssh/multi/subsession.rb
%doc %{geminstdir}/lib/net/ssh/multi/version.rb
%doc %{geminstdir}/lib/net/ssh/multi.rb
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct 24 2011 Sergio Rubio <rubiojr@frameos.org> - 1.1-1
- Update to 1.1

* Tue Apr 12 2011 Sergio Rubio <rubiojr@frameos.org> - 1.0.1-1
- Initial package
