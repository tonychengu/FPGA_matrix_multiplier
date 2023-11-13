`timescale 1ns / 1ps
module matrix_multiply #(
    parameter Col1 = 2,
    parameter Row1 = 2,
    parameter Row2 = 2
) (
    input [15:0] a[Col1*Row1-1:0],
    input [15:0] b[Row1*Row2-1:0],
    output logic [15:0] c[Col1*Row2-1:0]
);


  integer i, j, k;
  always @(*) begin
    for (i = 0; i < Col1; i=i+1) begin
      for (j = 0; j < Row1; j=j+1) begin
        for (k = 0; k < Row2; k=k+1) begin
          if (c[i*Row2+k] === 'z || c[i*Row2+k] === 'x) begin
            c[i*Row2+k] = 15'd0;
          end
          c[i*Row2+k] = c[i*Row2+k] + a[i*Row1+j] * b[j*Row2+k];
        end
      end
    end
  end
endmodule

// module matrix_multiply_tb ();
//   reg [15:0] a_in[0:3];
//   reg [15:0] b_in[0:3];
//   wire [15:0] c_out[0:3];
//   matrix_multiply dut (.a(a_in), .b(b_in), .c(c_out));
//   initial begin
//     a_in[0] = 1;
//     a_in[1] = 2;
//     a_in[2] = 3;
//     a_in[3] = 4;
//     b_in[0] = 1;
//     b_in[1] = 2;
//     b_in[2] = 3;
//     b_in[3] = 4;
//     #3 $stop;
//   end

// endmodule
