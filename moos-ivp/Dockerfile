FROM ubuntu:23.04
# Download dependencies as establised in ONENote
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install cmake subversion wget nano
RUN apt-get -y install fltk1.3-dev xterm libfltk1.3-dev  freeglut3-dev  libpng-dev  libjpeg-dev
RUN apt-get -y install libxft-dev  libxinerama-dev   libtiff5-dev
RUN apt-get -y install libprotobuf-dev protobuf-compiler libboost-dev libsdl2-dev socat

# Many of these are repeated and excluded. We run the second line
#RUN apt-get install gpp subversion cmake build-essential libprotobuf-dev protobuf-compiler libboost-all-dev libb64-dev -y
RUN apt-get -y install gpp build-essential libboost-all-dev libb64-dev

#I get errors with these apt-get dependencies and have exluded them:
# RUN apt-get install netcat libtiff5

# Installing MOOS-Ivp
WORKDIR root/moos-ivp
RUN svn --non-interactive --trust-server-cert co https://oceanai.mit.edu/svn/moos-ivp-aro/trunk/ .
RUN ./build-moos.sh
RUN ./build-ivp.sh

# Import PATH modifications and concatenate into to .bashrc
ADD bashrc_mods.txt  ./bashrc_mods.txt
RUN cat bashrc_mods.txt >> ~/.bashrc
RUN rm bashrc_mods.txt

# Some utility aliases as home comforts
# throw an error for some reason

RUN echo 'alias cdd="cd .."' >> ~/.bash_profile
RUN echo 'alias cdd="cd ../.."' >> ~/.bash_profile
RUN echo 'alias cdddd="cd ../../.."' >> ~/.bash_profile
RUN echo 'alias cddddd="cd ../../../.."' >> ~/.bash_profile
