from measurement.lib.config import adwins as adwinscfg

physical_adwin = qt.instruments.create('physical_adwin','ADwin_Gold_I',address=1)


#physical_adwin_m1 = qt.instruments.create('physical_adwin_m1','ADwin_Pro_II',address=2, processor_type = 1012)

adwin = qt.instruments.create('adwin', 'adwin', 
    		    adwin=physical_adwin,
	        	processes = adwinscfg.config['adwin_telecom_processes'],
                default_processes = ['set_dac', 'read_adc'], 
                dacs = adwinscfg.config['adwin_telecom_dacs'],
                tags = ['virtual'],
                process_subfolder = 'adwin_gold_1',)

# edac40 = qt.instruments.create('edac40','EDAC40',MAC_address='\x00\x04\xA3\x13\xDA\x94')
# okotech_dm = qt.instruments.create('okotech_dm', 'OKOTech_DM',dac=qt.instruments['edac40'])

powermeter = qt.instruments.create('powermeter','Thorlabs_PM100D', address='USB0::0x1313::0x8078::P0008241::INSTR')
powermeter_telecom = qt.instruments.create('powermeter_telecom','Thorlabs_PM100D', address='USB0::0x1313::0x8078::P0008241::INSTR')#'USB0::0x1313::0x8078::P0008241::INSTR')#'USB0::0x1313::0x8078::P0003753::INSTR')





# counters = qt.instruments.create('counters', 'counters_via_adwin',
        # adwin='adwin')




# optimiz0r = qt.instruments.create('optimiz0r', 'optimiz0r', opt1d_ins=
#         opt1d_counts, mos_ins=master_of_space, dimension_set='rt2')

# c_optimiz0r = qt.instruments.create('c_optimiz0r', 'convex_optimiz0r', 
#     mos_ins=master_of_space, adwin_ins = adwin)

# GreenAOM = qt.instruments.create('GreenAOM', 'AOM', 
#         use_adwin='adwin', use_pm= 'powermeter')

# p7889 = qt.instruments.create('p7889','FastCom_P7889')

qTelecom_manager = qt.instruments.create('qTelecom_manager', 'qTelecom_manager',
        adwin='adwin', powermeter= 'powermeter_telecom')

# qTelecom_plot_manager = qt.instruments.create('qTelecom_plot_manager', 'qTelecom_plot_manager',
#         adwin='adwin', powermeter= 'powermeter_telecom')




###############
# Start setup #
###############

execfile(os.path.join(qt.config['startdir'],'rt2_scripts/setup_rt2.py'))