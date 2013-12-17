# This file contains user-specific settings for qtlab.
# It is run as a regular python script.
import sys, os
BASE = r'D:\measuring'
sys.path.append(BASE)

# FIXME: this is a dirty fix to ensure qtlab/source is the first in sys.path
sys.path.insert(0,os.path.join(BASE, 'qtlab', 'source'))

# Do not change the following line unless you know what you are doing
config.remove([
            'datadir',
            'startdir',
            'scriptdirs',
            'user_ins_dir',
            'startgui',
            'gnuplot_terminal',
            ])

# QTLab instance name and port for networked operation
config['instance_name'] = 'qtlab_lt1'
config['port'] = 12002

# A list of allowed IP ranges for remote connections
config['allowed_ips'] = ('192.168.0.*', )
#    '130.161.*.*',
#    '145.94.*.*',
     
# Start instrument server to share with instruments with remote QTLab?
config['instrument_server'] = True

## This sets a default directory for qtlab to start in
config['startdir'] = os.path.join(BASE,'measurement/scripts')

## A default script (or list of scripts) to run after qtlab started
config['startscript'] = []      #e.g. 'initscript1.py'

## A default script (or list of scripts) to run when qtlab closes
config['exitscript'] = []       #e.g. ['closescript1.py', 'closescript2.py']

## This sets a default location for data-storage
config['datadir'] = os.path.join(BASE,'data')
# Add directories containing scripts here. All scripts will be added to the
# global namespace as functions.

config['scriptdirs'] = [
        os.path.join(BASE,'measurement/scripts'),
]

## This sets a user instrument directory
## Any instrument drivers placed here will take
## preference over the general instrument drivers
config['user_insdir'] = os.path.join(BASE,'measurement/instruments')

# cyclops configuration
cyclops_dir = os.path.join(BASE,'cyclops')
config['cyclops_dir'] = cyclops_dir
sys.path.append(cyclops_dir)
sys.path.append(os.path.join(cyclops_dir, 'source'))

config['setup_cfg'] = os.path.join(os.getcwd(), 'setup.cfg')
# config['pq_dll'] = 'd:/measuring/measurement/bin/pq_tttr.dll'
config['anc350_dll'] = os.path.join(BASE, 'bin', 'attocube_ANC350',
        'hvpositionerv2.dll')
config['adwin_programs'] = 'd:/measuring/measurement/ADwin_Codes/'
config['adwin_lt1_subfolder'] = 'adwin_gold_2_lt1'
config['adwin_lt2_subfolder'] = 'adwin_pro_2_lt2'

# config files
config['cfg_path'] = os.path.join(BASE, 'measurement', 'config')
config['ins_cfg_path'] = os.path.join(BASE, 'measurement', 'config')
config['samples_cfg'] = os.path.join(BASE, 'measurement', 'config','samples.cfg')
config['protocols_cfg'] = os.path.join(BASE, 'measurement', 'config','protocols.cfg')
config['awg_cfg'] = os.path.join(BASE, 'measurement', 'config','awgchannels.cfg')

# Whether to start the GUI automatically
config['startgui'] = True

# Default gnuplot terminal
#config['gnuplot_terminal'] = 'x11'
config['gnuplot_terminal'] = 'wxt'
#config['gnuplot_terminal'] = 'windows'

# cyclops configuration
cyclops_dir = os.path.join(BASE,'cyclops')
config['cyclops_dir'] = cyclops_dir
sys.path.append(cyclops_dir)
sys.path.append(os.path.join(cyclops_dir, 'source'))

# Enter a filename here to log all IPython commands
config['ipython_logfile'] = ''      #e.g. 'command.log'
