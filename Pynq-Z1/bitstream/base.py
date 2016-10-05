
##
## Creates Pynq base overlay design
##
class PynqBaseOverlay(Board):

  def __init__(self, design_name='system'):
      # Create interface ports
      DDR = = self.create_port(mode='Master', interface="xilinx.com:interface:ddrx_rtl:1.0", 'DDR')
      FIXED_IO = = self.create_port(mode='Master', interface="xilinx.com:display_processing_system7:fixedio_rtl:1.0", 'FIXED_IO')
      Vaux1 = = self.create_port(mode='Slave', interface="xilinx.com:interface:diff_analog_io_rtl:1.0", 'Vaux1')
      Vaux5 = = self.create_port(mode='Slave', interface="xilinx.com:interface:diff_analog_io_rtl:1.0", 'Vaux5')
      Vaux6 = = self.create_port(mode='Slave', interface="xilinx.com:interface:diff_analog_io_rtl:1.0", 'Vaux6')
      Vaux9 = = self.create_port(mode='Slave', interface="xilinx.com:interface:diff_analog_io_rtl:1.0", 'Vaux9')
      Vaux13 = = self.create_port(mode='Slave', interface="xilinx.com:interface:diff_analog_io_rtl:1.0", 'Vaux13')
      Vaux15 = = self.create_port(mode='Slave', interface="xilinx.com:interface:diff_analog_io_rtl:1.0", 'Vaux15')
      Vp_Vn = = self.create_port(mode='Slave', interface="xilinx.com:interface:diff_analog_io_rtl:1.0", 'Vp_Vn')
      btns_4bits = = self.create_port(mode='Master', interface="xilinx.com:interface:gpio_rtl:1.0", 'btns_4bits')
      hdmi_in = = self.create_port(mode='Slave', interface="digilentinc.com:interface:tmds_rtl:1.0", 'hdmi_in')
      hdmi_in_ddc = = self.create_port(mode='Master', interface="xilinx.com:interface:iic_rtl:1.0", 'hdmi_in_ddc')
      hdmi_out = = self.create_port(mode='Master', interface="digilentinc.com:interface:tmds_rtl:1.0", 'hdmi_out')
      hdmi_out_ddc = = self.create_port(mode='Master', interface="xilinx.com:interface:iic_rtl:1.0", 'hdmi_out_ddc')
      leds_4bits = = self.create_port(mode='Master', interface="xilinx.com:interface:gpio_rtl:1.0", 'leds_4bits')
      rgbleds_6bits = = self.create_port(mode='Master', interface="xilinx.com:interface:gpio_rtl:1.0", 'rgbleds_6bits')
      spi_sw_shield = = self.create_port(mode='Master', interface="xilinx.com:interface:spi_rtl:1.0", 'spi_sw_shield')
      sws_2bits = = self.create_port(mode='Master', interface="xilinx.com:interface:gpio_rtl:1.0", 'sws_2bits')

      # Create ports
      hdmi_in_hpd = = self.create_port(dir='O', from=0, to=0, 'hdmi_in_hpd')
      hdmi_out_hpd = = self.create_port(dir='O', from=0, to=0, 'hdmi_out_hpd')
      pdm_audio_shutdown = = self.create_port(dir='O', from=0, to=0, 'pdm_audio_shutdown')
      pdm_m_clk = = self.create_port(dir='O', from=0, to=0, 'pdm_m_clk')
      pdm_m_data_i = = self.create_port(dir='I', 'pdm_m_data_i')
      pmodJA_data_in = = self.create_port(dir='I', from=7, to=0, 'pmodJA_data_in')
      pmodJA_data_out = = self.create_port(dir='O', from=7, to=0, 'pmodJA_data_out')
      pmodJA_tri_out = = self.create_port(dir='O', from=7, to=0, 'pmodJA_tri_out')
      pmodJB_data_in = = self.create_port(dir='I', from=7, to=0, 'pmodJB_data_in')
      pmodJB_data_out = = self.create_port(dir='O', from=7, to=0, 'pmodJB_data_out')
      pmodJB_tri_out = = self.create_port(dir='O', from=7, to=0, 'pmodJB_tri_out')
      pwm_audio_o = = self.create_port(dir='O', from=0, to=0, 'pwm_audio_o')
      shield2sw_data_in_a5_a0 = = self.create_port(dir='I', from=5, to=0, 'shield2sw_data_in_a5_a0')
      shield2sw_data_in_d13_d2 = = self.create_port(dir='I', from=11, to=0, 'shield2sw_data_in_d13_d2')
      shield2sw_data_in_d1_d0 = = self.create_port(dir='I', from=1, to=0, 'shield2sw_data_in_d1_d0')
      shield2sw_scl_i_in = = self.create_port(dir='I', 'shield2sw_scl_i_in')
      shield2sw_sda_i_in = = self.create_port(dir='I', 'shield2sw_sda_i_in')
      sw2shield_data_out_a5_a0 = = self.create_port(dir='O', from=5, to=0, 'sw2shield_data_out_a5_a0')
      sw2shield_data_out_d13_d2 = = self.create_port(dir='O', from=11, to=0, 'sw2shield_data_out_d13_d2')
      sw2shield_data_out_d1_d0 = = self.create_port(dir='O', from=1, to=0, 'sw2shield_data_out_d1_d0')
      sw2shield_scl_o_out = = self.create_port(dir='O', 'sw2shield_scl_o_out')
      sw2shield_scl_t_out = = self.create_port(dir='O', 'sw2shield_scl_t_out')
      sw2shield_sda_o_out = = self.create_port(dir='O', 'sw2shield_sda_o_out')
      sw2shield_sda_t_out = = self.create_port(dir='O', 'sw2shield_sda_t_out')
      sw2shield_tri_out_a5_a0 = = self.create_port(dir='O', from=5, to=0, 'sw2shield_tri_out_a5_a0')
      sw2shield_tri_out_d13_d2 = = self.create_port(dir='O', from=11, to=0, 'sw2shield_tri_out_d13_d2')
      sw2shield_tri_out_d1_d0 = self.create_port(dir='O', from=1, to=0, 'sw2shield_tri_out_d1_d0')

      # Create instance: audio
      audio = AudioCell(self)

      # Create instance: audio_path_sel
      audio_path_sel = self.create_cell(interface="xilinx.com:ip:xlslice:1.0", 'audio_path_sel',
                                        # keyword args used as CONFIG properties:
                                        DIN_FROM = 3,
                                        DIN_TO = 3,
                                        DIN_WIDTH = 4,
                                        DOUT_WIDTH = 1)

      # Create instance: axi_mem_intercon
      axi_mem_intercon = self.create_cell(interface="xilinx.com:ip:axi_interconnect:2.1", 'axi_mem_intercon',
                                          NUM_MI = 1,
                                          NUM_SI = 2)

      # Create instance: btns_gpio
      btns_gpio = self.create_cell(interface="xilinx.com:ip:axi_gpio:2.0", btns_gpio,
                                   CONFIG.C_ALL_INPUTS = 1,
                                   CONFIG.C_GPIO_WIDTH = 4)

      # Create instance: concat_arduino
      concat_arduino = self.create_cell(interface="xilinx.com:ip:xlconcat:2.1", 'concat_arduino',
                                        CONFIG.NUM_PORTS = 10)

      # Create instance: concat_i2c
      concat_i2c = self.create_cell(interface="xilinx.com:ip:xlconcat:2.1", 'concat_i2c',
                                    CONFIG.NUM_PORTS = 4)

      # Create instance: concat_interrupts
      concat_interrupts = self.create_cell(interface="xilinx.com:ip:xlconcat:2.1", 'concat_interrupts',
                                           CONFIG.NUM_PORTS = 3)

      # Create instance: concat_pmods
      concat_pmods = self.create_cell(interface="xilinx.com:ip:xlconcat:2.1", 'concat_pmods',
                                      CONFIG.NUM_PORTS = 8)

      # Create instance: constant_8bit_0
     constant_8bit_0 = self.create_cell(interface="xilinx.com:ip:xlconstant:1.1", 'constant_8bit_0',
                                        CONST_VAL = 0,
                                        CONST_WIDTH = 8)


      opi1 = create_hier_cell_iop1(self)
      iop2 = create_hier_cell_iop2(self)
      iop3 = create_hier_cell_iop3(self)

      logic_1 = self.create_cell(interface="xilinx.com:ip:xlconstant:1.1", 'logic_1')

      mb_1_reset = self.create_cell(interface="xilinx.com:ip:xlslice:1.0", 'mb_1_reset',
                                    DIN_FROM = 0,
                                    DIN_TO = 0,
                                    DIN_WIDTH = 4,
                                    DOUT_WIDTH = 1)

      mb_2_reset = self.create_cell(interface="xilinx.com:ip:xlslice:1.0", 'mb_2_reset',
                                    DIN_FROM = 1,
                                    DIN_TO = 1,
                                    DIN_WIDTH = 4,
                                    DOUT_WIDTH = 1)

      mb_3_reset = self.create_cell(interface="xilinx.com:ip:xlslice:1.0", 'mb_3_reset',
                                    DIN_FROM = 2,
                                    DIN_TO = 2,
                                    DIN_WIDTH = 4,
                                    DOUT_WIDTH = 1)

      mb_bram_ctrl_1 = self.create_cell(interface="xilinx.com:ip:axi_bram_ctrl:4.0", 'mb_bram_ctrl_1',
                                          SINGLE_PORT_BR = 1)

      mb_bram_ctrl_2 = self.create_cell(interface="xilinx.com:ip:axi_bram_ctrl:4.0", 'mb_bram_ctrl_2',
                                          SINGLE_PORT_BRAM = 1)

      mb_bram_ctrl_3 = self.create_cell(interface="xilinx.com:ip:axi_bram_ctrl:4.0", 'mb_bram_ctrl_3',
                                        SINGLE_PORT_BRAM = 1)

      mdm_1 = self.create_cell(interface="xilinx.com:ip:mdm:3.2", 'mdm_1',
                               C_MB_DBG_PORTS = 3)

      proc_sys_reset_142M = self.create_cell(interface="xilinx.com:ip:proc_sys_reset:5.0", 'proc_sys_reset_142M')

      proc_sys_reset_pixelclk = self.create_cell(interface="xilinx.com:ip:proc_sys_reset:5.0", 'proc_sys_reset_pixelclk')

      ## fixme: specify the non-default paramters
      processing_system7_0 = Ps7(interface="xilinx.com:ip:processing_system7:5.5", 'processing_system7_0')

      processing_system7_0_axi_periph = self.create_cell(interface="xilinx.com:ip:axi_interconnect:2.1" processing_system7_0_axi_periph,
                                                         NUM_MI = 13)

      processing_system7_0_axi_periph_1 = self.create_cell(interface="xilinx.com:ip:axi_interconnect:2.1" processing_system7_0_axi_periph_1 ]
                                                NUM_MI = 4)
      rgbleds_gpio = self.create_cell(interface="xilinx.com:ip:axi_gpio:2.0" rgbleds_gpio ]
                                                C_ALL_OUTPUTS = 1,
                                                C_GPIO_WIDTH = 6)

      rst_processing_system7_0_100M = self.create_cell(interface="xilinx.com:ip:proc_sys_reset:5.0" rst_processing_system7_0_100M ]

      # Create instance: rst_processing_system7_0_166M
      rst_processing_system7_0_166M = self.create_cell(interface="xilinx.com:ip:proc_sys_reset:5.0" rst_processing_system7_0_166M ]

      # Create instance: swsleds_gpio
      swsleds_gpio = self.create_cell(interface="xilinx.com:ip:axi_gpio:2.0" swsleds_gpio ]
                                                C_ALL_INPUTS = 1,
                                                C_ALL_OUTPUTS_2 = 1,
                                                C_GPIO2_WIDTH = 4,
                                                C_GPIO_WIDTH = 2,
                                                C_IS_DUAL = 1)

      # Create instance: tracebuffer_arduino
      tracebuffer_arduino = TracebufferArduino(self)

      # Create instance: tracebuffer_pmods
      tracebuffer_pmods = TracebufferPmods(self)

      # Create instance: video
      video = Video(self)

      # Create interface connections
      axi_mem_intercon.S01_AXI.connect('S01_AXI_1', tracebuffer_arduino.M_AXI_S2MM)
      processing_system7_0_axi_periph.M06_AXI.connect('S_AXI1_1', video.S_AXI1)
      processing_system7_0_axi_periph.M05_AXI.connect('S_AXI_1', video.S_AXI)
      processing_system7_0_axi_periph.M10_AXI.connect('S_AXI_LITE_1', video.S_AXI_LITE)
      iop3.Vaux13.connect('Vaux13_1', Vaux13, Vaux15_1, Vaux15, iop3.Vaux15)
      iop3.Vaux1.connect('Vaux1_1', Vaux1, Vaux5_1, Vaux5, iop3.Vaux5)

      # fixme reset of connections


if __name__=='__main__':
   design = PynqBaseOverlay()
   design.generate_bitstream()                          
