physical_adwin = qt.instruments.create('physical_adwin','ADwin_Pro_II',
        address=336)
#physical_adwin_lt2 = qt.instruments.create('physical_adwin_lt2','ADwin_Pro_II',
#        address=340)

#SMB100 = qt.instruments.create('SMB100', 'RS_SMB100', 
#        address='GPIB::28::INSTR', reset=False)


labjack = qt.instruments.create('labjack', 'LabJack_U3')

wavemeter = qt.instruments.create('wavemeter','WS600_WaveMeter')
wavemeter.set_active_channel(3)

adwin = qt.instruments.create('adwin', 'adwin_lt4', 
        physical_adwin='physical_adwin')# Some demo stuff in here, to get the idea


wm_channel_nf = 1
_setfrq_nf = lambda x: labjack.set_bipolar_dac1(x)
_getfrq_nf = lambda: labjack.get_bipolar_dac1()
_setfrq_coarse_nf = lambda x: labjack.set_bipolar_dac0(x)
_getfrq_coarse_nf = lambda: labjack.get_bipolar_dac0()
_getval_nf = lambda: wavemeter.Get_Frequency(wm_channel_nf)
print _getval_nf()
pidnewfocus = qt.instruments.create('pidnewfocus', 'pid_controller_v4', \
        set_ctrl_func=_setfrq_nf, get_ctrl_func=_getfrq_nf, \
        set_ctrl_func_coarse=_setfrq_coarse_nf, get_ctrl_func_coarse=_getfrq_coarse_nf, \
        get_val_func=_getval_nf,ctrl_minval_coarse=-4., ctrl_maxval_coarse=4.)