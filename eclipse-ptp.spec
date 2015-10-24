%{?_javapackages_macros:%_javapackages_macros}

%global eclipse_base            %{_datadir}/eclipse
%global cdtreq                  1:8.1.0
%global pdereq                  1:4.2.0
%global rsereq                  3.5
%global pdebuild                %{_bindir}/eclipse-pdebuild
%global ptp_build_id            201402121320
%global ptp_git_tag             PTP_7_0_4
#global ptp_git_tag             7a7225fc8470b8ec4bc614ff9110d8045fa20a52

# All arches line up except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%ifarch %{arm}
%define eclipse_arch    arm
%else
%define eclipse_arch   %{_arch}
%endif
%endif

Summary:        Eclipse Parallel Tools Platform
Name:           eclipse-ptp
Version:        7.0.4
Release:        1.1
License:        EPL
Group:          Development/Java
URL:            http://www.eclipse.org/ptp

# The following tarballs were downloaded from the git repositories
Source0:        http://git.eclipse.org/c/ptp/org.eclipse.ptp.git/snapshot/org.eclipse.ptp-%{ptp_git_tag}.tar.bz2
# This is made with makesource.sh
#Source0:        org.eclipse.ptp-%{ptp_git_tag}.tar.xz
Source2:        makesource.sh
# To help generate the needed Requires
Source3:        finddeps.sh

# Remove dependency specifications on ant-trax
Patch0:         eclipse-ptp-notrax.patch
# Remove rdt.remotetools from ptp feature
Patch1:         eclipse-ptp-noremote.patch
# Remove extra environments from pom.xml
Patch3:         eclipse-ptp-tycho-build.patch
# Add <repository> for tycho-eclipserun-plugin
Patch5:         eclipse-ptp-repository.patch

# Remove some unneeded dependencies
BuildRequires:  java-devel >= 1.5.0
BuildRequires:  maven-local
# Need tycho-extras for core/org.eclipse.ptp.doc.isv
BuildRequires:  tycho-extras
BuildRequires:  eclipse-cdt-parsers >= %{cdtreq}
#BuildRequires: eclipse-cdt-tests
# >= 1:6.0.2
BuildRequires:  eclipse-jgit
BuildRequires:  eclipse-pde >= %{pdereq}
BuildRequires:  eclipse-photran-intel
BuildRequires:  eclipse-photran-xlf
BuildRequires:  eclipse-rse >= %{rsereq}
BuildRequires:  lpg-java-compat = 1.1.0

Requires:       eclipse-cdt >= %{cdtreq}
# Pulled in by rdt.remotetools being in ptp main
Requires:       %{name}-rdt = %{version}-%{release}
Provides:       %{name}-cdt-compilers = %{version}-%{release}
Obsoletes:      %{name}-cdt-compilers < %{version}-%{release}
Provides:       %{name}-etfw-ppw = %{version}-%{release}
Obsoletes:      %{name}-etfw-ppw < %{version}-%{release}
Provides:       %{name}-gig = %{version}-%{release}
Obsoletes:      %{name}-gig < %{version}-%{release}
Provides:       %{name}-pldt = %{version}-%{release}
Obsoletes:      %{name}-pldt < %{version}-%{release}
Provides:       %{name}-pldt-openacc = %{version}-%{release}
Obsoletes:      %{name}-pldt-openacc < %{version}-%{release}
Provides:       %{name}-rdt-remotetools = %{version}-%{release}
Obsoletes:      %{name}-rdt-remotetools < %{version}-%{release}
Provides:       %{name}-rdt-sdk = %{version}-%{release}
Obsoletes:      %{name}-rdt-sdk < %{version}-%{release}
Provides:       %{name}-rdt-sync = %{version}-%{release}
Obsoletes:      %{name}-rdt-sync < %{version}-%{release}
Provides:       %{name}-rdt-xlc-sdk = %{version}-%{release}
Obsoletes:      %{name}-rdt-xlc-sdk < %{version}-%{release}

%description
The aim of the parallel tools platform project is to produce an open-source
industry-strength platform that provides a highly integrated environment
specifically designed for parallel application development. The project will
provide:

 - a standard, portable parallel IDE that supports a wide range of parallel
   architectures and run-time systems
 - a scalable parallel debugger
 - support for the integration of a wide range of parallel tools
 - an environment that simplifies the end-user interaction with parallel
   systems

This package contains the main PTP run-time features.


%package        master
Summary:        Complete PTP package
Group:          Development/Java
Requires:       eclipse-cdt >= %{cdtreq}
Requires:       %{name} = %{version}-%{release}

#master package is a virtual package that requires all of the components
Requires:       %{name}-etfw-tau = %{version}-%{release}
Requires:       %{name}-etfw-tau-fortran = %{version}-%{release}
Requires:       %{name}-fortran = %{version}-%{release}
Requires:       %{name}-gem = %{version}-%{release}
#Requires:       %{name}-gig = %{version}-%{release}
Requires:       %{name}-pldt-fortran = %{version}-%{release}
Requires:       %{name}-pldt-upc = %{version}-%{release}
Requires:       %{name}-rdt = %{version}-%{release}
Requires:       %{name}-rdt-xlc = %{version}-%{release}
Requires:       %{name}-remote-rse = %{version}-%{release}
Requires:       %{name}-rm-contrib = %{version}-%{release}
Requires:       %{name}-sci = %{version}-%{release}
Requires:       %{name}-sdk = %{version}-%{release}
Requires:       %{name}-sdm = %{version}-%{release}
Requires:       eclipse-photran
Requires:       eclipse-photran-intel
Requires:       eclipse-photran-xlf

%description    master
The package will bring in all of the PTP components.


%package        core-source
Summary:        PTP Core Components Source
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    core-source
Parallel Tools Platform core components source code.


%package        etfw-tau
Summary:        PTP External Tools Framework TAU Support
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    etfw-tau
Extends the external tools framework with capabilities specific
to the TAU performance analysis system.


%package        etfw-tau-fortran
Summary:        PTP External Tools Framework: TAU Fortran Enabler
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name}-etfw-tau = %{version}-%{release}
Requires:       eclipse-photran

%description    etfw-tau-fortran
Adds selective instrumentation functionality for Fortran via the
Photran project.


%package        fortran
Summary:        PTP Fortran Support
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-etfw-tau-fortran = %{version}-%{release}
Requires:       %{name}-pldt-fortran = %{version}-%{release}
Requires:       %{name}-rdt-sync-fortran = %{version}-%{release}
Requires:       eclipse-photran
Requires:       eclipse-photran-intel
Requires:       eclipse-photran-xlf

%description    fortran
Adds Fortran support to PTP.


%package        gem
Summary:        PTP Graphical Explorer of MPI Programs (GEM)
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    gem
GEM serves as a graphical front end for In-situ Partial Order (ISP), a
dynamic formal verification tool for MPI developed at the School of
Computing, University of Utah.

Whether you are new to MPI or are an advanced user, GEM will help you debug
your MPI programs, and graphically show many valuable facts, including all
the possible send/receive matches, and synchronizations. GEM also includes
features to help users understand and debug the program across all platforms
on which it may be run (e.g. highlighting deadlocks that may occur due to
differing communication buffer allocations). For a given test harness, GEM
will allow you to explore only the relevant process interleavings, which are
much smaller than the number of total feasible interleavings. GEM also
guarantees to discover and explore all non-deterministic matches at run-time. 


%if 0
%package        gig
Summary:        PTP Graphical Inquisitor of GPU Programs (GIG)
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    gig
The Graphical Explorer of GPU Programs (GIG) is used to help debug CUDA
programs. It uses the formal verifier GKLEE, developed at the University
of Utah, to automatically detect many errors and problems such as race
conditions, deadlocks, and bank conflicts.  This is all cleanly integratedi
into an easy-to use eclipse plug-in.  GKLEE can be obtained from
http://cs.utah.edu/fv/gklee
%endif


%package        pldt-fortran
Summary:        PTP Parallel Language Development Tools Fortran Support
Group:          Development/Java
BuildArch:      noarch
Requires:       eclipse-cdt-parsers >= %{cdtreq}
Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-photran

%description    pldt-fortran
Adds a range of static analysis and programming assistance tools for Fortran.


%package        pldt-upc
Summary:        PTP Parallel Language Development Tools UPC Support
Group:          Development/Java
BuildArch:      noarch
Requires:       eclipse-cdt-parsers >= %{cdtreq}
Requires:       %{name} = %{version}-%{release}

%description    pldt-upc
Adds a range of static analysis and programming assistance tools for UPC.  
Note: this is separated from the rest of PLDT since it requires the UPC
feature of CDT, which is sometimes not installed with CDT.


%package        rdt
Summary:        PTP Remote Development Tools
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-jgit
Requires:       eclipse-rse >= %{rsereq}

%description    rdt
PTP components for supporting Remote Development Tools.


%package        rdt-sync-fortran
Summary:        PTP Fortran Synchronization Support
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name}-rdt-sync = %{version}-%{release}

%description    rdt-sync-fortran
Adds the ability to remotely synchronize Fortran projects.


%package        rdt-xlc
Summary:        PTP Remote Development Tools XL C/C++ Compiler Support
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name}-rdt = %{version}-%{release}
Requires:       eclipse-cdt-parsers >= %{cdtreq}

%description    rdt-xlc
Remote support for the IBM XL C/C++ compilers.


%package        rm-contrib
Summary:        PTP Contributed Resource Manager Definitions
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    rm-contrib
Adds resource managers for a number of different systems.


%package        sci
Summary:        PTP Scalable Communication Infrastructure (SCI)
Group:          Development/Java
BuildArch:      noarch

%description    sci
Parallel Tools Platform components that implements the Scalable Communication
Infrastructure (SCI).


%package        sdk
Summary:        Parallel Tools Platform SDK 
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name}-core-source = %{version}-%{release}

%description    sdk
Eclipse Parallel Tools Platform. Software development kit including source
code and developer documentation.


%package        sdm
Summary:        PTP Scalable Debug Manager (SDM)
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    sdm
Parallel Tools Platform components that implement a parallel debug server
using the Scalable Debug Manager (SDM).

NOTE: The sdm binary for the architecture of the host machine is available
in the sdm plugin and at %{_libdir}/ptp/sdm.  If the target system is of
a different archicture, you will need to build and install it by hand.


%package        remote-rse
Summary:        PTP RSE Enabler
Group:          Development/Java
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    remote-rse
Provides support for remote services using RSE.


%prep
%setup -q -n org.eclipse.ptp-%{ptp_git_tag}
# Fix tycho version
tychover=$(sed -ne '/<version>/{s/.*>\(.*\)<.*/\1/;p;q}' < /usr/share/maven-fragments/tycho)
sed -i -e "/tycho-version/s/>[0-9].*</>${tychover}</" pom.xml
%patch0 -p1 -b .notrax
%patch1 -p2 -b .noremote
%patch3 -p2 -b .tycho-build
%patch5 -p1 -b .repository
sed -i -e 's/<arch>x86<\/arch>/<arch>%{eclipse_arch}<\/arch>/g' pom.xml
# Remove bundled binaries
rm -r releng/org.eclipse.ptp.linux/os/linux
# Remotejars requires a bunch of downloaded prebuilt stuff
%pom_disable_module rdt/org.eclipse.ptp.rdt.core.remotejars
%pom_disable_module releng/org.eclipse.ptp.rdt.remotejars-feature
# This depends on remotejars
%pom_disable_module rdt/org.eclipse.ptp.rdt.server.dstore
# This depends on rdt.server.dstor
%pom_disable_module releng/org.eclipse.ptp.rdt.remotetools-feature


%build
export JAVA_HOME=%{java_home}
export PATH=/usr/bin:$PATH
export MAVEN_OPTS="-XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState ${MAVEN_OPTS}"
# Build the sdm binary
pushd debug/org.eclipse.ptp.debug.sdm
export CFLAGS="%{optflags}"
sh BUILD
popd
mkdir -p releng/org.eclipse.ptp.linux/os/linux/%{_arch}
cp -p debug/org.eclipse.ptp.debug.sdm/bin/sdm releng/org.eclipse.ptp.linux/os/linux/%{_arch}/sdm
# Build the project
mvn-rpmbuild -DforceContextQualifier=%{ptp_build_id} install


%install
mkdir -p %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/{features,plugins}

# ptp
for jar in releng/org.eclipse.ptp.repo/target/repository/features/*.jar
do
  name=$(basename $jar .jar)
  # Skip photran components
  [ ${name/org.eclipse.photran/} != $name ] && continue
  [ ${name/org.eclipse.rephraserengine/} != $name ] && continue
  unzip -u -d %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name $jar
  if [ $name == org.eclipse.ptp_%{version}.%{ptp_build_id} ]
  then
    # Group the core features
    sed -ne '/id=/s#.*"\(.*\)"#%{eclipse_base}/dropins/ptp/eclipse/features/\1_*#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name/feature.xml | tail -n +2 > files.$name
    # Add the plugins for those features
    sed -ne '/id=/s#.*"\(.*\)"#\1#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name/feature.xml | tail -n +2 | while read f
    do
      [ $f == org.eclipse.ptp ] && continue
      sed -ne '/id=/s#.*"\(.*\)"#%{eclipse_base}/dropins/ptp/eclipse/plugins/\1_*.jar#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/${f}_*/feature.xml | tail -n +2 >> files.$name
    done
    sort -u -o files.$name files.$name
  else
    sed -ne '/id=/s#.*"\(.*\)"#%{eclipse_base}/dropins/ptp/eclipse/plugins/\1_*.jar#gp' %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/features/$name/feature.xml | tail -n +2 > files.$name
  fi
done
cp -u releng/org.eclipse.ptp.repo/target/repository/plugins/*.jar \
   %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/plugins/
# Remove photran plugins
rm %{buildroot}%{eclipse_base}/dropins/ptp/eclipse/plugins/org.eclipse.{photran,rephraserengine}*

# Remove disabled modules from filelist
sed -i -e '\,plugins/org.eclipse.ptp.remote.remotetools_,d' \
       -e '\,plugins/org.eclipse.ptp.remote_,d' \
       -e '\,plugins/org.eclipse.ptp.remotetools_,d' files.*

# Install sdm binary so debuginfo is created
mkdir -p %{buildroot}%{_libdir}/ptp
cp -p debug/org.eclipse.ptp.debug.sdm/bin/sdm %{buildroot}%{_libdir}/ptp/

# cb - rpm5 doesnt handle multiple -f
cat files.org.eclipse.ptp.rdt.editor_%{version}.%{ptp_build_id} >> files.org.eclipse.ptp.rdt_%{version}.%{ptp_build_id}


%files -f files.org.eclipse.ptp_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%dir %{eclipse_base}/dropins/ptp
%dir %{eclipse_base}/dropins/ptp/eclipse
%dir %{eclipse_base}/dropins/ptp/eclipse/features
%dir %{eclipse_base}/dropins/ptp/eclipse/plugins

%files master
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html

%files core-source -f files.org.eclipse.ptp.core.source_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.core.source_*

%files etfw-tau -f files.org.eclipse.ptp.etfw.tau_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.etfw.tau_*

%files etfw-tau-fortran -f files.org.eclipse.ptp.etfw.tau.fortran_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.etfw.tau.fortran_*

%files fortran
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.fortran_*

%files gem -f files.org.eclipse.ptp.gem_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.gem_*

# GIG was disabled for 7.0 release for now
%if 0
%files gig -f files.org.eclipse.ptp.gig_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.gig_*
%endif

%files pldt-fortran -f files.org.eclipse.ptp.pldt.fortran_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.pldt.fortran_*

%files pldt-upc -f files.org.eclipse.ptp.pldt.upc_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.pldt.upc_*

%files rdt -f files.org.eclipse.ptp.rdt_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt_*
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt.editor_*

%files rdt-sync-fortran -f files.org.eclipse.ptp.rdt.sync.fortran_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt.sync.fortran_*

%files rdt-xlc -f files.org.eclipse.ptp.rdt.xlc_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rdt.xlc_*

%files remote-rse -f files.org.eclipse.ptp.remote.rse_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.remote.rse_*

%files rm-contrib -f files.org.eclipse.ptp.rm.jaxb.contrib_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.rm.jaxb.contrib_*

%files sci -f files.org.eclipse.ptp.sci_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.sci_*

%files sdk -f files.org.eclipse.ptp.sdk_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.sdk_*

%files sdm -f files.org.eclipse.ptp.debug.sdm_%{version}.%{ptp_build_id}
%doc releng/org.eclipse.ptp.license-feature/epl-v10.html
%{eclipse_base}/dropins/ptp/eclipse/features/org.eclipse.ptp.debug.sdm_*
%{_libdir}/ptp/


%changelog
* Tue Apr 8 2014 Orion Poplawski <orion@cora.nwra.com> 7.0.4-1
- Update to 7.0.4

* Fri Aug 16 2013 Orion Poplawski <orion@cora.nwra.com> 7.0.3-1
- Update to 7.0.3
- Drop deps patch and sysmon changes - removed upstream

* Sat Aug 3 2013 Orion Poplawski <orion@cora.nwra.com> 7.0.2-1
- Update to 7.0.2

* Tue Jul 23 2013 Krzysztof Daniel <kdaniel@redhat.com> 7.0.1-2
- Fix build on ARM (RHBZ#987438).

* Mon Jul 8 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.1-1
- Update to 7.0.1
- Use bz2 compressed sources
- Drop docbuild patch, fixed upstream
- Drop gig sub-package for now

* Tue May 14 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.6.20130514git845dccd
- Update to latest git
- Fix requires corruption

* Sat May 11 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.5.20130511git71cc5a7
- Update to latest git

* Fri May 10 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.5.20130510gitd11d96c
- Update to latest git

* Tue May 7 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.4.20130502gitbd8fbd1
- Drop tycho-extras repository sed - fixed in tycho-extras-0.17.0-2

* Mon May 6 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.3.20130502gitbd8fbd1
- Add patch to add repository info for tycho-eclipserun-plugin
- Add patch and sed to fix doc.isv build

* Thu May 2 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.3.20130502gitbd8fbd1
- Update to latest git
- Drop photran build - now in separate package
- Add patch to fix parent pom paths

* Tue Apr 23 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.2.20130422git
- Update to git master
- Build sdm executable and install it so that debuginfo is generated

* Tue Apr 9 2013 Orion Poplawski <orion@cora.nwra.com> - 7.0.0-0.1.20130409git
- Update to git master

* Mon Apr 8 2013 Orion Poplawski <orion@cora.nwra.com> - 6.0.5-1
- Update to PTP 6.0.5, photran 8.0.5
- Remove rdt.remotetools feature beause we are unable to build
  remotejars
- Hande tycho versions automatically

* Fri Feb 8 2013 Alexander Kurtakov <akurtako@redhat.com> 6.0.3-4
- Remove a lot of old stuff.

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 6.0.3-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Feb 4 2013 Orion Poplawski <orion@cora.nwra.com> - 6.0.3-2
- Obsolete/Provide pldt-openacc

* Tue Nov 6 2012 Orion Poplawski <orion@cora.nwra.com> - 6.0.3-1
- Update to PTP 6.0.3, photran 8.0.3
- Use maven/tycho for building, major rework of spec
- Add patch remove ant-trax dependency, fix maven jdk tools.jar dep
- Drop overrides patch
- Move pldt and rdt-sync into the main package
- Add fortran meta sub-package to bring in Fortran support
- Drop cdt-compilers, rdt-sdk, and rdt-xlc-sdk sub-packages

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-0.3.junom6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Orion Poplawski <orion@cora.nwra.com> - 6.0.0-0.2.junom6
- Add some new features
- Rework buildid to avoid photran build duplication

* Thu Apr 19 2012 Jeff Johnston <jjohnstn@redhat.com> - 6.0.0-0.1.junom6
- Update to PTP Juno M6 (6.0.0 pre-release)

* Fri Apr 13 2012 Orion Poplawski <orion@cora.nwra.com> - 5.0.7-1
- Update to PTP 5.0.7, photran 7.0.7
- Add %%{pdebuild} macro

* Tue Mar 13 2012 Orion Poplawski <orion@cora.nwra.com> - 5.0.6-1
- Update to PTP 5.0.6, photran 7.0.6

* Fri Feb 17 2012 Orion Poplawski <orion@cora.nwra.com> - 5.0.5-1
- Update to PTP 5.0.5, photran 7.0.5

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Orion Poplawski <orion@cora.nwra.com> - 5.0.4-1
- Update to PTP 5.0.4, photran 7.0.4
- Add pldt-fortran and rm-contrib sub-packages
- Update makesource.sh/spec/finddeps.sh to use git archive
- Unpack cdtdb-4.0.3-eclipse.jar from tar archive
- Remove orbitDeps usage, not needed
- Remove license feature hack, not needed
- Drop defattr, BuildRoot, clean
- Actually build master package

* Tue Oct 25 2011 Orion Poplawski <orion@cora.nwra.com> - 5.0.3-1
- Update to PTP 5.0.3, photran 7.0.3

* Thu Oct 20 2011 Orion Poplawski <orion@cora.nwra.com> - 5.0.2-1
- Update to PTP 5.0.2, photran 7.0.2
- Update deps patch
- Add jaxb to feature build before ptp

* Tue Sep 6 2011 Orion Poplawski <orion@cora.nwra.com> - 5.0.1-2
- Fixup some dependencies

* Wed Aug 31 2011 Orion Poplawski <orion@cora.nwra.com> - 5.0.1-1
- Update to PTP 5.0.1, photran 7.0.1
- Bump CDT and PDE requirement
- Work around issue with pdebuild shared license feature
- Add BR on ws-jaxme, add jaxmeapi and xml-commons-apis to orbitDeps
- Add patch to remove unneeded dependencies
- Add BR on eclipse-jgit
- Add sdk and photran components to ptp-master
- Add rdt-sync, rdt-sync-fortran, and sdk sub-packages
- Fixup some requires
- Improve the finddeps.sh utility script

* Wed May 18 2011 Orion Poplawski <orion@cora.nwra.com> - 4.0.7-1
- Update to PTP 4.0.7, photran 6.0.7

* Wed Mar 2 2011 Orion Poplawski <orion@cora.nwra.com> - 4.0.6-1
- Update to PTP 4.0.6, photran 6.0.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.5-1
- Update to PTP 4.0.5, photran 6.0.5

* Fri Nov 5 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.4-1
- Update to PTP 4.0.4, photran 6.0.4

* Fri Oct 8 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-3
- Fix photran cdt requirement

* Mon Sep 27 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-2
- Make rdt provide/obsolete rdt-remotetools

* Mon Sep 20 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-1
- Update to PTP 4.0.3, photran 6.0.3
- Drop rdt-remotetools now part of rdt

* Fri Sep 3 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-0.3.RC2c
- Fix changelog version

* Thu Sep 2 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-0.2.RC2b
- Fix remote-rse deps

* Wed Sep 1 2010 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-0.1.v201009010938
- Update snapshot
- Re-work build

* Tue Jun 1 2010 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-0.1.v201004302110
- Update snapshot
- Add patch from cvs to fix exception in MPI project wizard

* Fri May 28 2010 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-1
- Update to 3.0.1 final
- Rework dependencies

* Mon Feb 1 2010 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-0.4.v201002011019
- Update snapshot

* Tue Jan 26 2010 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-0.3.v201001251825
- Update snapshot

* Thu Jan 21 2010 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-0.2.v201001152110
- Make photran versions 5.0.1, rephraserengine 1.0.1

* Thu Jan 21 2010 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-0.1.v201001152110
- Update to 3.0.1 snapshot
- Split package
- Make noarch

* Mon Dec 7 2009 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-1
- Update to 3.0.0 final

* Wed Nov 11 2009 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.5.200911091447
- Update to 200911091447

* Tue Oct 27 2009 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.4.200910232110
- Update to 200910232110

* Thu Oct 22 2009 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.3.200910162113
- Update to 200910162113

* Fri Oct 16 2009 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.2.200910091648
- Remove gcj - eclipse is not built with it.

* Thu Oct 15 2009 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.1.200910091648
- Initial package
