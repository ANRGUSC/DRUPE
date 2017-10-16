# Top level config file (leave this file at the root directory). `import config`
# on the top of your file to include the global information included here.

from os import path
import os


here = path.abspath(path.dirname(__file__))

KUBECONFIG_PATH         = os.environ['KUBECONFIG']
DEPLOYMENT_NAMESPACE    = 'pradipta'
PROFILER_NAMESPACE      = 'pradipta'

#home's child node is hardcoded in write_home_specs.py
HOME_NODE               = 'ubuntu-2gb-nyc2-01' 
HOME_IMAGE              = 'docker.io/anrg/home_node:pg1' 
HOME_CHILD              = 'task1'

WORKER_IMAGE            = 'docker.io/anrg/worker_node:pg'

PROFILER_HOME_IMAGE     = 'anrg/central_profiler:v2' 
PROFILER_WORKER_IMAGE   = 'anrg/worker_profiler:v6' 