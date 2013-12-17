# Some demo stuff in here, to get the idea

#Hardware
lt1_remote=False

# if not lt1_remote:
physical_adwin = qt.instruments.create('physical_adwin','ADwin_Gold_II',
        address=336)
physical_adwin_lt2 = qt.instruments.create('physical_adwin_lt2','ADwin_Pro_II',
        address=352)

# AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014', 
#         address='GPIB::1::INSTR' ,reset=False, numpoints=1e3)

SMB100 = qt.instruments.create('SMB100', 'RS_SMB100', 
        address='GPIB::28::INSTR', reset=False)

# PH_300 = qt.instruments.create('PH_300', 'PicoHarp_PH300')

powermeter = qt.instruments.create('powermeter','Thorlabs_PM100', address='ASRL5::INSTR')

# MillenniaLaser = qt.instruments.create('MillenniaLaser', 'Millennia_Pro', 
#         address='COM1')

TemperatureController = qt.instruments.create('TemperatureController', 
     'Lakeshore_340', address = 'GPIB::12::INSTR')

# Velocity1 = qt.instruments.create('Velocity1', 'NewfocusVelocity', address='GPIB::8::INSTR')
# AttoPositioner = qt.instruments.create('AttoPositioner', 'Attocube_ANC350')
ivvi = qt.instruments.create('ivvi', 'IVVI', address = 'ASRL1::INSTR', numdacs = 4)
servo_ctrl=qt.instruments.create('ServoController', 'ParallaxServoController', address=3)
ZPLServo=qt.instruments.create('ZPLServo','ServoMotor', servo_controller='ServoController')
PMServo=qt.instruments.create('PMServo','ServoMotor', servo_controller='ServoController')

if not lt1_remote:

    AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014', 
        address='TCPIP0::192.168.0.22::inst0::INSTR', 
        reset=False, numpoints=1e3)
     
    adwin = qt.instruments.create('adwin', 'adwin_lt1', 
            physical_adwin='physical_adwin')
    
    counters = qt.instruments.create('counters', 'counters_via_adwin',
            adwin='adwin')
    
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

    optimiz0r = qt.instruments.create('optimiz0r', 'optimiz0r', opt1d_ins=
            opt1d_counts, mos_ins=master_of_space, dimension_set='lt1')

    c_optimiz0r = qt.instruments.create('c_optimiz0r', 'convex_optimiz0r', 
        mos_ins=master_of_space, adwin_ins = adwin)
    
  
    GreenAOM = qt.instruments.create('GreenAOM', 'AOM', 
            use_adwin='adwin', use_pm= 'powermeter')
    NewfocusAOM = qt.instruments.create('NewfocusAOM', 'AOM', 
            use_adwin='adwin', use_pm = 'powermeter')         
    MatisseAOM = qt.instruments.create('MatisseAOM', 'AOM', 
            use_adwin='adwin', use_pm = 'powermeter')
    YellowAOM = qt.instruments.create('YellowAOM', 'AOM', 
            use_adwin='adwin', use_pm ='powermeter')
    
    #laser_scan = qt.instruments.create('laser_scan', 'laser_scan')
     
    setup_controller = qt.instruments.create('setup_controller',
             'setup_controller',
            use = { 'master_of_space' : 'mos'} )
    
    if objsh.start_glibtcp_client('192.168.0.80', port=12002, nretry=3):
        remote_ins_server = objsh.helper.find_object('qtlab_lasermeister:instrument_server')
        labjack = qt.instruments.create('labjack', 'Remote_Instrument',
        remote_name='labjack', inssrv=remote_ins_server)
    
#positioner = qt.instruments.create('positioner', 'NewportAgilisUC2_v2', 
#        address = 'COM14')
#rejecter = qt.instruments.create('rejecter', 'laser_reject0r')


