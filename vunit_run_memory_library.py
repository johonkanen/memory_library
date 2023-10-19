#!/usr/bin/env python3

from pathlib import Path
from vunit import VUnit

# ROOT
ROOT = Path(__file__).resolve().parent
VU = VUnit.from_argv()

lib = VU.add_library("memory")
lib.add_source_files(ROOT / "fpga_ram/ram_configuration/ram_configuration_16x1024_pkg.vhd")
lib.add_source_files(ROOT / "fpga_ram" / "*.vhd")
lib.add_source_files(ROOT / "fpga_ram/fpga_ram_simulation" / "*.vhd")

fpga_internal_ram = VU.add_library("fpga_internal_ram")
fpga_internal_ram.add_source_files(ROOT / "fpga_internal_ram/ram_configuration_pkg.vhd")
fpga_internal_ram.add_source_files(ROOT / "fpga_internal_ram/ram_read_base_pkg.vhd")
fpga_internal_ram.add_source_files(ROOT / "fpga_internal_ram/dual_port_ram.vhd")
fpga_internal_ram.add_source_files(ROOT / "fpga_internal_ram/arch_sim_dual_port_ram.vhd")
fpga_internal_ram.add_source_files(ROOT / "testbench/dual_port_ram/tb_dual_port_ram.vhd")

lib.add_source_files(ROOT / "sorting_algorithms/sorting_simulation" / "*.vhd")

lib.add_source_files(ROOT / "fpga_memory_interface_tests" / "*.vhd")

lib.add_source_files(ROOT / "testbench/hyperram/hyperram_command_frames_tb.vhd")
VU.main()
