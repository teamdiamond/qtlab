import logging

### control of LT1; comment this if adwin is operated from lt1-computer
### set lt1_control to False if LT1 is supposed to work independently
lt1_control=False

#remote instrument connection 
def _do_remote_connect_lt1():
    global powermeter_lt1, SMB100_lt1, PMServo_lt1, ZPLServo_lt1
    if objsh.start_glibtcp_client('192.168.0.20',port=12002, nretry=3, timeout=5):
        remote_ins_server=objsh.helper.find_object('qtlab_lt1:instrument_server')
        powermeter_lt1 = qt.instruments.create('powermeter_lt1', 'Remote_Instrument',
                     remote_name='powermeter', inssrv=remote_ins_server)
        SMB100_lt1 = qt.instruments.create('SMB100_lt1', 'Remote_Instrument',
                     remote_name='SMB100', inssrv=remote_ins_server)
        PMServo_lt1= qt.instruments.create('PMServo_lt1', 'Remote_Instrument',
                     remote_name='PMServo', inssrv=remote_ins_server)
        ZPLServo_lt1= qt.instruments.create('ZPLServo_lt1', 'Remote_Instrument',
                     remote_name='ZPLServo', inssrv=remote_ins_server)
        return True

    logging.warning('Failed to start remote instruments')       
    return False

def _do_remote_connect_monitor():
    global pidnewfocus, pidnewfocus_lt1, pidmatisse
    if objsh.start_glibtcp_client('localhost',port=12003, nretry=3, timeout=5):
        remote_ins_server=objsh.helper.find_object('qtlab_monitor_lt2:instrument_server')
        pidnewfocus = qt.instruments.create('pidnewfocus', 'Remote_Instrument',
                     remote_name='pidnewfocus', inssrv=remote_ins_server)
        pidmatisse= qt.instruments.create('pidmatisse', 'Remote_Instrument',
                     remote_name='pidmatisse', inssrv=remote_ins_server)
        if lt1_control:
            pidnewfocus_lt1 = qt.instruments.create('pidnewfocus_lt1', 'Remote_Instrument',
                     remote_name='pidnewfocus_lt1', inssrv=remote_ins_server)
        return True

    logging.warning('Failed to start remote instruments from monitor')       
    return False

#Hardware
lt1_remote=False

# if not lt1_remote:

physical_adwin = qt.instruments.create('physical_adwin','ADwin_Gold_II',
        address=336)

wavemeter = qt.instruments.create('wavemeter','WS600_WaveMeter')

if objsh.start_glibtcp_client('localhost',port=12003, nretry=3):
    remote_ins_server=objsh.helper.find_object('qtlab_monitor_lt1:instrument_server')
    labjack = qt.instruments.create('labjack', 'Remote_Instrument',
            remote_name='labjack', inssrv=remote_ins_server)
    pidvelocity1 = qt.instruments.create('pidvelocity1', 'Remote_Instrument',
            remote_name='pidvelocity1', inssrv=remote_ins_server)
    pidvelocity2 = qt.instruments.create('pidvelocity2', 'Remote_Instrument',
            remote_name='pidvelocity2', inssrv=remote_ins_server)
    pidyellow = qt.instruments.create('pidyellow', 'Remote_Instrument',
            remote_name='pidyellow', inssrv=remote_ins_server)


AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014', 
        address='GPIB::1::INSTR',reset=False,numpoints=1e3)
SMB100 = qt.instruments.create('SMB100', 'RS_SMB100', 
        address='GPIB::28::INSTR', reset=False)

PH_300 = qt.instruments.create('PH_300', 'PicoHarp_PH300')

powermeter = qt.instruments.create('powermeter','Thorlabs_PM100', address = 'ASRL11::INSTR')
# MillenniaLaser = qt.instruments.create('MillenniaLaser', 'Millennia_Pro', 
#         address='COM1')
TemperatureController = qt.instruments.create('TemperatureController', 
     'Lakeshore_340', address = 'GPIB::12::INSTR')

Velocity1 = qt.instruments.create('Velocity1', 'NewfocusVelocity', 
        address='GPIB::8::INSTR')

#Velocity2 = qt.instruments.create('Velocity2', 'NewfocusVelocity',
#
        

# AttoPositioner = qt.instruments.create('AttoPositioner', 'Attocube_ANC350')

servo_ctrl=qt.instruments.create('ServoController', 'ParallaxServoController', address=7)
ZPLServo=qt.instruments.create('ZPLServo','ServoMotor',servo_controller='ServoController')
PMServo=qt.instruments.create('PMServo','ServoMotor',servo_controller='ServoController')

<<<<<<< HEAD
# simple laser scan
laser_scan = qt.instruments.create('laser_scan', 'laser_scan')

# pid instuments for laser frequeqncy saving 
_do_remote_connect_monitor()



if lt1_control:

    physical_adwin_lt1 = qt.instruments.create('physical_adwin_lt1','ADwin_Gold_II',
                     address=353)
    adwin_lt1 = qt.instruments.create('adwin_lt1', 'adwin_lt1')
    counters_lt1 = qt.instruments.create('counters_lt1', 'counters_via_adwin',
            adwin='adwin_lt1')
    master_of_space_lt1 = qt.instruments.create('master_of_space_lt1', 
            'master_of_space_lt1', adwin='adwin_lt1')
    linescan_counts_lt1 = qt.instruments.create('linescan_counts_lt1', 
            'linescan_counts', adwin='adwin_lt1', mos='master_of_space_lt1',
            counters='counters_lt1')
    scan2d_lt1 = qt.instruments.create('scan2d_lt1', 'scan2d_counts',
            linescan='linescan_counts_lt1', mos='master_of_space_lt1',
            xdim='x', ydim='y', counters='counters_lt1')
    opt1d_counts_lt1 = qt.instruments.create('opt1d_counts_lt1', 
            'optimize1d_counts', linescan='linescan_counts_lt1', 
            mos='master_of_space_lt1', counters='counters_lt1')
    optimiz0r_lt1 = qt.instruments.create('optimiz0r_lt1', 'optimiz0r',opt1d_ins=
            opt1d_counts_lt1, mos_ins = master_of_space_lt1, dimension_set='lt1')
    
    remote_ins_connect=_do_remote_connect_lt1
    if remote_ins_connect():        
        powermeter_lt1_nm = 'powermeter_lt1'
    else:
        logging.warning('LT1 AOMs USE INCORRECT POWER METER!!!1111')
        powermeter_lt1_nm = 'powermeter'
    
    
    GreenAOM_lt1 = qt.instruments.create('GreenAOM_lt1', 'AOM', 
            use_adwin='adwin_lt1', use_pm = powermeter_lt1_nm)         
    NewfocusAOM_lt1 = qt.instruments.create('NewfocusAOM_lt1', 'AOM', 
            use_adwin='adwin_lt1', use_pm = powermeter_lt1_nm)         
    MatisseAOM_lt1 = qt.instruments.create('MatisseAOM_lt1', 'AOM', 
            use_adwin='adwin_lt1', use_pm = powermeter_lt1_nm)   
    laser_scan_lt1 = qt.instruments.create('laser_scan_lt1', 'laser_scan_lt1')
=======
if not lt1_remote:
     
    adwin = qt.instruments.create('adwin', 'adwin_lt1', 
            physical_adwin='physical_adwin')
    
    counters = qt.instruments.create('counters', 'counters_via_adwin',
            adwin='adwin')
>>>>>>> lt1
    
    master_of_space = qt.instruments.create('master_of_space', 
            'master_of_space_lt1', adwin='adwin')

    linescan_counts = qt.instruments.create('linescan_counts', 
            'linescan_counts',  adwin='adwin', mos='master_of_space',
            counters='counters')
    
    scan2d = qt.instruments.create('scan2d', 'scan2d_counts',
             linescan='linescan_counts', mos='master_of_space',
            xdim='x', ydim='y', counters='counters')
     
    opt1d_counts = qt.instruments.create('opt1d_counts', 
             'optimize1d_counts', linescan='linescan_counts', 
            mos='master_of_space', counters='counters')

    optimiz0r = qt.instruments.create('optimiz0r', 'optimiz0r',opt1d_ins=
            opt1d_counts,mos_ins=master_of_space,dimension_set='lt1')
  
    GreenAOM = qt.instruments.create('GreenAOM', 'AOM', 
            use_adwin='adwin', use_pm= 'powermeter')
    Velocity1AOM = qt.instruments.create('Velocity1AOM', 'AOM', 
            use_adwin='adwin', use_pm = 'powermeter')         
    Velocity2AOM = qt.instruments.create('Velocity2AOM', 'AOM', 
            use_adwin='adwin', use_pm = 'powermeter')
    YellowAOM = qt.instruments.create('YellowAOM', 'AOM', 
            use_adwin='adwin', use_pm ='powermeter')
    #laser_scan = qt.instruments.create('laser_scan', 'laser_scan')
     
    setup_controller = qt.instruments.create('setup_controller',
             'setup_controller',
            use = { 'master_of_space' : 'mos'} )



