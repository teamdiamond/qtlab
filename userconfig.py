# This file contains user-specific settings for qtlab.
# It is run as a regular python script.

# Do not change the following line unless you know what you are doing
config.remove([
            'datadir',
            'startdir',
            'startscript',
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

## This sets a default location for data-storage
#config['datadir'] = 'd:/data'

## This sets a default directory for qtlab to start in
#config['startdir'] = 'd:/scripts'

## This sets a default script to run after qtlab started
#config['startscript'] = 'initscript.py'
import sys, os
BASE = os.path.join(os.getcwd(), '..')

## This sets a default location for data-storage
config['datadir'] = os.path.join(BASE,'data')
# Add directories containing scripts here. All scripts will be added to the
# global namespace as functions.

config['scriptdirs'] = [
        'examples/scripts',
        os.path.join(BASE,'measurement/scripts'),
        os.path.join(BASE,'measurement/scripts/lt1_scripts')
#        'd:/scripts',
]
## This sets a user instrument directory
## Any instrument drivers placed here will take
## preference over the general instrument drivers
config['user_insdir'] = os.path.join(BASE,'measurement/instruments')

## For adding additional folders to the 'systm path'
## so python can find your modules

sys.path.append(r'D:\measuring')

# FIXME: this is a dirty fix to ensure qtlab/source is the first in sys.path
sys.path.insert(0,'D:\measuring\qtlab\source')

# cyclops configuration
cyclops_dir = os.path.join(BASE,'cyclops')
config['cyclops_dir'] = cyclops_dir
sys.path.append(cyclops_dir)
sys.path.append(os.path.join(cyclops_dir, 'source'))

config['setup_cfg'] = os.path.join(os.getcwd(), 'setup.cfg')
config['pq_dll'] = 'd:/measuring/measurement/bin/pq_tttr.dll'
config['anc350_dll'] = os.path.join(BASE, 'bin', 'attocube_ANC350',
        'hvpositionerv2.dll')
config['adwin_programs'] = 'd:/measuring/measurement/ADwin_Codes/'
config['adwin_lt1_subfolder'] = 'adwin_gold_2_lt1'
config['adwin_lt2_subfolder'] = 'adwin_pro_2_lt2'

# config files
config['ins_cfg_path'] = "../measurement/config/"
config['samples_cfg'] = os.path.join(os.getcwd(), '../measurement/config/samples.cfg')
config['protocols_cfg'] = os.path.join(os.getcwd(), '../measurement/config/protocols.cfg')
config['awg_cfg'] = os.path.join(os.getcwd(), '../measurement/config/awgchannels.cfg')

## This sets a user instrument directory
## Any instrument drivers placed here will take
## preference over the general instrument drivers
#config['user_insdir'] = 'd:/instruments'

## For adding additional folders to the 'systm path'
## so python can find your modules
#import sys
#sys.path.append('d:/folder1')
#sys.path.append('d:/folder2')

# Whether to start the GUI automatically
config['startgui'] = False

# Default gnuplot terminal
#config['gnuplot_terminal'] = 'x11'
#config['gnuplot_terminal'] = 'wxt'
#config['gnuplot_terminal'] = 'windows'
