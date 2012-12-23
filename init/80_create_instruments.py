import logging

#Hardware
lt1_remote=False


if not lt1_remote:

    physical_adwin = qt.instruments.create('physical_adwin','ADwin_Gold_II',
                     address=336)
    #wavemeter = qt.instruments.create('wavemeter','WS600_WaveMeter')
#     if objsh.start_glibtcp_client('192.168.0.30',port=12002, nretry=3, timeout=5):
#         remote_ins_server=objsh.helper.find_object('qtlab_lt2:instrument_server')
#         wavemeter = qt.instruments.create('wavemeter', 'Remote_Instrument',
#                      remote_name='wavemeter', inssrv=remote_ins_server)


AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014', 
        address='GPIB::1::INSTR',reset=False,numpoints=1e3)
SMB100 = qt.instruments.create('SMB100', 'RS_SMB100', 
        address='GPIB::28::INSTR', reset=False)
#PH_300 = qt.instruments.create('PH_300', 'PicoHarp_PH300')

powermeter = qt.instruments.create('powermeter','Thorlabs_PM100', address = 'ASRL2::INSTR')

# MillenniaLaser = qt.instruments.create('MillenniaLaser', 'Millennia_Pro', 
#         address='COM1')
# TemperatureController = qt.instruments.create('TemperatureController', 
#     'Lakeshore_340', address = 'GPIB::12::INSTR')
# NewfocusLaser = qt.instruments.create('NewfocusLaser', 'NewfocusVelocity', 
#             address='GPIB::8::INSTR')

# AttoPositioner = qt.instruments.create('AttoPositioner', 'Attocube_ANC350')

servo_ctrl=qt.instruments.create('ServoController', 'ParallaxServoController', address=7)
ZPLServo=qt.instruments.create('ZPLServo','ServoMotor',servo_controller='ServoController')
PMServo=qt.instruments.create('PMServo','ServoMotor',servo_controller='ServoController')

if not lt1_remote:
     
    adwin = qt.instruments.create('adwin', 'adwin_lt1', 
            physical_adwin='physical_adwin')
    
    counters = qt.instruments.create('counters', 'counters_via_adwin',
            adwin='adwin')
    
    master_of_space = qt.instruments.create('master_of_space', 
            'master_of_space_lt1', adwin='adwin')

    linescan_counts = qt.instruments.create('linescan_counts', 
            'linescan_counts', adwin='adwin', mos='master_of_space',
            counters='counters')
    
    scan2d = qt.instruments.create('scan2d', 'scan2d_counts',
            linescan='linescan_counts', mos='master_of_space',
            xdim='x', ydim='y', counters='counters')
     
    opt1d_counts = qt.instruments.create('opt1d_counts', 
            'optimize1d_counts', linescan='linescan_counts', 
            mos='master_of_space', counters='counters')

#     
#     optimiz0r = qt.instruments.create('optimiz0r', 'optimiz0r',opt1d_ins=
#             opt1d_counts,mos_ins=master_of_space,dimension_set='lt1')
    
#     GreenAOM = qt.instruments.create('GreenAOM', 'AOM', 
#             use_adwin='adwin', use_pm= 'powermeter')
#     NewfocusAOM = qt.instruments.create('NewfocusAOM', 'AOM', 
#             use_adwin='adwin', use_pm = 'powermeter')         
#     MatisseAOM = qt.instruments.create('MatisseAOM', 'AOM', 
#             use_adwin='adwin', use_pm = 'powermeter')
   
# #    laser_scan = qt.instruments.create('laser_scan', 'laser_scan')
#     
#    setup_controller = qt.instruments.create('setup_controller',
#        'setup_controller',
#        use = { 'master_of_space' : 'mos'} )
# 
#     #SMB100_lt1 = qt.instruments.create('SMB100', 'RS_SMB100', 
#     #    address='GPIB::28::INSTR', reset=False)


#scan2d_demo= qt.instruments.create('scan2d_demo','scan2d_demo')
#counters_demo=qt.instruments.create('counters_demo','counters_demo')
###
### end of lt1-control

