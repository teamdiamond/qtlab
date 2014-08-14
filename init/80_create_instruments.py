# Some demo stuff in here, to get the idea

#Hardware

# if not lt1_remote:
physical_adwin = qt.instruments.create('physical_adwin','ADwin_Pro_II',
        address=336)
#physical_adwin_lt2 = qt.instruments.create('physical_adwin_lt2','ADwin_Pro_II',
#        address=352)

SMB100 = qt.instruments.create('SMB100', 'RS_SMB100', address='USB0::0x0AAD::0x005F::258299::INSTR', reset=False)

#labjack = qt.instruments.create('labjack', 'LabJack_U3')

powermeter = qt.instruments.create('powermeter','Thorlabs_PM100D', address='USB0::0x1313::0x8078::PM002587::INSTR')

wavemeter = qt.instruments.create('wavemeter','WS600_WaveMeter')
wavemeter.set_active_channel(3)

#TH_260N=qt.instruments.create('TH_260N', 'TimeHarp_TH260N')

#ivvi = qt.instruments.create('ivvi', 'IVVI', address = 'ASRL1::INSTR', numdacs = 4)
#servo_ctrl=qt.instruments.create('ServoController', 'ParallaxServoController', address=2)
#ZPLServo=qt.instruments.create('ZPLServo','ServoMotor', servo_controller='ServoController')
#PMServo=qt.instruments.create('PMServo','ServoMotor', servo_controller='ServoController', min_pos=330, max_pos=1500)

AWG = qt.instruments.create('AWG', 'Tektronix_AWG5014_09', 
    address='TCPIP0::192.168.0.51::inst0::INSTR', 
    reset=False, numpoints=1e3)
 
adwin = qt.instruments.create('adwin', 'adwin_lt4', 
        physical_adwin='physical_adwin')
counters = qt.instruments.create('counters', 'counters_via_adwin',
        adwin='adwin')

master_of_space = qt.instruments.create('master_of_space', 
        'master_of_space', adwin='adwin', dimension_set='mos_lt4')

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
        opt1d_counts, mos_ins=master_of_space, dimension_set='lt4')

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
PulseAOM = qt.instruments.create('PulseAOM', 'AOM', 
        use_adwin='adwin', use_pm ='powermeter')
#
##laser_scan = qt.instruments.create('laser_scan', 'laser_scan')
# 
setup_controller = qt.instruments.create('setup_controller',
         'setup_controller',
        use = { 'master_of_space' : 'mos'} )
#
if objsh.start_glibtcp_client('localhost', port=12003, nretry=3):
    remote_ins_server = objsh.helper.find_object('qtlab_lt4_monitor:instrument_server')
    labjack = qt.instruments.create('labjack', 'Remote_Instrument',
            remote_name='labjack', inssrv=remote_ins_server)
