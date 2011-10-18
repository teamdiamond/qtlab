# This file contains user-specific settings for qtlab.
# It is run as a regular python script.

# Do not change the following line unless you know what you are doing
config.remove([
            'datadir',
            'startdir',
            'startscript',
            'user_ins_dir',
            ])

import sys, os
BASE = os.path.join(os.getcwd(), '..')


## This sets a default location for data-storage
config['datadir'] = BASE+'data'

## This sets a default directory for qtlab to start in
#config['startdir'] = 'd:/scripts'

## This sets a default script to run after qtlab started
#config['startscript'] = 'initscript.py'

# Add directories containing scripts here. All scripts will be added to the
# global namespace as functions.
config['scriptdirs'] = [
        'examples/scripts',
        BASE+'user/scripts'
#        'd:/scripts',
]

## This sets a user instrument directory
## Any instrument drivers placed here will take
## preference over the general instrument drivers
config['user_insdir'] = BASE+'user/instruments'

## For adding additional folders to the 'systm path'
## so python can find your modules
import sys, os
sys.path.append(BASE+'/user/modules')

# cyclops configuration
cyclops_dir = BASE+'cyclops'
config['cyclops_dir'] = cyclops_dir
sys.path.append(cyclops_dir)
sys.path.append(os.path.join(cyclops_dir, 'source'))
