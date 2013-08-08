import logging
sys.path.append('D:\\measuring\\measurement')


#remote instrument connection 
def _do_remote_connect():
    global TemperatureController_lt1, AttoPositioner_lt1
    if objsh.start_glibtcp_client('192.168.0.20',port=12002, nretry=3, timeout=5):
        remote_ins_server=objsh.helper.find_object('qtlab_lt1:instrument_server')
        TemperatureController_lt1=qt.instruments.create('TemperatureController_lt1', 'Remote_Instrument',
                     remote_name='TemperatureController', inssrv=remote_ins_server)
        AttoPositioner_lt1=qt.instruments.create('AttoPositioner_lt1', 'Remote_Instrument',
                     remote_name='AttoPositioner', inssrv=remote_ins_server)

        return True

    logging.warning('Failed to start remote instruments')       
    return False

def remote_connect_pids():
    global pidyellow,pidmatisse,pidnewfocus
    if objsh.start_glibtcp_client('192.168.0.80',port=12002, nretry=3, timeout=5):
        remote_ins_server_lasers=objsh.helper.find_object('qtlab_lasermeister:instrument_server')
        pidyellow = qt.instruments.create('pidyellow', 'Remote_Instrument',
                     remote_name='pidyellow', inssrv=remote_ins_server_lasers)    
        pidmatisse = qt.instruments.create('pidmatisse', 'Remote_Instrument',
                     remote_name='pidmatisse', inssrv=remote_ins_server_lasers)
        pidnewfocus = qt.instruments.create('pidnewfocus', 'Remote_Instrument',
                     remote_name='pid_lt2_newfocus', inssrv=remote_ins_server_lasers)                       

# adwin
physical_adwin = qt.instruments.create('physical_adwin','ADwin_Pro_II'
                 ,address=352)
adwin = qt.instruments.create('adwin', 'adwin_lt2', init=False, use_cfg=False)



#labjack
# NOTE not connected right now
#labjack = qt.instruments.create('labjack', 'LabJack_U3')

# laser & wavemeter
# NewfocusLaser = qt.instruments.create('NewfocusLaser', 'NewfocusVelocity', 
#        address = 'GPIB::10::INSTR' )

#pids
remote_connect_pids()        
        
tuner=qt.instruments.create('tuner','lt2_ssro_optimizer')                
 
#remote pid yellow:      

lt1_control=False

if lt1_control:
    physical_adwin_lt1 = qt.instruments.create('physical_adwin_lt1','ADwin_Gold_II',
                     address=353)
    adwin_lt1 = qt.instruments.create('adwin_lt1', 'adwin_lt1', init=False, 
            use_cfg=False) 
    # PID for LT1 laser stabilization
    wm_channel_lt1=3
    _setfrq_lt1 = lambda x: adwin_lt1.set_dac_voltage(('newfocus_frq', x))
    _getfrq_lt1=lambda: wavemeter.Get_Frequency(wm_channel_lt1)

    pidnewfocus_lt1 = qt.instruments.create('pidnewfocus_lt1', 'pid_controller', 
        set_ctrl_func=_setfrq_lt1, get_val_func=_getfrq_lt1, get_stabilizor_func=get_frq_hene)
    remote_ins_connect=_do_remote_connect
    # _monitor_lt1 = remote_ins_connect()


# monitoring
keithleyMM = qt.instruments.create('keithleyMM', 'Keithley_2000', address='GPIB::11::INSTR')

gmailer = qt.instruments.create('gmailer','send_email',username='cryolt2',password='Diamond=Geil!')
monitor_cryo = qt.instruments.create('monitor_cryo','monitor_cryo', monitor_lt1=False)
monitor_cryo.start()

adwin_lt2_monit0r = qt.instruments.create('adwin_lt2_monit0r', 
    'adwin_monit0r', physical_adwin='physical_adwin')
adwin_lt2_monit0r.add_fpar(41, 'Matisse Frequency')
adwin_lt2_monit0r.add_fpar(43, 'NewFocus Frequency')
adwin_lt2_monit0r.start()

#cmd line tool for GUI
command0r = qt.instruments.create('command0r', 'command0r')

