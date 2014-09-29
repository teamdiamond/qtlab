HH_400 = qt.instruments.create('HH_400','HydraHarp_HH400')

if objsh.start_glibtcp_client('localhost', port=12003, nretry=2):
    remote_ins_server = objsh.helper.find_object('qtlab_bs_monitor:instrument_server')
    remote_measurement_helper = qt.instruments.create('remote_measurement_helper', 'Remote_Instrument',
            remote_name='bs_measurement_helper', inssrv=remote_ins_server)

# adwins
physical_adwin_lt4 = qt.instruments.create('physical_adwin_lt4','ADwin_Pro_II', address=341)


physical_adwin_lt3 = qt.instruments.create('physical_adwin_lt3','ADwin_Pro_II', address=339)


broadcast0r = qt.instruments.create('broadcast0r', 'broadcast0r')
broadcast0r.add_broadcast('counts_channel_0', 
							lambda: HH_400.get_CountRate0(), 
							lambda x: physical_adwin_lt4.Set_Par(43,x))
broadcast0r.add_broadcast('counts_channel_1', 
							lambda: HH_400.get_CountRate1(), 
							lambda x: physical_adwin_lt3.Set_Par(43,x))
#broadcast0r.start()