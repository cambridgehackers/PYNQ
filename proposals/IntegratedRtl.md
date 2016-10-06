Seamless Python Programmable Logic Interactions on Pynq-Z1
==========================================================

The Pynq Python framework makes it very easy to use python to interact
with external modules via standard interfaces such as SPI, I2C, HDMI.

These same modules could be ported to on a Raspberry Pi or
Arduino. They do not seem to expose the capabilities of the Zynq
programmable logic.

# Problem: It's too difficult to use the Pynq-Z1 Programmable Logic

If a user of Pynq-Z1 wants to incorporate their own RTL, they have to
download 10+ GB of Vivado, and learn to use it. To  extend the base
design with their RTL, they need to learn Verilog or VHDL, Verilog IP
Integrator, and they have to be able to package their RTL as an
IP. After they get a bitstream, they have to write some python code to
interact with their RTL through a memory mapped interface.

To me, this seems like a very steep learning curve. It's a gigantic
cliff. Even for someone who knows an RTL language, I think it's too
many steps. Too tedious for something that could be fun.

# Goals:

## G1: Enable incremental extension of base design

Rather than requiring users to package their RTL as an IP and to
modify the 3000 line base.tcl, provide a way to incorporate their IP
as an I/O processor instead of one of the provided I/O processors.

In addition, wrap simple Verilog modules with memory-mapped adapters:

    from pynq.verilog import VerilogIop

    iop = VerilogIop('''
       module (
              input CLK,

              // wrapper provides a value for x
              input x,

              // wrapper reads y
              output y,
              
              // pmod pins routed to pmod connector
              output pmod_d1,
              input pmod_d2,
              );
          assign pmod_d1 = x;
          assign y = pmod_d2;
       endmodule
    ''')
    pl = Base(pmod_iop1=iop))

For logic that needs some handshaking, e.g., FIFO, VerilogIop understands AXI stream interfaces:

    iop = VerilogIop('''
       module (
              input CLK,

              // AXI stream input to module
              input x_data,
              input x_valid,  // data is valid when this is 1
              output x_ready, // if not provided, data is assumed to be 

              // AXI stream output from module
              output y_data,
              output y_valid, // optional
              input  y_ready, // consume the value

              // wrapper reads y
              output y,
              
              // pmod pins routed to pmod connector
              output pmod_d1,
              input pmod_d2,
              );
          reg x_reg;
          assign x_ready = 1;
          assign y_valid = 1;
          assign pmod_d1 = x_reg;
          assign y_data = pmod_d2;
          always @(posedge CLK) begin
             if (x_valid == 1)
                x_reg = x_data;
             if (y_ready == 1) begin
                ...
             end
          end                 
       endmodule
    ''')
    pl = Base(pmod_iop1=iop))

Adapters can be provided for other common interface idioms as desired.

## G2: Enable bitstream generation without Vivado download

Rather than downloading and installing Vivado every quarter, provide a
mechanism for the Jupiter notebook kernel to use a build service. 

    # generates verilog from pl
    # checks for cached bitstream
    # if verilog is new or changed, send verilog to build server
    # build server re-users cached bitstreams or else builds
    # elapsed time, 1 second to 5 minutes
    bitstream = pl.generate_bitstream()

The service may require the user to have an account or the servce may
just authenticate with the PynqZ1 board itself.

## G3: Enable pythonic interactions with the RTL

Now that the user has a new bitstream incorporating their logic,
provide a way to interact with it from python using the generated
memory-mapped adapter.

    iop = VerilogIop('''
       module (
              input CLK,

              // wrapper provides a value for x
              input x,

              // wrapper reads y
              output y,
              
              // pmod pins routed to pmod connector
              output pmod_d1,
              input pmod_d2,
              );
          assign pmod_d1 = x;
          assign y = pmod_d2;
       endmodule
    ''')
    pl = Base(pmod_iop1=iop))
    pl.generate_bitstream().load()

    ## VerilogIop provides a set/get methods and corresponding logic for input ports and output ports
    pl.x = 1
    print("pl.y==%d' % pl.y)


For logic that needs some handshaking, e.g., FIFO, VerilogIop understands AXI stream interfaces:

    iop = VerilogIop('''
       module (
              input CLK,

              // AXI stream input to module
              input x_data,
              input x_valid,  // data is valid when this is 1
              output x_ready, // if not provided, data is assumed to be 

              // AXI stream output from module
              output y_data,
              output y_valid, // optional
              input  y_ready, // consume the value

              // wrapper reads y
              output y,
              
              // pmod pins routed to pmod connector
              output pmod_d1,
              input pmod_d2,
              );
          reg x_reg;
          assign x_ready = 1;
          assign y_valid = 1;
          assign pmod_d1 = x_reg;
          assign y_data = pmod_d2;
          always @(posedge CLK) begin
             if (x_valid == 1)
                x_reg = x_data;
          end                 
       endmodule
    ''')
    pl = Base(pmod_iop1=iop))
    pl.generate_bitstream().load()

    ## VerilogIop provides a set/get methods and corresponding logic for input ports and output ports
    pl.x = 1
    print("pl.y==%d' % pl.y)
    ## alternately, to distinguish from registers:
    pl.put_x(1)
    print("pl.y==%d' % pl.get_y())

## G4: Enable pythonic expression of RTL

Instead of using Verilog, provide [MyHdl](http://www.myhdl.org) modules.

# How achievable is this?

This is all very doable.

[Connectal](http://www.connectal.org) already provides solutions for
G1 and G3 when the RTL is written in Bluespec Systems Verilog
(BSV). Connectal is open source on
https://github.com/cambridgehackers/connectal.

Connectal includes a script for wrapping Verilog modules and for
constructing memory-mapped adapters for modules. This could be adapter
to implement pynq.verilog.VerilogIop.

We previously prototyped a build service so that people could use
Connectal on a zedboard without installing any new software.

Connectal [buildcache](https://github.com/cambridgehackers/buildcache)
is a tool that re-uses previous builds of unchanged sources. We use
this on Connectal's buildbot and in standard developer builds.

G4 adds a dependence to the project but does not change the technical
difficulty. Actually, if MyHdl was supported but not Verilog, it would
be easier because we would not have to parse Verilog.

