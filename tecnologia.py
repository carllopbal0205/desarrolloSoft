import json
marca = {}

marca['Ubiquiti'] = []

marca['Ubiquiti'].append({
    'Tecnologia 1': 'airMax',
    'modelo1': 'LiteBeam AC',
    'modelo2': 'GigaBeam',
    'modelo3': 'Rocket Prism AC'})

marca['Ubiquiti'].append({
    'Tecnologia 2': 'airFiber',
    'modelo1': 'airFiber 5XHD',
    'modelo2': 'airFiber 60LR',
    'modelo3': 'airFiber 24HD'})

marca['Ubiquiti'].append({
    'Tecnologia 3': 'EdgeMax',
    'modelo1': 'EdgeRouter X',
    'modelo2': 'EdgePoint',
    'modelo3': 'EdgeSwitch Lite'})


#Segunda Tecnologia de Telecomunicaciones

marca['MikroTik'] = []

marca['MikroTik'].append({
    'Tecnologia 1': 'RouterOS',
    'modelo1': 'SistemaOperativo',
    'modelo2': 'Enrutamiento',
    'modelo3': 'Firewall'})

marca['MikroTik'].append({
    'Tecnologia 2': 'IoT Products',
    'modelo1': 'wAP LR8 kit',
    'modelo2': 'Antenna kit for LoRa',
    'modelo3': 'R11e-LR9'})

marca['MikroTik'].append({
    'Tecnologia 3': 'CCR',
    'modelo1': 'CCR1009-7G-1C-PC',
    'modelo2': 'CCR1016-12G',
    'modelo3': 'CCR1009-7G-1C-1S+PC'})

#Tercera Tecnologia de Telecomunicaciones

marca['CISCO'] = []

marca['CISCO'].append({
    'Tecnologia 1': 'Redes',
    'modelo1': 'Switches',
    'modelo2': 'Routers',
    'modelo3': 'Tecnologia inalambrica'})

marca['CISCO'].append({
    'Tecnologia 2': 'IoT',
    'modelo1': 'Redes Industriales',
    'modelo2': 'Seguridad Industrial',
    'modelo3': 'Administracion de datos'})

marca['CISCO'].append({
    'Tecnologia 3': 'Seguridad',
    'modelo1': 'Secure Firewall',
    'modelo2': 'Secure Endpoint',
    'modelo3': 'Umbrella'})
    


with open('tecnologia.json', 'w') as file:
    json.dump(marca, file, indent=4, sort_keys=True)
