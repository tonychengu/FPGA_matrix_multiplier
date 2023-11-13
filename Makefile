# Makefile for cocotb simulation

# Specify the simulator (Icarus Verilog in this case)
SIM ?= icarus


PWD=$(shell pwd)
VERILOG_SOURCES = $(PWD)/../matrix_multiply.sv

# Top-level module name
TOPLEVEL := matrix_multiply

# Python test module name
MODULE := test_matrix_multiply.py

# Include cocotb's makefile
include $(shell cocotb-config --makefiles)/Makefile.sim

EXTRA_ARGS=-P matrix_multiply.c1=2 -P matrix_multiply.r1=3 -P matrix_multiply.r2=2

