from rich import print
from rich.panel import Panel

class Control:
  def __init__(self, power = False, current_channel = 1, volume = 0):
    self.power = power
    self.current_channel = current_channel
    self.volume = volume

  def tur(self):
    while True:
      if self.power == False:
        print (Panel('[red]The TV is off[/]', title=' [ TV ]', width=30))
        print ('\n< CH1 >   - VOL2 +   ', end='')
      else:
        # Build channel display with yellow background on current channel
        channels = []
        for i in range(1, 6):
          if i == self.current_channel:
            channels.append(f'[on yellow]{i}[/]')
          else:
            channels.append(str(i))
        channel_str = ' '.join(channels)
        
        # Build volume display
        vol_on = '[on green] [/]' * self.volume
        vol_off = '[on grey50] [/]' * (5 - self.volume)
        
        print (Panel(f'CHANNEL = {channel_str}\nVOLUME  = {vol_on}{vol_off}', title=' [ TV ]', width=30))
        print ('\n< CH1 >   - VOL2 +   ', end='')
      turn = str(input(''))
      if turn == '0':
        break
      if turn == '@':
        self.power = not self.power  # Toggle between True and False
      if turn == '<':
        self.current_channel -= 1
        if self.current_channel < 1:
          self.current_channel = 5
      if turn == '>':
        self.current_channel += 1
        if self.current_channel > 5:
          self.current_channel = 1
      if turn == '-':
        self.volume -= 1
        if self.volume < 0:
          self.volume = 0
      if turn == '+':
        self.volume += 1
        if self.volume > 5:
          self.volume = 5


tv1 = Control()

tv1.tur()