def podio_olimpico(dayana,iago,derek):
  if derek < iago < dayana:
    return f'1 - {derek} minutos\n2 - {iago} minutos\n3 - {dayana} minutos\n'
  if iago < derek < dayana:
    return f'1 - {iago} minutos\n2 - {derek} minutos\n3 - {dayana} minutos\n'
  if dayana < iago < derek:
    return f'1 - {dayana} minutos\n2 - {iago} minutos\n3 - {derek} minutos\n'
  if dayana < derek < iago:
    return f'1 - {dayana} minutos\n2 - {derek} minutos\n3 - {iago} minutos\n'
  if iago < dayana < derek:
    return f'1 - {iago} minutos\n2 - {dayana} minutos\n3 - {derek} minutos\n'
  if derek < dayana < iago:
    return f'1 - {derek} minutos\n2 - {dayana} minutos\n3 - {iago} minutos\n'
  
    


