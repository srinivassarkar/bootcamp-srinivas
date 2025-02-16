Amazon Linux: Install Docker & Run Python

1. Update & Install Docker
   ```bash
   sudo yum update -y && sudo yum install docker -y
   ```
   Updates system & installs Docker.

2. Start & Enable Docker
   ```bash
   sudo systemctl start docker && sudo systemctl enable docker
   ```
   Starts Docker & ensures it runs on reboot.

3. Add User to Docker Group
   ```bash
   sudo usermod -aG docker $USER
   ```
   Allows non-root user to run Docker without sudo.

4. Apply Group Changes
   ```bash
   newgrp docker
   ```
   Applies changes without logging out.

5. Verify Docker Installation
   ```bash
   docker info
   ```
   Confirms Docker is running.

6. Pull Python Image
   ```bash
   docker pull python:latest
   ```
   Downloads latest Python image from Docker Hub.

7. Run Python in Docker
   ```bash
   docker run --rm python:latest python -c 'print("Hello, World!")'
   ```
   Runs Python inside a container and prints output.



Hosting Python via HTTP Server on Amazon Linux

1. Install Python (If Not Installed)
   ```bash
   sudo yum install python3 -y
   ```
   Ensures Python is installed.

2. Start HTTP Server
   ```bash
   python3 -m http.server 8080 --bind 0.0.0.0
   ```
   Hosts files in the current directory on port 8080.

3. Open Firewall Port (If Required)
   ```bash
   sudo firewall-cmd --add-port=8080/tcp --permanent && sudo firewall-cmd --reload
   ```
   Allows external access to port 8080.

4. Access Server
   Open in browser:
   ```
   http://<EC2-PUBLIC-IP>:8080/
   ```
   Serves directory listing via browser.



Setting Up Custom Domain with DuckDNS

1. Register on DuckDNS & Get a Subdomain
   - Go to [DuckDNS](https://www.duckdns.org/) and create a subdomain.

2. Update DuckDNS with Public IP
   ```bash
   echo url="https://www.duckdns.org/update?domains=<YOUR_SUBDOMAIN>&token=<YOUR_TOKEN>&ip=" | curl -k -o ~/duckdns.log -K -
   ```
   Updates DuckDNS with EC2’s public IP.

3. Use Domain to Access Server
   ```
   http://<YOUR_SUBDOMAIN>.duckdns.org:8080/
   ```
   Access hosted files via custom domain.









