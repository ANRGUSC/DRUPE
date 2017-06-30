1. Modify input in folder central_input (nodes.txt, link_list.txt) of central_network_profiler and upload_docker_network accordingly (IP, PASSWORD, REG, link_list)

2. Run: ./upload_docker_network to upload codes to all the nodes

3. Build the dockers: Scheduler IP0, and other droplets IP1, IP2, IP3

- Scheduler(IP0): docker build -t central_network_profiler .
- Droplets(IP1, IP2, IP3): docker build -t droplet_network_profiler .

4. Run the dockers: Scheduler IP0, and other droplets IP1, IP2, IP3

Step 1: Inside the droplet_network_profiler:
docker run --rm --name droplet_network_profiler -t -i -e DOCKER_HOST=IP1 -p 5100:22 -P droplet_network_profiler
docker run --rm --name droplet_network_profiler -t -i -e DOCKER_HOST=IP2 -p 5100:22 -P droplet_network_profiler
docker run --rm --name droplet_network_profiler -t -i -e DOCKER_HOST=IP3 -p 5100:22 -P droplet_network_profiler

Step 2: Inside the central_network_profiler:
docker run --rm --name  central_network_profiler -i -t -e DOCKER_HOST=IP0 -p 5100:22 -P central_network_profiler


