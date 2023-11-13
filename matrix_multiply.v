`timescale 1ns / 1ps
module matrix_multiply #(
    parameter Col1 = 2,
    parameter Row1 = 2,
    parameter Row2 = 2
) (
    input [Col1*Row1-1:0] a[15:0] ,
    input [Row1*Row2-1:0] b[15:0] ,
    output reg [Col1*Row2-1:0] c[15:0]
);

  integer i, j, k;
  always @(*) begin
    for (i = 0; i < Col1; i=i+1) begin
      for (j = 0; j < Row1; j=j+1) begin
        c[Col1*i + j] = 15'd0;
        for (k = 0; k < Row2; k=k+1) begin
          c[i*Row2+k] = c[i*Row2+k] + a[i*Row1+j] * b[j*Row2+k];
        end
      end
    end
  end
endmodule
