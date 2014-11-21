Name:           ros-indigo-kobuki-node
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS kobuki_node package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_node
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-angles
Requires:       ros-indigo-capabilities
Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-ecl-exceptions
Requires:       ros-indigo-ecl-sigslots
Requires:       ros-indigo-ecl-streams
Requires:       ros-indigo-ecl-threads
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-kobuki-driver
Requires:       ros-indigo-kobuki-ftdi
Requires:       ros-indigo-kobuki-keyop
Requires:       ros-indigo-kobuki-msgs
Requires:       ros-indigo-kobuki-rapps
Requires:       ros-indigo-kobuki-safety-controller
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-ecl-exceptions
BuildRequires:  ros-indigo-ecl-sigslots
BuildRequires:  ros-indigo-ecl-streams
BuildRequires:  ros-indigo-ecl-threads
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-kobuki-driver
BuildRequires:  ros-indigo-kobuki-ftdi
BuildRequires:  ros-indigo-kobuki-keyop
BuildRequires:  ros-indigo-kobuki-msgs
BuildRequires:  ros-indigo-kobuki-safety-controller
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf

%description
ROS nodelet for Kobuki: ROS wrapper for the Kobuki driver.

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
* Fri Nov 21 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.4-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.4-1
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.3-0
- Autogenerated by Bloom

* Mon Aug 11 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.0-0
- Autogenerated by Bloom

* Fri Aug 08 2014 Daniel Stonier <stonier@yujinrobot.com> - 0.6.1-0
- Autogenerated by Bloom

