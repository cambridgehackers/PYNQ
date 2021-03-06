#   Copyright (c) 2016, Xilinx, Inc.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without 
#   modification, are permitted provided that the following conditions are met:
#
#   1.  Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#
#   2.  Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution.
#
#   3.  Neither the name of the copyright holder nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#   THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR 
#   PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF 
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__author__      = "Parimal Patel"
__copyright__   = "Copyright 2016, Xilinx"
__email__       = "pynq_support@xilinx.com"


import time
import struct
from pynq import MMIO
from pynq.iop import request_iop
from pynq.iop import iop_const
from pynq.iop import PMODA
from pynq.iop import PMODB
from pynq.iop import ARDUINO
from pynq.iop import PMOD_GROVE_G1
from pynq.iop import PMOD_GROVE_G2
from pynq.iop import PMOD_GROVE_G3
from pynq.iop import PMOD_GROVE_G4
from pynq.iop import ARDUINO_GROVE_G1
from pynq.iop import ARDUINO_GROVE_G2
from pynq.iop import ARDUINO_GROVE_G3
from pynq.iop import ARDUINO_GROVE_G4
from pynq.iop import ARDUINO_GROVE_G5
from pynq.iop import ARDUINO_GROVE_G6
from pynq.iop import ARDUINO_GROVE_G7

PMOD_GROVE_BUZZER_PROGRAM = "pmod_grove_buzzer.bin"
ARDUINO_GROVE_BUZZER_PROGRAM = "arduino_grove_buzzer.bin"

class Grove_Buzzer(object):
    """This class controls the Grove Buzzer.
    
    The grove buzzer module has a piezo buzzer as the main component. 
    The piezo can be connected to digital outputs, and will emit a tone 
    when the output is HIGH. Alternatively, it can be connected to an analog 
    pulse-width modulation output to generate various tones and effects.
    Hardware version: v1.2.

    Attributes
    ----------
    iop : _IOP
        I/O processor instance used by Grove Buzzer.
    mmio : MMIO
        Memory-mapped I/O instance to read and write instructions and data.
    log_interval_ms : int
        Time in milliseconds between sampled reads of the GROVE_BUZZER sensor.
        
    """
    def __init__(self, if_id, gr_pin): 
        """Return a new instance of an GROVE_Buzzer object. 
        
        Parameters
        ----------
        if_id : int
            IOP ID (1, 2, 3) corresponding to (PMODA, PMODB, arduino).
        gr_pin: list
            A group of pins on stickit connector or arduino shield.
            
        """
        if if_id in [PMODA, PMODB]:
            if not gr_pin in [PMOD_GROVE_G1, \
                              PMOD_GROVE_G2, \
                              PMOD_GROVE_G3, \
                              PMOD_GROVE_G4]:
                raise ValueError("Buzzer group number can only be G1 - G4.")
            GROVE_BUZZER_PROGRAM = PMOD_GROVE_BUZZER_PROGRAM
        elif if_id in [ARDUINO]:
            if not gr_pin in [ARDUINO_GROVE_G1, \
                              ARDUINO_GROVE_G2, \
                              ARDUINO_GROVE_G3, \
                              ARDUINO_GROVE_G4, \
                              ARDUINO_GROVE_G5, \
                              ARDUINO_GROVE_G6, \
                              ARDUINO_GROVE_G7]:
                raise ValueError("Buzzer group number can only be G1 - G7.")
            GROVE_BUZZER_PROGRAM = ARDUINO_GROVE_BUZZER_PROGRAM
        else:
            raise ValueError("No such IOP for grove device.")

        self.iop = request_iop(if_id, GROVE_BUZZER_PROGRAM)
        self.mmio = self.iop.mmio
        self.iop.start()
        
        # Write SCL and SDA pin config
        self.mmio.write(iop_const.MAILBOX_OFFSET, gr_pin[0])
        self.mmio.write(iop_const.MAILBOX_OFFSET+4, gr_pin[1])
        
        # Write configuration and wait for ACK
        self.mmio.write(iop_const.MAILBOX_OFFSET + \
                        iop_const.MAILBOX_PY2IOP_CMD_OFFSET, 1)
        while (self.mmio.read(iop_const.MAILBOX_OFFSET + \
                              iop_const.MAILBOX_PY2IOP_CMD_OFFSET) == 1):
            pass
        
    def play_tone(self, tone_period, num_cycles):
        """Play a single tone with tone_period for num_cycles
        
        Parameters
        ----------
        tone_period : int
            The period of the tone in microsecond.
        num_cycles : int
            The number of cycles for the tone to be played.
            
        Returns
        -------
        None
        
        """
        if (tone_period not in range(1,32768)):
            raise ValueError("Valid tone period is between 1 and 32767.")
        if (num_cycles not in range(1,32768)): 
            raise ValueError("Valid number of cycles is between 1 and 32767.")
        
        self.mmio.write(iop_const.MAILBOX_OFFSET, tone_period)
        self.mmio.write(iop_const.MAILBOX_OFFSET+4, num_cycles)
        
        self.mmio.write(iop_const.MAILBOX_OFFSET + \
                        iop_const.MAILBOX_PY2IOP_CMD_OFFSET, 0x3)
        while not (self.mmio.read(iop_const.MAILBOX_OFFSET + \
                                  iop_const.MAILBOX_PY2IOP_CMD_OFFSET) == 0):
            pass
            
    def play_melody(self):
        """Play a melody.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
                
        """
        self.mmio.write(iop_const.MAILBOX_OFFSET + \
                        iop_const.MAILBOX_PY2IOP_CMD_OFFSET, 0x5)
        while not (self.mmio.read(iop_const.MAILBOX_OFFSET + \
                                  iop_const.MAILBOX_PY2IOP_CMD_OFFSET) == 0):
            pass
            