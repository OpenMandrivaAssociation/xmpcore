%{?_javapackages_macros:%_javapackages_macros}
Name:          xmpcore
Version:       5.1.2
Release:       2.1
Summary:       Java XMP Library
Group:         Development/Java
License:       BSD
URL:           http://www.adobe.com/devnet/xmp.html
Source0:       http://repo1.maven.org/maven2/com/adobe/xmp/%{name}/%{version}/%{name}-%{version}-sources.jar
# from http://repo1.maven.org/maven2/com/adobe/xmp/xmpcore/5.1.2/xmpcore-5.1.2.pom
# customized:
# fix compiler,javadoc-plugin configuration
# fix manifest entries
Source1:       %{name}-%{version}.pom
# from http://download.macromedia.com/pub/developer/xmp/sdk/XMP-Toolkit-SDK-5.1.2.zip
Source2:       %{name}-BSD-License.txt

BuildRequires: java-devel
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-local
BuildArch:     noarch

%description
The XMP Library for Java is based on the
C++ XMPCore library and the API is similar.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

mkdir java
mv com java/
rm -r META-INF

cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} BSD-License.txt
sed -i 's/\r//' BSD-License.txt

%build

%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc BSD-License.txt

%files javadoc -f .mfiles-javadoc
%doc BSD-License.txt

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 gil cattaneo <puntogil@libero.it> 5.1.2-1
- initial rpm
