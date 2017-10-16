# centralized_scheduler
Centralized scheduler implementation using Docker containers and Kubernetes (K8s).

Instructions:

The instructions here begin at the point in which you have a target 
configuration.txt and nodes.txt file. First, you need to build your Docker 
images. There are currently two separate images: the "home_node" image and 
"worker_node" image.

To rebuild Docker images and push them to the ANRG Docker Hub repo, first login 
to Docker Hub using your own credentials by running `docker login`. Then, in the
folder with the *.Dockerfile files, use this template to build all the needed
Docker images:

    docker build -f $target_dockerfile . -t $dockerhub_user/$repo_name:$tag
    docker push $dockerhub_user/$repo_name:$tag

Example (you can turn this into a bash script):

    docker build -f worker_node.Dockerfile . -t anrg/worker_node:v1
    docker push anrg/worker_node:v1
    docker build -f home_node.Dockerfile . -t anrg/home_node:v1
    docker push anrg/home_node:v1

Note: If you just want to control the whole cluster via our master node (i.e. you don't
want to use your computer) go to [this section](#controlling-cluster-from-k8s-master-node) 
in the readme).

To control the cluster, you need to grab the `admin.conf` file from the k8s 
master node. When the cluster is bootstrapped by `kubeadm` [see the k8s cluster
setup notes here](https://drive.google.com/open?id=1NeewrSx9Bp3oNOGGpgyfKBjul1NbSB8kHqy7gslxtKk)
the `admin.conf` file is stored in `/etc/kubernetes/admin.conf`. Usually, a copy
is made into the $HOME folder. Either way, make a copy of `admin.conf` into your 
local machine's home folder. Then, make sure you have `kubectl` installed ([instrcutions 
here](https://kubernetes.io/docs/tasks/tools/install-kubectl/)). Next, you need 
to run the commands below. You can wrap it up in a script you source or directly 
place the export line and source line into your .bashrc file. However, make sure 
to re-run the full set of commands if the `admin.conf` file has changed:

    sudo chown $(id -u):$(id -g) $HOME/admin.conf
    export KUBECONFIG=$HOME/admin.conf #check if it works with `kubectl get nodes`
    source <(kubectl completion bash)

Clone/pull this repo and `cd` into the repo's directory. Currently, you need to have
`admin.conf` in the folder above your clone. Our python scripts need it exactly
there to work. Then, run:

    python3 k8s_scheduler.py

Lastly, you will want to access the k8s Web UI on your local machine. Assuming 
you have `kubectl` installed and `admin.conf` imported, simply open a separate 
terminal on your local machine and run:

    kubectl proxy

The output should be something like:

    Starting to serve on 127.0.0.1:8001

Open up a browser on your local machine and go to 
`http://127.0.0.1:8001/ui`. You should see the k8s dashboard. Hit `Ctrl+c` on
the terminal running the server to turn off the proxy. Alternatively, you can
run this command directly in the folder where the `admin.conf` file is (not 
recommended):

    kubectl --kubeconfig=./admin.conf proxy - p 80

The last step is to push a file into the input folder at the home node. To shell
into the home node, run this (using the actual home pod name of course):

    kubectl exec -it home-1720468393-ln2jx /bin/sh
    cd input
    echo "1 2 3 4" > test.txt

## Teardown

To teardown the DAG deployment, run the following:
    
    python3 delete_all_deployment.py

Once the deployment is torn down, you can simply start from the begining of 
these instructions to make changes to your code and redeploy the DAG. FYI, 
k8s_scheduler.py defaults to ALWAYS pulling the Docker image (even if it hasn't 
changed).

## Controlling Cluster from K8s Master Node

Login to the Kubernetes Master node (currently Jason's computer under the user 
"apac"). Assuming the cluster is up (it typically will not be shutdown), source
the sourceit.sh script in the "apac" user's home folder so you can use`kubectl` 
to  control the cluster:
    
    source sourceit.sh

Note that you do NOT need to do this if the `admin.conf` file hasn't changed 
given the following lines are placed in the master node's .bashrc file:

    export KUBECONFIG=$HOME/admin.conf
    source <(kubectl completion bash)

The `admin.conf` file changes whenever the cluster is re-bootstrapped. You can 
then run the following command to check if everything is working. If it lists 
all the nodes in the cluster, you're ready to start controlling it:

    kubectl get nodes #if this works you're ready to start controlling
