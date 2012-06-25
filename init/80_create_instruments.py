sys.path.append('D:\\measuring\\user\\modules')



#Hardware
physical_adwin = qt.instruments.create('physical_adwin','ADwin_Pro_II',
                 address=352)

NewfocusLaser = qt.instruments.create('NewfocusLaser', 'NewfocusVelocity',
                address = 'GPIB::10::INSTR' )
AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014_09',
                address='GPIB::23::INSTR',reset=False,numpoints=1e3)
SMB100 = qt.instruments.create('SMB100', 'RS_SMB100', 
        address='GPIB::4::INSTR', reset=False)

# physical_adwin.Boot()

# some real instruments
wavemeter = qt.instruments.create('wavemeter','WS600_WaveMeter')
powermeter = qt.instruments.create('powermeter', 'Thorlabs_PM100D',
        address='USB0::0x1313::0x8078::P0003753::INSTR')

#Adwin instruments
adwin_lt2 = qt.instruments.create('adwin', 'adwin_lt2')
adwin = adwin_lt2

counters = qt.instruments.create('counters', 'counters_via_adwin',
        adwin='adwin')
counters.set_is_running(True)


## more Hardware, that also needs the adwin
HH_400 = qt.instruments.create('HH_400','HydraHarp_HH400')


# AOMs
NewfocusAOM  = qt.instruments.create('NewfocusAOM', 'AOM')
GreenAOM  = qt.instruments.create('GreenAOM', 'AOM')
MatisseAOM  = qt.instruments.create('MatisseAOM', 'AOM')


# Position instruments
master_of_space = qt.instruments.create('master_of_space', 'master_of_space',
        adwin='adwin') 
linescan_counts = qt.instruments.create('linescan_counts', 'linescan_counts',
        adwin='adwin', mos='master_of_space')
scan2d_stage = qt.instruments.create('scan2d_stage', 'scan2d_counts',
        linescan='linescan_counts', mos='master_of_space',
        xdim='x', ydim='y', counters='counters')
opt1d_counts = qt.instruments.create('opt1d_counts', 'optimize1d_counts',
        linescan='linescan_counts', mos='master_of_space', counters='counters')
optimiz0r = qt.instruments.create('optimiz0r', 'optimiz0r')

#Servo instruments
servo_ctrl=qt.instruments.create('ServoController', 'ParallaxServoController', address=3)
PMServo=qt.instruments.create('PMServo','ServoMotor',servo_controller='ServoController')
ZPLServo=qt.instruments.create('ZPLServo','ServoMotor',servo_controller='ServoController')

# simple laser scan
laser_scan = qt.instruments.create('laser_scan', 'laser_scan')


### control of LT1; comment this if adwin is operated from lt1-computer
### set lt1_control to False if LT1 is supposed to work independently
lt1_control=True

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
            opt1d_counts_lt1,dimension_set='lt1')

    objsh.start_glibtcp_client('192.168.0.20')
    remote_ins_server=objsh.helper.find_object('qtlab_lt1:instrument_server')
    powermeter_lt1 = qt.instruments.create('powermeter_lt1', 'Remote_Instrument',
                     remote_name='PM', inssrv=remote_ins_server)
    SMB_100_lt1 = qt.instruments.create('SMB_100_lt1', 'Remote_Instrument',
                     remote_name='SMB100', inssrv=remote_ins_server)
    GreenAOM_lt1 = qt.instruments.create('GreenAOM_lt1', 'AOM', 
            use_adwin=adwin_lt1, use_pm = powermeter_lt1)         
    NewfocusAOM_lt1 = qt.instruments.create('NewfocusAOM_lt1', 'AOM', 
            use_adwin=adwin_lt1, use_pm = powermeter_lt1)         
    MatisseAOM_lt1 = qt.instruments.create('MatisseAOM_lt1', 'AOM', 
            use_adwin=adwin_lt1, use_pm = powermeter_lt1)   
    laser_scan_lt1 = qt.instruments.create('laser_scan_lt1', 'laser_scan_lt1')
    
    setup_controller_lt1 = qt.instruments.create('setup_controller_lt1',
        'setup_controller',
        use = { 'master_of_space_lt1' : 'mos'} )

    servo_ctrl_lt1=qt.instruments.create('ServoController_lt1',
            'ParallaxServoController', address=4)
    ZPLServo_lt1=qt.instruments.create('ZPLServo_lt1','ServoMotor',
            servo_controller='ServoController_lt1')

###
### end of lt1-control


### Pannel instruments
setup_controller = qt.instruments.create('setup_controller',
    'setup_controller',
    use = { 'master_of_space' : 'mos'} )

