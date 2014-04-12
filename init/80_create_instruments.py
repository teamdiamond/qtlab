HH_400 = qt.instruments.create('HH_400','HydraHarp_HH400')

if objsh.start_glibtcp_client('192.168.0.40', port=12003, nretry=2):
    remote_ins_server = objsh.helper.find_object('qtlab_lt3_monitor:instrument_server')
    remote_measurement_helper = qt.instruments.create('remote_measurement_helper', 'Remote_Instrument',
            remote_name='bs_measurement_helper', inssrv=remote_ins_server)