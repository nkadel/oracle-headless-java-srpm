oracle-j2sdk1.8.0-headless-srpm
===============================

This is a plugin to allow the Cloudera published rewrap of the Oracle
1.8.0 JDK to satisfy dependencies for other RHEL packages, and to
block installation of openjdk or the distinct Oracle jdk package.
This plugin should be installed along with the Cloudera RPM, to avoid
other conflicts.

It does *not* provide /etc/alternatives handling: setting the PATH to
include the installed Cloudera JDK or setting JAVA_HOME is an exercise
for the user. That need is usually handled by providing a valid
/etc/profile.d/jdk.sh, but I've not attempted to provide one here.

Nico Kadel-Garcia <nkadel@gmail.com>