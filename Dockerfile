# Use a base image (CentOS in this case)
FROM centos:7

# Update the package manager and install necessary packages
RUN yum -y update && \
    yum -y install python3 wget gtk2-devel gtk3-devel epel-release && \
    yum -y groupinstall "Development Tools" && \
    yum -y install python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install opencv-python-headless==4.2.0.34 && \
    pip3 install flask

# Download and install CMake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.21.2/cmake-3.21.2-Linux-x86_64.sh && \
    chmod +x cmake-3.21.2-Linux-x86_64.sh && \
    ./cmake-3.21.2-Linux-x86_64.sh --skip-license --prefix=/usr/local

# Copy your video.py from the host to the Docker image
COPY video.py /app/video.py

# Set the working directory
WORKDIR /app

ENV IP_ADDRESS="192.168.0.41"

# Start the Python3 file
CMD ["python3", "video.py"]
