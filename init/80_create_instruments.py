bs_measurement_helper = qt.instruments.create('bs_measurement_helper', 'remote_measurement_helper', exec_qtlab_name = 'qtlab_bs')

conrad_relay=qt.instruments.create('conrad_relay','Conrad_Relaycard', address=1)