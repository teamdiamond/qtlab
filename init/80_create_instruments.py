# Some demo stuff in here, to get the idea

#Hardware

# if not lt1_remote:
physical_adwin = qt.instruments.create('physical_adwin','ADwin_Pro_II',
        address=339)

#SMB100 = qt.instruments.create('SMB100', 'RS_SMB100', 
#        address='GPIB::28::INSTR', reset=False)


labjack = qt.instruments.create('labjack', 'LabJack_U3')

wavemeter = qt.instruments.create('wavemeter','WS600_WaveMeter')
wavemeter.set_active_channel(3)

adwin = qt.instruments.create('adwin', 'adwin_lt3', 
        physical_adwin='physical_adwin')

rotator = qt.instruments.create('rotator', 'NewportAgilisUC', 
        address = 'COM6', ins_type='UC8')
rejecter = qt.instruments.create('rejecter', 'laser_reject0r_v2', rotator='rotator',
        adwin='adwin', rotation_config_name='waveplates_lt3')

ivvi = qt.instruments.create('ivvi', 'IVVI', address = 'ASRL1::INSTR', numdacs= 4)

lt3_measurement_helper = qt.instruments.create('lt3_measurement_helper', 'remote_measurement_helper', exec_qtlab_name = 'qtlab_lt3')

wm_channel_nf = 1
_setfrq_nf = lambda x: labjack.set_bipolar_dac3(x)
_getfrq_nf = lambda: labjack.get_bipolar_dac3()
_setfrq_coarse_nf = lambda x: labjack.set_bipolar_dac2(x)
_getfrq_coarse_nf = lambda: labjack.get_bipolar_dac2()
_getval_nf = lambda: wavemeter.Get_Frequency(wm_channel_nf)
print _getval_nf()
pidnewfocus = qt.instruments.create('pidnewfocus', 'pid_controller_v4', \
        set_ctrl_func=_setfrq_nf, get_ctrl_func=_getfrq_nf, \
        set_ctrl_func_coarse=_setfrq_coarse_nf, get_ctrl_func_coarse=_getfrq_coarse_nf, \
        get_val_func=_getval_nf)

wm_channel_ye = 2
_setfrq_ye = lambda x: labjack.set_bipolar_dac5(x)
_getfrq_ye = lambda: labjack.get_bipolar_dac5()
_setfrq_coarse_ye = lambda x: labjack.set_bipolar_dac4(x)
_getfrq_coarse_ye = lambda: labjack.get_bipolar_dac4()
_getval_ye = lambda: wavemeter.Get_Frequency(wm_channel_ye)
pidyellow = qt.instruments.create('pidyellow', 'pid_controller_v4', \
        set_ctrl_func=_setfrq_ye, get_ctrl_func=_getfrq_ye, \
        set_ctrl_func_coarse=_setfrq_coarse_ye, get_ctrl_func_coarse=_getfrq_coarse_ye, \
        get_val_func=_getval_ye)

wm_channel_ta = 4
_setfrq_ta = lambda x: labjack.set_bipolar_dac1(x)
_getfrq_ta = lambda: labjack.get_bipolar_dac1()
_setfrq_coarse_ta = lambda x: labjack.set_bipolar_dac0(x)
_getfrq_coarse_ta = lambda: labjack.get_bipolar_dac0()
_getval_ta = lambda: physical_adwin.Get_FPar(40+wm_channel_ta)
pidtaper = qt.instruments.create('pidtaper', 'pid_controller_v4', \
        set_ctrl_func=_setfrq_ta, get_ctrl_func=_getfrq_ta, \
        set_ctrl_func_coarse=_setfrq_coarse_ta, get_ctrl_func_coarse=_getfrq_coarse_ta, \
        get_val_func=_getval_ta)

physical_adwin.Set_FPar(51,pidnewfocus.get_setpoint())
physical_adwin.Set_FPar(52,pidyellow.get_setpoint())
physical_adwin.Set_FPar(53,pidtaper.get_setpoint())
   
# set up broadcasting
broadcast0r = qt.instruments.create('broadcast0r', 'broadcast0r')
broadcast0r.add_broadcast('wm_ch1', lambda: wavemeter.Get_Frequency(1), lambda x: physical_adwin.Set_FPar(41, (x-470.40)*1e3 ))
broadcast0r.add_broadcast('wm_ch2', lambda: wavemeter.Get_Frequency(2), lambda x: physical_adwin.Set_FPar(42, (x-521.22)*1e3 ))
broadcast0r.add_broadcast('pid_newfocus_setpoint', lambda: physical_adwin.Get_FPar(51), lambda x: pidnewfocus.set_setpoint(x), lambda x: x > -100.)
broadcast0r.add_broadcast('pidyellow_setpoint',    lambda: physical_adwin.Get_FPar(52), lambda x: pidyellow.set_setpoint(x), lambda x: x != 0.)
broadcast0r.add_broadcast('pidtaper_setpoint',     lambda: physical_adwin.Get_FPar(53), lambda x: pidtaper.set_setpoint(x), lambda x: x > -100.)
broadcast0r.start()