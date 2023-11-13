import os
import sys
from pathlib import Path

import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
from cocotb.runner import get_runner

import numpy as np

@cocotb.test()
async def test_matrix_multiply_randint(dut):
    # cocotb returns binary 
    c1 = 2
    r1 = 3
    r2 = 2
    for i in range(3):
        A = np.random.randint(1,200, size =(c1,r1))
        B = np.random.randint(1,200, size =(r1,r2))
        A_flat = A.flatten()
        B_flat = B.flatten()
        for ii in range(len(A_flat)):
            # dut.a[].value <=   assign is not working
            dut.a[len(A_flat) - ii - 1] <= A_flat[ii].item() # from MS to LS
        for ii in range(len(B_flat)):
            dut.b[len(B_flat) - ii - 1] <= B_flat[ii].item()

        await Timer(5, units='ns')

        real_C = np.matmul(A, B)
        test_C_flat = [int(j) for j in dut.c.value]
        test_C = np.array(test_C_flat).reshape(c1, r2)
        status = "Failed"
        if(np.array_equal(real_C, test_C)):
            status = "Passed"
        print("========================================================")
        print("Test %d %s" % (i+1, status) )
        print("Test A: \n", A)
        print("Test B: \n", B)
        print("test C: \n", test_C)
        print("real C: \n", real_C)

def test_adder_runner():
    """Simulate the adder example using the Python runner.

    This file can be run directly or via pytest discovery.
    """
    hdl_toplevel_lang = os.getenv("HDL_TOPLEVEL_LANG", "verilog")
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent

    verilog_sources = [proj_path /  "matrix_multiply.sv"]

    # equivalent to setting the PYTHONPATH environment variable
    sys.path.append(str(proj_path / "tests"))

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="matrix_multiply",
        always=True,
        build_args=["-P", "matrix_multiply.Col1=2", "-P", "matrix_multiply.Row1=3", "-P", "matrix_multiply.Row2=2"]
    )
    runner.test(hdl_toplevel="matrix_multiply", test_module="test_matrix_multiply")


if __name__ == "__main__":
    test_adder_runner()


# reference:  https://github.com/cocotb/cocotb/blob/d19464474ad2b990732f062359a2c144bc6e3fb8/examples/matrix_multiplier/tests/test_matrix_multiplier.py