Name:           ros-indigo-kobuki
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS kobuki package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-kobuki-auto-docking
Requires:       ros-indigo-kobuki-bumper2pc
Requires:       ros-indigo-kobuki-capabilities
Requires:       ros-indigo-kobuki-controller-tutorial
Requires:       ros-indigo-kobuki-description
Requires:       ros-indigo-kobuki-keyop
Requires:       ros-indigo-kobuki-node
Requires:       ros-indigo-kobuki-random-walker
Requires:       ros-indigo-kobuki-rapps
Requires:       ros-indigo-kobuki-safety-controller
Requires:       ros-indigo-kobuki-testsuite
BuildRequires:  ros-indigo-catkin

%description
Software for Kobuki, Yujin Robot's mobile research base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Aug 26 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.4-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.3-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.0-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.1-0
- Autogenerated by Bloom

