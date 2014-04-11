import logging

### control of LT1; comment this if adwin is operated from lt1-computer
### set lt1_control to False if LT1 is supposed to work independently
lt1_control=False

#remote instrument connection
def _do_remote_connect_lt1():
    global powermeter_lt1, SMB100_lt1, PMServo_lt1, ZPLServo_lt1
    if objsh.start_glibtcp_client('192.168.0.20',port=12002, nretry=3, timeout=5):
        remote_ins_server_lt1=objsh.helper.find_object('qtlab_lt1:instrument_server')
        powermeter_lt1 = qt.instruments.create('powermeter_lt1', 'Remote_Instrument',
                     remote_name='powermeter', inssrv=remote_ins_server_lt1)
        SMB100_lt1 = qt.instruments.create('SMB100_lt1', 'Remote_Instrument',
                     remote_name='SMB100', inssrv=remote_ins_server_lt1)
        PMServo_lt1= qt.instruments.create('PMServo_lt1', 'Remote_Instrument',
                     remote_name='PMServo', inssrv=remote_ins_server_lt1)
        ZPLServo_lt1= qt.instruments.create('ZPLServo_lt1', 'Remote_Instrument',
                     remote_name='ZPLServo', inssrv=remote_ins_server_lt1)
        return True
    logging.warning('Failed to start remote instruments')
    return False

def _do_remote_connect_pids():
    global pidyellow,pidmatisse,pidnewfocus,labjack
    if objsh.start_glibtcp_client('192.168.0.80',port=12002, nretry=3, timeout=5):
        remote_ins_server_lasers=objsh.helper.find_object('qtlab_lasermeister:instrument_server')
        labjack = qt.instruments.create('labjack', 'Remote_Instrument',
            remote_name='labjack', inssrv=remote_ins_server_lasers)
        pidyellow = qt.instruments.create('pidyellow', 'Remote_Instrument',
                     remote_name='pidyellow', inssrv=remote_ins_server_lasers)
        pidmatisse = qt.instruments.create('pidmatisse', 'Remote_Instrument',
                     remote_name='pidmatisse', inssrv=remote_ins_server_lasers)
        pidnewfocus = qt.instruments.create('pidnewfocus', 'Remote_Instrument',
                     remote_name='pid_lt2_newfocus', inssrv=remote_ins_server_lasers)
        return True
    logging.warning('Failed to start remote instruments from lasermeister')
    return False

def _do_remote_connect_monitor():
    global pidnewfocus, pidnewfocus2, pidyellow,labjack,tuner,pidnewfocus_lt1
    if objsh.start_glibtcp_client('localhost',port=12003, nretry=3, timeout=5):
        remote_ins_server=objsh.helper.find_object('qtlab_monitor_lt2:instrument_server')
        tuner=qt.instruments.create('tuner', 'Remote_Instrument',
                     remote_name='tuner', inssrv=remote_ins_server)
        return True
    logging.warning('Failed to start remote instruments from monitor')
    return False

#Hardware
physical_adwin = qt.instruments.create('physical_adwin','ADwin_Pro_II',
                 address=352)

# NewfocusLaser = qt.instruments.create('NewfocusLaser', 'NewfocusVelocity',
#                 address = 'GPIB::10::INSTR' )
AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014_09',
        address='TCPIP0::192.168.0.31::inst0::INSTR',reset=False,numpoints=1e3)
        #GPIB::23::INSTR' $#AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014_09',
#        address='GPIB::23::INSTR',reset=False,numpoints=1e3)
SMB100 = qt.instruments.create('SMB100', 'RS_SMB100',
        address='GPIB::4::INSTR', reset=False, max_cw_pwr=-3)
noIQ_SMB100 = qt.instruments.create('noIQ_SMB100', 'RS_SMB100_noIQ',
        address='GPIB::13::INSTR', reset=False, max_pwr=-3, max_cw_pwr=-3)


# physical_adwin.Boot()

# some real instruments
# wavemeter = qt.instruments.create('wavemeter','WSU_WaveMeter')
powermeter = qt.instruments.create('powermeter', 'Thorlabs_PM100D',
        address='USB0::0x1313::0x8070::P0000478::INSTR')


#Adwin instruments
adwin_lt2 = qt.instruments.create('adwin', 'adwin_lt2')
adwin = adwin_lt2

counters = qt.instruments.create('counters', 'counters_via_adwin',
        adwin='adwin')
counters.set_is_running(True)


## more Hardware, that also needs the adwin
#HH_400 = qt.instruments.create('HH_400','HydraHarp_HH400') went to LT3 20140307 Julia&Bas

# AOMs
NewfocusAOM  = qt.instruments.create('NewfocusAOM', 'AOM')
GreenAOM  = qt.instruments.create('GreenAOM', 'AOM')
MatisseAOM  = qt.instruments.create('MatisseAOM', 'AOM')
YellowAOM  = qt.instruments.create('YellowAOM', 'AOM')

# Position instruments
master_of_space = qt.instruments.create('master_of_space', 'master_of_space',
        adwin='adwin', dimension_set='mos_lt2')
linescan_counts = qt.instruments.create('linescan_counts', 'linescan_counts',
        adwin='adwin', mos='master_of_space')
scan2d_stage = qt.instruments.create('scan2d_stage', 'scan2d_counts',
        linescan='linescan_counts', mos='master_of_space',
        xdim='x', ydim='y', counters='counters')
opt1d_counts = qt.instruments.create('opt1d_counts', 'optimize1d_counts',
        linescan='linescan_counts', mos='master_of_space', counters='counters')
optimiz0r = qt.instruments.create('optimiz0r', 'optimiz0r')
c_optimiz0r = qt.instruments.create('c_optimiz0r', 'convex_optimiz0r',
        adwin_ins=adwin, mos_ins=master_of_space)

ANC300_LT2 = qt.instruments.create('ANC300_LT2', 'Attocube_ANC300',
        address = 'COM3')
master_of_magnet = qt.instruments.create('master_of_magnet', 'Master_of_magnet')

#Servo instruments
servo_ctrl=qt.instruments.create('ServoController', 'ParallaxServoController', address=3)
PMServo=qt.instruments.create('PMServo','ServoMotor',servo_controller='ServoController')
ZPLServo=qt.instruments.create('ZPLServo','ServoMotor',servo_controller='ServoController')

#qutau = qt.instruments.create('QuTau', 'QuTau')
# pid instuments for laser frequeqncy saving
_do_remote_connect_pids()

#tuner instrument from monitor
#_do_remote_connect_monitor()

if lt1_control:

    physical_adwin_lt1 = qt.instruments.create('physical_adwin_lt1','ADwin_Gold_II',
                     address=353)
    adwin_lt1 = qt.instruments.create('adwin_lt1', 'adwin_lt1')
    counters_lt1 = qt.instruments.create('counters_lt1', 'counters_via_adwin',
            adwin='adwin_lt1')
    master_of_space_lt1 = qt.instruments.create('master_of_space_lt1',
            'master_of_space', adwin='adwin_lt1', dimension_set='mos_lt1')
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
        powermeter_lt1 = qt.instruments['powermeter_lt1']
    else:
        logging.warning('LT1 AOMs USE INCORRECT POWER METER!!!1234')
        powermeter_lt1 = qt.instruments['powermeter_lt1']


    GreenAOM_lt1 = qt.instruments.create('GreenAOM_lt1', 'AOM',
            use_adwin='adwin_lt1', use_pm = powermeter_lt1.get_name())
    NewfocusAOM_lt1 = qt.instruments.create('NewfocusAOM_lt1', 'AOM',
            use_adwin='adwin_lt1', use_pm = powermeter_lt1.get_name())
    MatisseAOM_lt1 = qt.instruments.create('MatisseAOM_lt1', 'AOM',
            use_adwin='adwin_lt1', use_pm = powermeter_lt1.get_name())
    YellowAOM_lt1 = qt.instruments.create('YellowAOM_lt1', 'AOM',
            use_adwin = 'adwin_lt1', use_pm = powermeter_lt1.get_name())

    setup_controller_lt1 = qt.instruments.create('setup_controller_lt1',
        'setup_controller',
        use = { 'master_of_space_lt1' : 'mos'} )


###
### end of lt1-control


### Pannel instruments
setup_controller = qt.instruments.create('setup_controller',
    'setup_controller',
    use = { 'master_of_space' : 'mos'} )

