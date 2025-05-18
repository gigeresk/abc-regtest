.model ripple64_adder
.inputs a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12 a13 a14 a15 a16 a17 a18 a19 a20 a21 a22 a23 a24 a25 a26 a27 a28 a29 a30 a31 a32 a33 a34 a35 a36 a37 a38 a39 a40 a41 a42 a43 a44 a45 a46 a47 a48 a49 a50 a51 a52 a53 a54 a55 a56 a57 a58 a59 a60 a61 a62 a63 b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 b25 b26 b27 b28 b29 b30 b31 b32 b33 b34 b35 b36 b37 b38 b39 b40 b41 b42 b43 b44 b45 b46 b47 b48 b49 b50 b51 b52 b53 b54 b55 b56 b57 b58 b59 b60 b61 b62 b63 carry_in
.outputs sum0 sum1 sum2 sum3 sum4 sum5 sum6 sum7 sum8 sum9 sum10 sum11 sum12 sum13 sum14 sum15 sum16 sum17 sum18 sum19 sum20 sum21 sum22 sum23 sum24 sum25 sum26 sum27 sum28 sum29 sum30 sum31 sum32 sum33 sum34 sum35 sum36 sum37 sum38 sum39 sum40 sum41 sum42 sum43 sum44 sum45 sum46 sum47 sum48 sum49 sum50 sum51 sum52 sum53 sum54 sum55 sum56 sum57 sum58 sum59 sum60 sum61 sum62 sum63 carry_out

# Full adder bit 0
.names a0 b0 carry_in sum0 carry0_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 1
.names a1 b1 carry0_carry sum1 carry1_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 2
.names a2 b2 carry1_carry sum2 carry2_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 3
.names a3 b3 carry2_carry sum3 carry3_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 4
.names a4 b4 carry3_carry sum4 carry4_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 5
.names a5 b5 carry4_carry sum5 carry5_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 6
.names a6 b6 carry5_carry sum6 carry6_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 7
.names a7 b7 carry6_carry sum7 carry7_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 8
.names a8 b8 carry7_carry sum8 carry8_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 9
.names a9 b9 carry8_carry sum9 carry9_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 10
.names a10 b10 carry9_carry sum10 carry10_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 11
.names a11 b11 carry10_carry sum11 carry11_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 12
.names a12 b12 carry11_carry sum12 carry12_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 13
.names a13 b13 carry12_carry sum13 carry13_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 14
.names a14 b14 carry13_carry sum14 carry14_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 15
.names a15 b15 carry14_carry sum15 carry15_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 16
.names a16 b16 carry15_carry sum16 carry16_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 17
.names a17 b17 carry16_carry sum17 carry17_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 18
.names a18 b18 carry17_carry sum18 carry18_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 19
.names a19 b19 carry18_carry sum19 carry19_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 20
.names a20 b20 carry19_carry sum20 carry20_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 21
.names a21 b21 carry20_carry sum21 carry21_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 22
.names a22 b22 carry21_carry sum22 carry22_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 23
.names a23 b23 carry22_carry sum23 carry23_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 24
.names a24 b24 carry23_carry sum24 carry24_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 25
.names a25 b25 carry24_carry sum25 carry25_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 26
.names a26 b26 carry25_carry sum26 carry26_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 27
.names a27 b27 carry26_carry sum27 carry27_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 28
.names a28 b28 carry27_carry sum28 carry28_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 29
.names a29 b29 carry28_carry sum29 carry29_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 30
.names a30 b30 carry29_carry sum30 carry30_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 31
.names a31 b31 carry30_carry sum31 carry31_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 32
.names a32 b32 carry31_carry sum32 carry32_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 33
.names a33 b33 carry32_carry sum33 carry33_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 34
.names a34 b34 carry33_carry sum34 carry34_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 35
.names a35 b35 carry34_carry sum35 carry35_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 36
.names a36 b36 carry35_carry sum36 carry36_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 37
.names a37 b37 carry36_carry sum37 carry37_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 38
.names a38 b38 carry37_carry sum38 carry38_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 39
.names a39 b39 carry38_carry sum39 carry39_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 40
.names a40 b40 carry39_carry sum40 carry40_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 41
.names a41 b41 carry40_carry sum41 carry41_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 42
.names a42 b42 carry41_carry sum42 carry42_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 43
.names a43 b43 carry42_carry sum43 carry43_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 44
.names a44 b44 carry43_carry sum44 carry44_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 45
.names a45 b45 carry44_carry sum45 carry45_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 46
.names a46 b46 carry45_carry sum46 carry46_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 47
.names a47 b47 carry46_carry sum47 carry47_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 48
.names a48 b48 carry47_carry sum48 carry48_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 49
.names a49 b49 carry48_carry sum49 carry49_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 50
.names a50 b50 carry49_carry sum50 carry50_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 51
.names a51 b51 carry50_carry sum51 carry51_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 52
.names a52 b52 carry51_carry sum52 carry52_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 53
.names a53 b53 carry52_carry sum53 carry53_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 54
.names a54 b54 carry53_carry sum54 carry54_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 55
.names a55 b55 carry54_carry sum55 carry55_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 56
.names a56 b56 carry55_carry sum56 carry56_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 57
.names a57 b57 carry56_carry sum57 carry57_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 58
.names a58 b58 carry57_carry sum58 carry58_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 59
.names a59 b59 carry58_carry sum59 carry59_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 60
.names a60 b60 carry59_carry sum60 carry60_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 61
.names a61 b61 carry60_carry sum61 carry61_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 62
.names a62 b62 carry61_carry sum62 carry62_carry
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

# Full adder bit 63
.names a63 b63 carry62_carry sum63 carry_out
000 00
001 10
010 10
011 01
100 10
101 01
110 01
111 11

.end
